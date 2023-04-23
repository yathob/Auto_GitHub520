# 导入包
import requests
import re
import os

# 删除 上一次 追加进 HOSTS 内容
File = open(r'C:\Windows\System32\drivers\etc\hosts', encoding='UTF-8')
content = File.read()
File.close()

githubhost = re.findall(r'# GitHub520 Host Start(.*?)# GitHub520 Host End', content, re.S)
if len(githubhost) > 0:
    content = content.replace(githubhost[0], '')
    content = content.replace('# GitHub520 Host Start# GitHub520 Host End', '')

githubHostNew = requests.get('https://raw.hellogithub.com/hosts')

hosts = open(r"C:\Windows\System32\drivers\etc\hosts", 'w', encoding='UTF-8')
content = content + githubHostNew.text
hosts.write(content)
hosts.close()

dnsFlush = "ipconfig /flushdns"
os.system(dnsFlush)
print("github DNS刷新成功")
