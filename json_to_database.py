import os
import json
from igraph import *

games = {}
collections = {}
to_remove = []

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
graph.add_vertices(len(games))

for key, value in games.iteritems():
    #print key, ": ", value['name']
    if value.has_key('developers'):
        for developer in value['developers']:
            if(value.has_key('platforms')):
                for platform in value['platforms']:
                    #print '(',developer,',',platform,')'
                    graph.add_edges([(developer, platform)])
            else:
                print value['name'].encode('utf-8'), "has no platform"

    else:
        if(value.has_key('collection')):
            if collections.has_key(value['collection']):
                for developer in collections[value['collection']]:
                    if (value.has_key('platforms')):
                        for platform in value['platforms']:
                            # print '(',developer,',',platform,')'
                            graph.add_edges([(developer, platform)])
                    else:
                        print value['name'].encode('utf-8'), "has no platform"
            else:
                # print value['name'].encode('utf-8')#, "has no valid collection"
                to_remove.append(value['name'].encode('utf-8'))
        # else:
        #     print value['name'].encode('utf-8'), "has no collection or developer"

with open('games_graph.txt', 'w') as graph_file:
    Graph.write_edgelist(graph, graph_file)