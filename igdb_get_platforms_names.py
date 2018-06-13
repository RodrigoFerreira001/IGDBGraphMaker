# -*- coding: utf-8 -*-

from igdb_api_python.igdb import igdb

igdb = igdb("c00b1bbc30c379f30337f726be119a69")
import json
import os

#ids_list = [130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24] #nintendo
#ids_list = [7, 8, 38, 46, 48, 9] #sony
#ids_list = [12, 11, 49] #microsoft
# ids_list = [64, 29, 78, 35, 30, 32, 23] #sega

platform_names = open('platform_names.txt','w')

ids = [130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24,7, 8, 38, 46, 48, 9, 12, 11, 49, 64, 29, 78, 35, 30, 32, 23, 6]
for id in ids:

    result = igdb.platforms({
        'ids': id,
        'fields': 'name'
    })
    platform_names.write(result.body[0]['name'] + ' ' + str(id) + '\n')

platform_names.close()