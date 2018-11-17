import requests, json, os, re

proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

def down(url, path):
    try:
        r = requests.get(url, proxies=proxies)
    except:
        print('ERROR:', url)
    else:
        with open(path, 'wb') as fp:
            for chunk in r.iter_content(100000):
                fp.write(chunk)


baseUrl = 'http://www.heyzo.com/'
# 0953
caribReg = re.compile(r'(\d{4})')
for file in os.listdir('.'):
    if caribReg.search(file) == None:
        print('wrong reg: ', file)
        continue
    num = caribReg.search(file).group(1)
    # http://www.heyzo.com/moviepages/0953/index.html
    infoUrl = baseUrl + 'moviepages/' + num + '/index.html'
    # http://www.heyzo.com/contents/3000/0953/images/player_thumbnail.jpg
    strUrl = baseUrl + 'contents/3000/' + num + '/images/player_thumbnail.jpg'
    # http://www.heyzo.com/contents/3000/0953/gallery/001.jpg
    po1Url = baseUrl + 'contents/3000/' + num + '/gallery/l/001.jpg'
    po2Url = baseUrl + 'contents/3000/' + num + '/gallery/l/002.jpg'
    po3Url = baseUrl + 'contents/3000/' + num + '/gallery/l/003.jpg'
    try:
        r = requests.get(infoUrl, proxies=proxies)
    except:
        print('ERROR:', infoUrl)
    else:
        titleReg = re.compile(r'<title>(.+?) - .*?</title>')
        if titleReg.search(r.text) == None:
            print('wrong title: ', file)
            continue
        title = titleReg.search(r.text).group(1)
        # info = json.loads(r.text)
        # actor = info['Actor']
        # title = info['Title']
        movname = 'Heyzo ' + num + os.path.splitext(file)[1]
        # infoname = '1pondo ' + num + ' ' + title + ' - ' + actor + '.json'
        strname = 'Heyzo ' + num + ' ' + title + ' str.jpg'

        os.rename(os.path.join('.', file), os.path.join('.', movname))
        # down(jsonUrl, os.path.join('.', infoname))
        down(strUrl, os.path.join('.', strname))
        
    print(file)
    
    



