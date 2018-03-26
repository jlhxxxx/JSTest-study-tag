#! python3
# downloadImagePlus.py - from huaban.com/boards/favorite/beauty/
import requests, bs4, os, sys, re, time

# add board or pin list
def addList(url, li, arg='board'):
    res = requests.get(url)
    res.raise_for_status()
    if arg=='board':
        searchReg = re.compile(r'"board_id":(\d+), "user_id":(\d+), "title":"(.+?)".*?"pin_count":(\d+)')
    else:
        searchReg = re.compile(r'"pin_id":(\d+), "user_id":(\d+).*?"key":"(.+?)", "type":"image/(.+?)"')
    results = searchReg.findall(res.text)
    for result in results:
        li.append(result)

# build all wanted boards list
def getBoardList(url, li, count):
    addList(url, li)
    for i in range((count-1)//20):
        burl = newBoardUrl(url, li)
        addList(burl, li)

# build all pins list in a board 
def getPinList(board, li):
    url = 'http://huaban.com/boards/' + board[0] + '/'
    addList(url, li, 'pin')
    for i in range((int(board[-1])-1)//30):
        purl = newBoardUrl(url, li, 30)
        addList(purl, li, 'pin')

# download pins        
def downImg(pin, path):
    url = 'http://img.hb.aicdn.com/' + pin[2]
    res = requests.get(url)
    res.raise_for_status()

    pinPath = os.path.join(path, pin[0]+'.'+pin[3])
    print(pinPath)
    imageFile = open(pinPath, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

# dealwith waterfall pages
# http://huaban.com/boards/19357616/?...max=337846652&limit=30&wfl=1
def newBoardUrl(url, li, num=20):
    newurl = url + '?max=' + li[-1][0] + '&limit='+str(num)+'&wfl=1'
    return newurl

homeUrl = 'http://huaban.com/boards/favorite/beauty/'
os.makedirs('D:\\huaban', exist_ok=True)
boardList = []
os.chdir('D:\\huaban')
existDir = os.listdir('.')
getBoardList(homeUrl, boardList, 40)
for board in boardList:
    boardPath = board[0]+'_'+board[2]
    if boardPath in existDir:
        continue
    os.makedirs(boardPath, exist_ok=True)

    pinList = []
    getPinList(board, pinList)
    for pin in pinList:
        try:
            downImg(pin, boardPath)
        except TimeoutError:
            time.sleep(5)
            print('TimeoutError')
            continue


print('done')    
