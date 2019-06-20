import json,csv,requests

def get(target):
    baseUrl = 'https://cgi.urlsec.qq.com/index.php?m=check&a=check&callback=&url=%s'
    headers = {'Referer': 'https://urlsec.qq.com/check.html'}
    result = ''
    r = requests.get(baseUrl % target, headers=headers)
    res = json.loads(r.text[1:-1])['data']['results']
    wt = res['whitetype']

    if wt == 3:
        wdres = '安全网站'
    elif wt == 1:
        wdres = '安全性未知'
    elif wt == 2:
        wdres = '危险网站'
    else:
        wdres = '安全网站'
    resList = [res['url'], wdres, '', '']
    result = '\n[-]当前检测域名：{0}\n  [*]网站检测结果：{1}'.format(res['url'], wdres)

    # 国内网站特有属性
    # res['Orgnization'] # 主办方
    # res['ICPSerial'] # 备案号

    if 'Orgnization' in res:
        resList[2] = res['Orgnization']
        result += '\n  [*]主办方：' + res['Orgnization']
    if 'ICPSerial' in res:
        resList[3] = res['ICPSerial']
        result += '\n  [*]备案号：' + res['ICPSerial']
    print(result)
    return resList


def ofile(fname):
    resLists = []
    try:
        with open(fname,'r') as f:
            url = f.readline()
            while url:
                resLists.append(get(url))
                url = f.readline()
            return resLists  # 二维列表
    except Exception as e:
        print(e)
        exit()


def wcsv(content):
    with open('./output.csv', 'w', newline='') as f:
        spanwriter = csv.writer(f, dialect='excel')
        spanwriter.writerow(['域名', '网站检测结果', '主办方', '备案号'])
        spanwriter.writerows(content)


if __name__ == '__main__':
    wcsv(ofile('./urls.txt'))