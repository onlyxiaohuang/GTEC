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

import os
import json

# 之后需要扩展到其他网页上
#print(os.getcwd())
def get_data():
	current_path = os.getcwd()
	relative_path = "json/luogu.json"
	source_json = os.path.join(current_path, relative_path)

	with open(source_json) as f:
		data = json.load(f)
	
	if __debug__ == True:
		print(data)

def get_data_from_luogu():
	data = get_data()
	re = requests.get(data['website'],cookies=data['cookie'])

	if __debug__ == True:
		print(re.status_code)
		



