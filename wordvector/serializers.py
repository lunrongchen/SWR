import zipfile
import re
import django
import os
from rest_framework import serializers
from wordvector.models import WordVector, WordVectorFile
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from shutil import rmtree
os.environ['DJANGO_SETTINGS_MODULE'] = 'SWR.settings'

class DataSetUploadHelper:

    def __init__(self, data_src, dimension, data_count, data_link):
        self.data_src = data_src
        self.dimension = dimension
        self.data_count = data_count
        self.data_link = data_link
        pass

    def unzipFile(self):
        zip_ref = zipfile.ZipFile(self.data_link, 'r')
        zip_ref.extractall(self.data_src)
        zip_ref.close()

    def validateFile(self):
        file_path = self.data_link[:-(len(".zip"))]
        file_path = file_path + "/" + self.data_src + ".txt"
        print "file_path"
        print file_path[16:]
        data_file = open(file_path[16:], 'r')

        for line in data_file:
            self.data_count = self.data_count + 1
            tmpCount = self.dimension
            for item in line.split('\t'):
                if re.match("^\d+?\.\d+?$", item):    #check float number
                    tmpCount = tmpCount - 1
            if(tmpCount != 0):
                print "Data set format is not valid for input dimension !"
                return -1

        data_file.close()
        return self.data_count

    def saveToDataBase(self):
        file_path = self.data_link[:-(len(".zip"))] + "/" + self.data_src + ".txt"
        file_path = file_path[16:]
        data_file = open(file_path, 'r')

        for line in data_file:
            items = line.split('\t')
            word_text = items[0]
            word_vector = line[(len(word_text + '\t')):-1]
            wordvector_tmp = WordVector(data_src=self.data_src, dimension=self.dimension,
                                        word_text=word_text, word_vector=word_vector)
            wordvector_tmp.save()
        data_file.close()
        # WordVectorFile.update
        #update database table
        rmtree(self.data_src)
        

class WordVectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WordVector
        fields = ('id', 'data_src', 'dimension', 'word_text', 'word_vector')

class WordVectorFileSerializer(serializers.ModelSerializer):
    data_link = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = WordVectorFile
        fields = ('id', 'data_src', 'dimension', 'data_count', 'data_link')

    def create(self, validated_data):
        obj = WordVectorFile.objects.create(**validated_data)
        obj.save()
        data_link_path = "media/" + str(obj.data_link)
        helper = DataSetUploadHelper(obj.data_src, obj.dimension,
                                     obj.data_count, data_link_path)
        # print "\n\n\n\======================n\n\n\n"
        # print obj.data_src
        # print obj.dimension
        # print obj.data_count
        # print obj.data_link
        # print data_link_path
        # print "\n\n\n\======================n\n\n\n"
        helper.unzipFile()
        helper.validateFile()
        helper.saveToDataBase()

        return obj
