from .models import ColourCatalog
import os


numOfCol = 8757
numOfColRal = 231
numOfColNcs = 1969
path_to_txt = os.path.normcase('C:/projects/website_Vlotho_QA/colourMix_page/txts/')

idOfCol = open(path_to_txt+"id.txt", "r")

baseType = open(path_to_txt+"baseType.txt", "r")

col1 = open(path_to_txt+"col1.txt", "r")
col2 = open(path_to_txt+"col2.txt", "r")
col3 = open(path_to_txt+"col3.txt", "r")
col4 = open(path_to_txt+"col4.txt", "r")



col1g = open(path_to_txt+"col1g.txt", "r")
col2g = open(path_to_txt+"col2g.txt", "r")
col3g = open(path_to_txt+"col3g.txt", "r")
col4g = open(path_to_txt+"col4g.txt", "r")

class ColourMix:


    def add_toDB():

        for x in range(numOfCol):

            print(x, 'added')
            ColourCatalog.objects.create(colour_id = idOfCol.readline().replace("\n", ""),
                                         base_type = baseType.readline().replace("\n", ""),
                                         colour1 = col1.readline().replace("\n", ""),
                                         colour2 = col2.readline().replace("\n", ""),
                                         colour3 = col3.readline().replace("\n", ""),
                                         colour4 = col4.readline().replace("\n", ""),
                                         colour1_grams = col1g.readline().replace("\n", "").replace(",", "."),
                                         colour2_grams = col2g.readline().replace("\n", "").replace(",", "."),
                                         colour3_grams = col3g.readline().replace("\n", "").replace(",", "."),
                                         colour4_grams = col4g.readline().replace("\n", "").replace(",", "."))

ColourMix.add_toDB()
