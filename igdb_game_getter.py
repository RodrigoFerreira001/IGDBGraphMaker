# -*- coding: utf-8 -*-

from igdb_api_python.igdb import igdb

igdb = igdb("c00b1bbc30c379f30337f726be119a69")
import json
import os

#ids_list = [130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24] #nintendo
#ids_list = [7, 8, 38, 46, 48, 9] #sony
#ids_list = [12, 11, 49] #microsoft
ids_list = [64, 29, 78, 35, 30, 32, 23] #sega

for id in ids_list:
    result = igdb.platforms({
        # 'ids':[130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24],
        'ids': [id],
        'fields': ['games', 'name']
    })

    platform_name = result.body[0]['name']

    if not os.path.exists(str('games_json/' + platform_name)):
        os.makedirs(str('games_json/' + platform_name))

    games_id = result.body[0]['games']
    for i in range(0, len(games_id), 100):

        result = igdb.games({
            'ids': games_id[i: i + 100]
        })

        for game in result.body:
            game_json = open('games_json/' + platform_name + '/' + game['name'].replace('/', '_') + '.json', 'w')
            game_json.write(json.dumps(game, indent=4, sort_keys=True))
            game_json.close()