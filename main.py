# Ugly code here!!! (Just to test things out)
import csv
import urllib.request
import os
from urllib.request import urlopen
import ssl

contextWoo = ssl._create_unverified_context()

labels = []
data = []
twoDURLS = []

# bedding-fashion.csv ===> (155, 77) 155 products with 77 other attributes
with open('./csv/bedding-fashion.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            for r in row:
                labels.append(r)
            line_count += 1
        else:
            data.append(row)
            line_count += 1

# MainImage, Image2, Image3, Image4, Image5, Image6, Image7, Image8
MainIndex = labels.index('MainImage')
Image2Index = labels.index('Image2')
Image3Index = labels.index('Image3')
Image4Index = labels.index('Image4')
Image5Index = labels.index('Image5')
Image6Index = labels.index('Image6')
Image7Index = labels.index('Image7')
Image8Index = labels.index('Image8')
indices = [MainIndex, Image2Index, Image3Index, Image4Index, Image5Index, Image6Index, Image7Index, Image8Index]

def getAllImages(product, listOfIndeces):
    temp = []
    for index in listOfIndeces:
        temp.append(product[index])
    return temp

for product in data:
    twoDURLS.append(getAllImages(product, indices))
   

indexToStart = 59
toStart = twoDURLS[indexToStart:] 
j = indexToStart
for product in toStart:
    i = 0
    for imgURL in product:
        if (imgURL):
            urllib.request.urlretrieve(imgURL, f"./images/{j}_{i}.jpg")
            i += 1
    j += 1
    
# urllib.request.urlretrieve("https://via.placeholder.com/150", './images/test.jpg')

# print(twoDURLS)
# product - 1, 2, 3, 4, 5 => [1, 2, 3, 4, 5]
# product ...
# product ...
# product ...
# product ...
# product ...

# array = [product: [1, 2, 3, 4, 5], product, ...]