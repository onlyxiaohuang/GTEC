import requests

# 下文中的函数均单线程，不涉及多线程
def Get(url):
	return requests.get(url).json()

def Post(url, data):
	return requests.post(url, data).json()

def Put(url, data):
	return requests.put(url, data).json()

def Delete(url):
	return requests.delete(url).json()

import json
# 之后需要扩展到其他网页上
source_json = "../json/luogu.json"
with open("source_json") as f:
	data = json.load(f)
print(data)




