#! python3
# countBugsRED.py - count bugs from redmine, then write to a csv
'''
使用方法：安装python3，将此文件和redmine平台导出的csv文件（默认为issues.csv）放到同一目录下，然后在此目录下运行cmd，输入“python countBugsRED.py”

注意：
本程序只根据特定规则统计；
被拒绝缺陷按照状态为'被拒绝的'统计；
残留缺陷按照状态为'挂起的'统计；
缺陷分布统计只统计所填写模块的最子模块，所以可能有模块重名的问题；
缺陷原因统计以开发填写为准，若开发未填写则取测试填写的原因；
发现bug版本按目标版本统计，若未填目标版本，统计版本为''（空值）；
可能还存在其他问题，报告应根据实际情况修正。
'''

import csv, re, datetime

# 等级序列
gradeSort = ['致命的', '严重的', '一般的', '轻微的', '建议性的']
# 模块序列（需要手动补齐，否则不排序）
pass


# 自定义排序dic：传入li时，pos随便填，按li顺序排序；不传li时，pos=1按dic.value值逆序，pos=0按dic.key值正序
def sortDict(dic, pos=1, *li):
    out = []
    if li != ():
        li = list(li[0])
        for e in li:
            if e in dic:
                out.append([e.upper(), dic[e]])
        return out
    else:
        for k, v in dic.items():
            out.append((k.upper(), v))
        return sorted(out, key=lambda e: e[pos], reverse=pos)


# 所属模块识别，只取最子模块(模块名称可包含中文字母数字，模块分隔符为非中文字母数字)
# 1级模块 - 2级模块 ，3级模块  
moduleRegex = re.compile(r'([\u4e00-\u9fa5a-zA-Z0-9]+)\s*$')

# open csv
csvname = 'issues.csv'
bugsFile = open(csvname)
bugsList = list(csv.reader(bugsFile))

# get titles.index
titles = bugsList[0]
trackerNum = titles.index('跟踪')
statusNum = titles.index('状态')
gradeNum = titles.index('Bug等级')
moduleNum = titles.index('所属模块')
reasonNum = titles.index('BUG原因（开发定位）')
reopenNum = titles.index('被重新打开次数')
versionNum = titles.index('目标版本')
projectNum = titles.index('项目')
project = bugsList[1][projectNum] + '缺陷统计'

treasonNum = titles.index('BUG原因（测试定位）')

# --- 初始化 ---
# 跟踪
trackerCount = {}
# 状态
statusCount = {}
# bug等级
gradeCount = {}
# 被拒绝的bug等级
rgradeCount = {}
# 残留缺陷bug等级
sgradeCount = {}
# bug原因
reasonCount = {}
# 被拒绝bug的原因
rreasonCount = {}
# 重新打开统计
reopenCount = {}
# 所属模块
moduleCount = {}
# bug提出版本
versionCount = {}


# count all
# versionSet = set([])
for i in range(1, len(bugsList)):
    # bug状态统计
    statusCount.setdefault(bugsList[i][statusNum], 0)
    statusCount[bugsList[i][statusNum]] += 1
    # 缺陷原因分析统计
    if bugsList[i][reasonNum] != '':
        reasonCount.setdefault(bugsList[i][reasonNum], 0)
        reasonCount[bugsList[i][reasonNum]] += 1
    else:
        reasonCount.setdefault(bugsList[i][treasonNum], 0)
        reasonCount[bugsList[i][treasonNum]] += 1
    if bugsList[i][statusNum] == '被拒绝的':
        # 被拒绝缺陷统计
        rgradeCount.setdefault(bugsList[i][gradeNum], 0)
        rgradeCount[bugsList[i][gradeNum]] += 1
        # 被拒绝缺陷原因分析统计
        rreasonCount.setdefault(bugsList[i][reasonNum], 0)
        rreasonCount[bugsList[i][reasonNum]] += 1
        continue
    if bugsList[i][statusNum] == '挂起的':
        # 残留缺陷等级统计（有效BUG）
        sgradeCount.setdefault(bugsList[i][gradeNum], 0)
        sgradeCount[bugsList[i][gradeNum]] += 1
    # 陷类型统计（有效BUG）
    trackerCount.setdefault(bugsList[i][trackerNum], 0)
    trackerCount[bugsList[i][trackerNum]] += 1
    # 缺陷等级统计（有效BUG）
    gradeCount.setdefault(bugsList[i][gradeNum], 0)
    gradeCount[bugsList[i][gradeNum]] += 1
    # 重新打开缺陷统计
    reopenCount.setdefault(bugsList[i][reopenNum], 0)
    reopenCount[bugsList[i][reopenNum]] += 1
    # 按照缺陷分布统计（有效BUG）
    module = moduleRegex.search(bugsList[i][moduleNum]).group(1)
    moduleCount.setdefault(module, 0)
    moduleCount[module] += 1
    # 按照发现缺陷版本统计（有效）
    versionCount.setdefault(bugsList[i][versionNum], 0)
    versionCount[bugsList[i][versionNum]] += 1

# write to a csv
outputFile = open(project+'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow([project])

outputWriter.writerow(['------2.1 按照缺陷等级统计（有效BUG）------'])
gradeList = sortDict(gradeCount, 1, gradeSort)
for i in gradeList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.2 按照缺陷类型统计（有效BUG）------'])
trackerList = sortDict(trackerCount)
for i in trackerList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.3 被拒绝缺陷统计------'])
rgradeList = sortDict(rgradeCount, 1, gradeSort)
for i in rgradeList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.4 残留缺陷及修复率统计（有效BUG）------'])
sgradeList = sortDict(sgradeCount, 1, gradeSort)
for i in sgradeList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.5 按照缺陷分布统计（有效BUG）------'])
for k, v in moduleCount.items():
    outputWriter.writerow([k, v])

outputWriter.writerow(['------2.6 按照发现缺陷版本统计（有效）------'])
versionList = sortDict(versionCount, 0)
for i in versionList:
    outputWriter.writerow(i)   

outputWriter.writerow(['------2.7 项目缺陷原因分析------'])
reasonList = sortDict(reasonCount)
for i in reasonList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.8 被拒绝缺陷原因分析------'])
rreasonList = sortDict(rreasonCount)
for i in rreasonList:
    outputWriter.writerow(i)

outputWriter.writerow(['------2.9 被重新打开缺陷统计与分析------'])
reopenList = sortDict(reopenCount, 0)
for i in reopenList:
    outputWriter.writerow(i)

outputFile.close()
print('done')
