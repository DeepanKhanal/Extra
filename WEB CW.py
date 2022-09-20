import requests

cookies = {
    '0ctf_csrf_cookie': 'f33a1f6fb165c24334ec99810cfc40fb',
    'ctf_session': '3c6123ef9734ddf7ed7a45a817bb40056777cd1c',
}

headers = {
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
}

data = {
    '0ctf_csrf_token': 'f33a1f6fb165c24334ec99810cfc40fb',
    'email': 'admin@admin.com',
    'password': 'dsdsf',
}

response = requests.post('https://ctf.0ops.sjtu.cn/login', cookies=cookies, headers=headers, data=data)
print(response.text)