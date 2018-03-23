#! python3
# countBugsZD.py - count bugs from zentao, then write to a csv
'''
使用方法：安装python3，将此文件和禅道平台导出的csv文件放到同一目录下，然后在此目录下运行cmd，输入“python countBugsZD.py”，根据提示输入文件名

注意：
本程序只根据特定规则统计；
被拒绝缺陷按照解决方案['不是BUG，测试需求理解错误', '不是BUG，测试操作错误']统计；
残留缺陷按照解决方案为'优化建议，暂不修改'或状态'未关闭'统计；
缺陷分布统计只统计所填写模块的最子模块，所以可能有模块重名的问题，未填写模块的统计为'其他'；
bug发现版本按影响版本统计，如果有多个只取第一个；
可能还存在其他问题，报告应根据实际情况修正。
'''

import csv, re, datetime

# 等级序列
gradeSort = ['致命', '严重', '一般', '轻微', '建议']
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


# 所属模块识别
# 110联动登记(#408)
moduleRegex = re.compile(r'(.+)\(#\d+\)$')

# redmine版本识别，去掉尾部（#xx）,有多个影响版本只取第一个
# v20180102(#31)\nv20180307(#32)
versionRegex = re.compile(r'^(.+)?\(#\d+\)')

# open csv
csvname = input('请输入待分析的csv文件名（带扩展名）：')
# csvname = 'zentao.csv'
bugsFile = open(csvname, encoding='UTF-8')
bugsList = list(csv.reader(bugsFile))

# get titles.index
titles = bugsList[0]     
trackerNum = titles.index('Bug类型')
statusNum = titles.index('Bug状态')
gradeNum = titles.index('严重程度')
moduleNum = titles.index('所属模块')
reasonNum = titles.index('解决方案')
reopenNum = titles.index('激活次数')
versionNum = titles.index('影响版本')
projectNum = titles.index('所属项目')
project = bugsList[1][projectNum] + '缺陷统计'
    
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
for i in range(1, len(bugsList)):
    # bug状态统计
    statusCount.setdefault(bugsList[i][statusNum], 0)
    statusCount[bugsList[i][statusNum]] += 1
    # 缺陷原因分析统计
    reasonCount.setdefault(bugsList[i][reasonNum], 0)
    reasonCount[bugsList[i][reasonNum]] += 1
    if bugsList[i][reasonNum] in ['不是BUG，测试需求理解错误', '不是BUG，测试操作错误']:
        # 被拒绝缺陷统计
        rgradeCount.setdefault(bugsList[i][gradeNum], 0)
        rgradeCount[bugsList[i][gradeNum]] += 1
        # 被拒绝缺陷原因分析统计
        rreasonCount.setdefault(bugsList[i][reasonNum], 0)
        rreasonCount[bugsList[i][reasonNum]] += 1
        continue
    if bugsList[i][reasonNum] == '优化建议，暂不修改' or bugsList[i][statusNum] != '已关闭':
        # 残留缺陷等级统计（有效BUG）
        sgradeCount.setdefault(bugsList[i][gradeNum], 0)
        sgradeCount[bugsList[i][gradeNum]] += 1
    # 陷类型统计（有效BUG）
    # 如果没填会出bug
    trackerCount.setdefault(bugsList[i][trackerNum], 0)
    trackerCount[bugsList[i][trackerNum]] += 1
    # 缺陷等级统计（有效BUG）
    gradeCount.setdefault(bugsList[i][gradeNum], 0)
    gradeCount[bugsList[i][gradeNum]] += 1
    # 重新打开缺陷统计
    reopenCount.setdefault(bugsList[i][reopenNum], 0)
    reopenCount[bugsList[i][reopenNum]] += 1
    # 按照缺陷分布统计（有效BUG）
    temp = bugsList[i][moduleNum]
    if temp != '0':
        module = moduleRegex.search(temp).group(1)
        moduleCount.setdefault(module, 0)
        moduleCount[module] += 1
    else:
        moduleCount.setdefault('其他', 0)
        moduleCount['其他'] += 1

    # 发现版本统计（有效BUG）
    version = versionRegex.search(bugsList[i][versionNum]).group(1)
    versionCount.setdefault(version, 0)
    versionCount[version] += 1

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