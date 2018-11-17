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


baseUrl = 'https://www.1pondo.tv/'
# 121915_001
searchReg = re.compile(r'(\d+_\d+)')
for file in os.listdir('.'):
    if searchReg.search(file) == None:
        print('wrong reg: ', file)
        continue
    num = searchReg.search(file).group(1)
    # https://www.1pondo.tv/dyn/phpauto/movie_details/movie_id/101715_001.json
    jsonUrl = baseUrl + 'dyn/phpauto/movie_details/movie_id/' + num + '.json'
    strUrl = baseUrl + 'moviepages/' + num + '/images/str.jpg'
    # https://www.1pondo.tv/assets/sample/101715_001/popu/1.jpg
    po1Url = baseUrl + 'assets/sample/' + num + '/popu/1.jpg'
    po2Url = baseUrl + 'assets/sample/' + num + '/popu/2.jpg'
    po3Url = baseUrl + 'assets/sample/' + num + '/popu/3.jpg'
    try:
        r = requests.get(jsonUrl, proxies=proxies)
    except:
        print('ERROR:', jsonUrl)
    else:
        info = json.loads(r.text)
        actor = info['Actor']
        title = info['Title']
        movname = '1pondo ' + num + os.path.splitext(file)[1]
        movnameb = '1pondo ' + num + 'B' + os.path.splitext(file)[1]
        infoname = '1pondo ' + num + ' ' + title + ' - ' + actor + '.json'
        strname = '1pondo ' + num + ' str.jpg'
        try:
            os.rename(os.path.join('.', file), os.path.join('.', movname))
        except:
            os.rename(os.path.join('.', file), os.path.join('.', movnameb))
        down(jsonUrl, os.path.join('.', infoname))
        down(strUrl, os.path.join('.', strname))
        
    print(file)
    
    



