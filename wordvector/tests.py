from django.test import TestCase
from .models import WordVector

def make_WordVector(data_src,dimension,word_text,word_vector,doc):
	return WordVector.objects.create(data_src = data_src,dimension = dimension,word_text = word_text,word_vector = word_vector,doc = doc)

class SimpleTest(TestCase):
	def setUp(self):
		self.Youtube = make_WordVector('Youtube',10,'too much','[1,2,3]','http://127.0.0.1:8000/media/doc/glove.twitter.27B_1.zip')
		self.Google = make_WordVector('Google',20,'too much','[1,2,3]','http://127.0.0.1:8000/media/doc/glove.twitter.27B_1.zip')
		self.FaceBook = make_WordVector('FaceBook',10,'too much','[1,2,3]','http://127.0.0.1:8000/media/doc/glove.twitter.27B_1.zip')

	def test_wordVector(self):
		Youtube = self.Youtube
		self.assertEqual(Youtube.dimension,10)
		Google = self.Google
		self.assertEqual(Google.dimension,20)