import requests
import re
import os

file = open(r'C:\Windows\System32\drivers\etc\hosts', encoding='UTF-8')
content = file.read()
file.close()

githubHostNew = requests.get('https://raw.hellogithub.com/hosts')
hosts = open(r"C:\Windows\System32\drivers\etc\hosts", 'w', encoding='UTF-8')
githubHost = re.findall(r'# GitHub520 Host Start(.*?)# GitHub520 Host End', content, re.S)

if len(githubHost) > 0:
    # 删除 上一次 HOSTS 中GitHub520内容
    content = content.replace(githubHost[0], '').replace('# GitHub520 Host Start# GitHub520 Host End', githubHostNew.text)
else:
    # 第一次直接追加
    content = content + '\n' + githubHostNew.text

hosts.write(content)
hosts.close()

dnsFlush = "ipconfig /flushdns"
os.system(dnsFlush)
print("github DNS刷新成功")
