import zipfile
import re
from shutil import rmtree
from models import WordVector

class DataSetUploadHelper:

    def __init__(self, data_src_name, dimension, data_link):
        self.data_src_name = data_src_name
        self.dimension = dimension
        self.count = 0
        self.data_link = data_link
        pass

    def unzipFile(self):
        zip_ref = zipfile.ZipFile(self.data_link, 'r')
        zip_ref.extractall(self.data_src_name)
        zip_ref.close()

    def validateFile(self):
        file_path = self.data_link[:-(len(".zip"))]
        file_path = file_path + "/" + self.data_src_name + ".txt"
        data_file = open(file_path, 'r')

        for line in data_file:
            self.count = self.count + 1
            tmpCount = self.dimension
            for item in line.split('\t'):
                if re.match("^\d+?\.\d+?$", item):    #check float number
                    tmpCount = tmpCount - 1
            if(tmpCount != 0):
                print "Data set format is not valid for input dimension !"
                return -1

        data_file.close()
        return helper.count

    def saveToDataBase(self):
        file_path = self.data_link[:-(len(".zip"))]
        file_path = file_path + "/" + self.data_src_name + ".txt"
        data_file = open(file_path, 'r')

        for line in data_file:
            items = line.split('\t')
            word_text = items[0]
            word_vector = line[(len(word_text + '\t')):]
            # wordvector_tmp = WordVector(data_src=self.data_src_name, dimension=self.dimension,
            #                             word_text=word_text, word_vector=word_vector)
            # wordvector_tmp.save()
            print word_text
            print word_vector
        data_file.close()
        #update database table
        rmtree(self.data_link[:-(len(".zip"))])

helper = DataSetUploadHelper("data", 5, "data.zip")
helper.unzipFile()
helper.validateFile()
helper.saveToDataBase()
