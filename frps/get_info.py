# coding:utf-8
import urllib.request
import json

url = 'https://api.github.com/repos/fatedier/frp/releases/latest'
rs = urllib.request.urlopen(url)
data = json.loads(rs.read())
print(str(data['tag_name'])[1:])
