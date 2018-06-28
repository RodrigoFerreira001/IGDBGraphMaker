import os
import json
from igraph import *

games = {}
collections = {}
to_remove = []

developers = set()
platforms = set()

#ids = [130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24,7, 8, 38, 46, 48, 9, 12, 11, 49, 64, 29, 78, 35, 30, 32, 23]
nintendo = [130, 87,99,33,22,19,58,21,4,5,159,20,37,41,137,18,24] #nintendo
sony = [7, 8, 38, 46, 48, 9] #sony
microsoft = [12, 11, 49] #microsoft
sega = [64, 29, 78, 35, 30, 32, 23] #sega

# companies = [70, 100, 128, 112]
companies = [70, 100, 128]

# ids = [99, 18, 64, 35, 33]
# thr_gen = [99, 18, 64, 35, 33]
# ids = [29, 19, 58, 78, 30]
# frt_gen = [29, 19, 58, 78, 30]
# ids = [32, 7 , 87, 4 , 22]
# fft_gen = [32, 7 , 87, 4 , 22]
# ids = [23, 8 , 24, 11, 21]
# sxt_gen = [23, 8 , 24, 11, 21]
# ids = [20, 159,38, 12, 9 , 5]
# svt_gen = [20, 159,38, 12, 9 , 5]
ids = [37, 46, 41, 48, 49, 130, 137]
# eth_gen = [37, 46, 41, 48, 49, 130, 137]


#le todos os json ja limpando os repetidos
for subdir, dirs, files in os.walk('games_json/'):
    for file in files:
        # print os.path.join(subdir, file)
        with open(os.path.join(subdir, file)) as file:
            game_json = json.load(file)
            if not games.has_key(str(game_json['id'])):
                games.update({str(game_json['id']): game_json})


for key, value in games.iteritems():
    if(value.has_key('collection') and value.has_key('developers')):
        # print value['name'].encode('utf-8'), "is in a collection"
        if not collections.has_key(value['collection']):
            collections.update({value['collection']: value['developers']})
#grafo
graph = Graph(directed=True)

#inserir os vertices
for key, value in games.iteritems():
    #print key, ": ", value['name']
    if value.has_key('developers'):
        for developer in value['developers']:
            if(value.has_key('platforms')):
                for platform in value['platforms']:
                    #print '(',developer,',',platform,')'
                    if platform in ids:
                        developers.add(developer)
                        platforms.add(platform)

    else:
        if(value.has_key('collection')):
            if collections.has_key(value['collection']):
                for developer in collections[value['collection']]:
                    if (value.has_key('platforms')):
                        for platform in value['platforms']:
                            if platform in ids:
                                developers.add(developer)
                                platforms.add(platform)

for developer in developers:
    graph.add_vertex(str(developer))

# for platform in platforms:
#     graph.add_vertex((platform + 16000))

for company in companies:
    graph.add_vertex(str(company + 16000))

for key, value in games.iteritems():
    #print key, ": ", value['name']
    if value.has_key('developers'):
        for developer in value['developers']:
            if(value.has_key('platforms')):
                for platform in value['platforms']:
                    #print '(',developer,',',platform,')'
                    if platform in ids:
                        if platform in nintendo:
                            #id 70
                            graph.add_edge(
                                str(developer), '16070', weight = (value['rating'] if value.has_key('rating') else 0),
                                pltfm = platform,
                                game = value['name'].encode('utf-8'), popularity = value['popularity'])
                            # graph.add_edges([(str(developer), '16070')])
                        elif platform in sony:
                            #id 100
                            graph.add_edge(
                                str(developer), '16100', weight=(value['rating'] if value.has_key('rating') else 0),
                                pltfm=platform,
                                game=value['name'].encode('utf-8'), popularity=value['popularity'])
                        elif platform in microsoft:
                            # id 128
                            graph.add_edge(
                                str(developer), '16128', weight=(value['rating'] if value.has_key('rating') else 0),
                                pltfm=platform,
                                game=value['name'].encode('utf-8'), popularity=value['popularity'])
                        else:
                            #id 112
                            graph.add_edge(
                                str(developer), '16112', weight=(value['rating'] if value.has_key('rating') else 0),
                                pltfm=platform,
                                game=value['name'].encode('utf-8'), popularity=value['popularity'])
                        #graph.add_edges([(developer, platform + 16000)])

    else:
        if(value.has_key('collection')):
            if collections.has_key(value['collection']):
                for developer in collections[value['collection']]:
                    if (value.has_key('platforms')):
                        for platform in value['platforms']:
                            if platform in ids:
                                if platform in nintendo:
                                    # id 70
                                    graph.add_edge(
                                        str(developer), '16070',
                                        weight=(value['rating'] if value.has_key('rating') else 0), pltfm=platform,
                                        game=value['name'].encode('utf-8'), popularity=value['popularity'])
                                elif platform in sony:
                                    # id 100
                                    graph.add_edge(
                                        str(developer), '16100',
                                        weight=(value['rating'] if value.has_key('rating') else 0), pltfm=platform,
                                        game=value['name'].encode('utf-8'), popularity=value['popularity'])
                                elif platform in microsoft:
                                    # id 128
                                    graph.add_edge(
                                        str(developer), '16128',
                                        weight=(value['rating'] if value.has_key('rating') else 0), pltfm=platform,
                                        game=value['name'].encode('utf-8'), popularity=value['popularity'])
                                else:
                                    # id 112
                                    graph.add_edge(
                                        str(developer), '16112',
                                        weight=(value['rating'] if value.has_key('rating') else 0), pltfm=platform,
                                        game=value['name'].encode('utf-8'), popularity=value['popularity'])

print "Platforms: ", len(platforms)
print "Developers: ", len(developers)


with open('eth_gen_games_graph.gml', 'w') as graph_file:
    #Graph.write_edgelist(graph, graph_file)
    graph.write_graphml(graph_file)