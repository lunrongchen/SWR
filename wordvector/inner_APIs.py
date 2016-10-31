'''
5) Write python library with authentication to allow a python 
coder to call both of the APIs easily.

Python apis:
 
GetDataSources() 
-- returns a dictionary (?) with all data_sources, dims, and 
vocabulary size.
 
GetWordVector(datasourcename, dims, word) 
-- returns word vector as (probably) double array?
 
AddWordVector(datasourcename, dims, word, vector) 
-- adds word vector or sets word vector, returns success/failure
'''

import requests

class ApiError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)

class Inner_Apis:
	def GetDataSources(self, host):
		s = host + 'wordvectorfiles/'
		resp = requests.get(s)
		if resp.status_code != 200:
    		# This means something went wrong.
			raise ApiError('GET /tasks/ {}'.format(resp.status_code))
		result = [];
		for todo_item in resp.json():
			print('{}'.format(todo_item['data_src']))
			print('{}'.format(todo_item['dimension']))
			print('{}'.format(todo_item['data_count']))
			print('{}'.format(todo_item['data_link']))
			print todo_item;
			result.append(todo_item)
		print result
		return result;	

	def GetWordVector(self, host, datasourcename,dims, word):
		s = host + 'wordvectors/'+datasourcename + '/'+ str(dims) +'/'+ word+ '/';
		resp = requests.get(s)
		if resp.status_code != 200:
    		# This means something went wrong.
			raise ApiError('GET /tasks/ {}'.format(resp.status_code))
		for todo_item in resp.json():
			print('{}'.format(todo_item['word_vector']))
			return todo_item['word_vector']
	def AddWordVector(self, host, datasourcename, dims, word, vector):
		task = {'data_src': datasourcename, 'dimension' : dims, 'word_text' : word, 'word_vector' : vector}
		resp = requests.post(host + 'wordvectors/', json=task)
		if resp.status_code != 201:
			raise ApiError('POST /tasks/ {}'.format(resp.status_code))
		print('Created task. ID: {}'.format(resp.json()["id"]))
		return True;

a = Inner_Apis();
a.GetWordVector('http://127.0.0.1:8000/','NU',50, 'Chicago');
a.AddWordVector('http://127.0.0.1:8000/', 'NWU', 200, 'NewYorks', '[10.0,21,78]');
a.GetDataSources('http://127.0.0.1:8000/')