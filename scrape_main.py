import requests
from bs4 import BeautifulSoup


def crawl_hkexnews(search_type, stock_code):
    url = 'https://www3.hkexnews.hk/reports/dirsearch/search?sc_lang=en'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 发送GET请求获取页面内容
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # 获取__RequestVerificationToken
    verification_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')

    # 构造POST请求的表单数据
    data = {
        '__RequestVerificationToken': verification_token,
        'searchBy': 'stockCode',
        'StockCode': stock_code
    }

    # 发送POST请求
    response = requests.post(url, data=data, headers=headers)
    return response


if __name__ == "__main__":
    stock_code = "00005"  # 股份代码，例如"00005"
    res = crawl_hkexnews('stockCode', stock_code)
    print(res.text)
