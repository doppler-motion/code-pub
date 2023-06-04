import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
url = ""

rsp_text = requests.get(url=url, verify=False,
                        timeout=15, headers=headers)

print(rsp_text.status_code)


