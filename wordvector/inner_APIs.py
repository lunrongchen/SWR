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

class Inner_Apis:
	#def GetDataSources():


	def GetWordVector(self, datasourcename,dims, word):
		s = 'http://127.0.0.1:8000/wordvectors/'+datasourcename + '/'+ str(dims) +'/'+ word+ '/';
		resp = requests.get(s)
		if resp.status_code != 200:
    		# This means something went wrong.
			raise ApiError('GET /tasks/ {}'.format(resp.status_code))
		for todo_item in resp.json():
			print('{}'.format(todo_item['word_vector']))
	def AddWordVector(self, datasourcename, dims, word, vector):
		task = {'data_src': datasourcename, 'dimension' : dims, 'word_text' : word, 'word_vector' : vector}
		resp = requests.post('http://127.0.0.1:8000/wordvectors/', json=task)
		if resp.status_code != 201:
			raise ApiError('POST /tasks/ {}'.format(resp.status_code))
		print('Created task. ID: {}'.format(resp.json()["id"]))

a = Inner_Apis();
a.GetWordVector('NU',50, 'Chicago');
a.AddWordVector('News', 50, 'NewYork', '[10.0,21,78]');