import urllib.request


def get(url: str, header: list = {}):
    """
    HTTP GET获取
    :param url: URL地址
    :param header: HTTP头
    :return: row
    """
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3790.0 Safari/537.36'
    # Chrome76
    req = urllib.request.Request(url, headers=header)
    return urllib.request.urlopen(req).read()

def decode(url: str):
    return urllib.parse.unquote(url.split('/')[-1])