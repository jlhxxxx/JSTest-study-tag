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


baseUrl = 'https://www.caribbeancom.com/'
# 121915_001
caribReg = re.compile(r'(\d+-\d+)')
for file in os.listdir('.'):
    if caribReg.search(file) == None:
        print('wrong reg: ', file)
        continue
    num = caribReg.search(file).group(1)
    # https://www.caribbeancom.com/moviepages/010914-518/index.html
    infoUrl = baseUrl + 'moviepages/' + num + '/index.html'
    # http://www.caribbeancom.com/moviepages/123014-001/images/l_l.jpg
    strUrl = baseUrl + 'moviepages/' + num + '/images/l_l.jpg'
    # https://www.caribbeancom.com/moviepages/123014-001/images/l/001.jpg
    po1Url = baseUrl + 'moviepages/' + num + '/images/l/001.jpg'
    po2Url = baseUrl + 'moviepages/' + num + '/images/l/002.jpg'
    po3Url = baseUrl + 'moviepages/' + num + '/images/l/003.jpg'
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
        movname = 'Carib ' + num + os.path.splitext(file)[1]
        movnameb = 'Carib ' + num + 'B' + os.path.splitext(file)[1]
        # infoname = '1pondo ' + num + ' ' + title + ' - ' + actor + '.json'
        strname = 'Carib ' + num + ' ' + title + ' str.jpg'
        try:
            os.rename(os.path.join('.', file), os.path.join('.', movname))
        except:
            os.rename(os.path.join('.', file), os.path.join('.', movnameb))
        # down(jsonUrl, os.path.join('.', infoname))
        down(strUrl, os.path.join('.', strname))
        
    print(file)
    
    



