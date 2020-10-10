# Cleaner code here...
import csv
import urllib.request
import os
from urllib.request import urlopen
import ssl

class SaveImgFromCSV:
    def __init__(self, csv_file_name, delimiter=','):
        contextWoo = ssl._create_unverified_context()
        self.labels = []
        self.data = []
        self.twoDURLS = []
        with open(csv_file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for r in row:
                        self.labels.append(r)
                    line_count += 1
                else:
                    self.data.append(row)
                    line_count += 1
                    
    def getIndices(self):
        MainIndex = self.labels.index('MainImage')
        Image2Index = self.labels.index('Image2')
        Image3Index = self.labels.index('Image3')
        Image4Index = self.labels.index('Image4')
        Image5Index = self.labels.index('Image5')
        Image6Index = self.labels.index('Image6')
        Image7Index = self.labels.index('Image7')
        Image8Index = self.labels.index('Image8')
        indices = [MainIndex, Image2Index, Image3Index, Image4Index, Image5Index, Image6Index, Image7Index, Image8Index]
        return indices

    def __getAllImages(self, product):
        indices = self.getIndices()
        temp = []
        for index in indices:
            temp.append(product[index])
        return temp

    def __getProductsImgLinkArray(self):
        for product in self.data:
            self.twoDURLS.append(self.__getAllImages(product))
    
    def run(self, directory, startIndex=0):
        self.__getProductsImgLinkArray()
        indexToStart = startIndex
        toStart = self.twoDURLS[indexToStart:] 
        j = indexToStart
        for product in toStart:
            i = 0
            for imgURL in product:
                if (imgURL):
                    urllib.request.urlretrieve(imgURL, f"./{directory}/{j}_{i}.jpg")
                    i += 1
            j += 1