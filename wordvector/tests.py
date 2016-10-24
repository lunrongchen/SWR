from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from wordvector.models import WordVector
from rest_framework.test import force_authenticate

class Tests(APITestCase):
	# POST save a new wordvector
	def test_create_wordvector(self):
		# Create a JSON POST request
		response = self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 50, 'word_text' : 'NewYork', 'word_vector' : '[10.0,21,78]'}, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(WordVector.objects.count(), 1)
		self.assertEqual(WordVector.objects.get().data_src, 'News')
		self.assertEqual(WordVector.objects.get().dimension, 50)
		self.assertEqual(WordVector.objects.get().word_text, 'New York')
		self.assertEqual(WordVector.objects.get().word_vector, '[10.0,21,78]')

	# GET get a wordvectorlist
	def test_get_wordvectorlist(self):
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 50, 'word_text' : 'NewYork', 'word_vector' : '[10.0,21,78]'}, format='json')
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 100, 'word_text' : 'York', 'word_vector' : '[10.0,21,78, 90, 100]'}, format='json')
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 50, 'word_text' : 'New', 'word_vector' : '[10.0,21]'}, format='json')
		response = self.client.get('/wordvectors/')
		assert response.status_code == 200
		self.assertEqual(WordVector.objects.count(), 3)
		self.assertEqual(WordVector.objects.get(id = 1).dimension, 50)

	# GET get a wordvector by filter
	def test_get_wordvector(self):
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 50, 'word_text' : 'NewYork', 'word_vector' : '[10.0,21,78]'}, format='json')
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 100, 'word_text' : 'York', 'word_vector' : '[10.0,21,78, 90, 100]'}, format='json')
		self.client.post('/wordvectors/', {'data_src': 'News', 'dimension' : 50, 'word_text' : 'New', 'word_vector' : '[10.0,21]'}, format='json')
		response = self.client.get('/wordvectors/News/50/NewYork/')
		assert response.status_code == 200
		self.assertEqual(response.data[0]['data_src'], 'News')
		self.assertEqual(response.data[0]['word_vector'], '[10.0,21,78]')


		