from igraph import *
import numpy as np
from colormap import rgb2hex
import sys

#graph = Graph.Read_Ncol("games_graph.txt", directed=True)
graph = Graph.Read_GraphML(sys.argv[1])

# graph.simplify(combine_edges=dict(weight="sum", popularity="sum"))

# graph.vs().find('16130')['name'] = 'Nintendo Switch'
# graph.vs().find('16087')['name'] = 'Virtual Boy'
# graph.vs().find('16099')['name'] = 'Family Computer (FAMICOM)'
# graph.vs().find('16033')['name'] = 'Game Boy'
# graph.vs().find('16022')['name'] = 'Game Boy Color'
# graph.vs().find('16019')['name'] = 'Super Nintendo Entertainment System (SNES)'
# graph.vs().find('16058')['name'] = 'Super Famicom'
# graph.vs().find('16021')['name'] = 'Nintendo GameCube'
# graph.vs().find('16004')['name'] = 'Nintendo 64'
# graph.vs().find('16005')['name'] = 'Wii'
# graph.vs().find('16159')['name'] = 'Nintendo DSi'
# graph.vs().find('16020')['name'] = 'Nintendo DS'
# graph.vs().find('16037')['name'] = 'Nintendo 3DS'
# graph.vs().find('16041')['name'] = 'Wii U'
# graph.vs().find('16137')['name'] = 'New Nintendo 3DS'
# graph.vs().find('16018')['name'] = 'Nintendo Entertainment System (NES)'
# graph.vs().find('16024')['name'] = 'Game Boy Advance'
# graph.vs().find('16007')['name'] = 'PlayStation'
# graph.vs().find('16008')['name'] = 'PlayStation 2'
# graph.vs().find('16038')['name'] = 'PlayStation Portable'
# graph.vs().find('16046')['name'] = 'PlayStation Vita'
# graph.vs().find('16048')['name'] = 'PlayStation 4'
# graph.vs().find('16009')['name'] = 'PlayStation 3'
# graph.vs().find('16012')['name'] = 'Xbox 360'
# graph.vs().find('16011')['name'] = 'Xbox'
# graph.vs().find('16049')['name'] = 'Xbox One'
# graph.vs().find('16064')['name'] = 'Sega Master System'
# graph.vs().find('16029')['name'] = 'Sega Mega Drive'
# graph.vs().find('16078')['name'] = 'Sega CD'
# graph.vs().find('16035')['name'] = 'Sega Game Gear'
# graph.vs().find('16030')['name'] = 'Sega 32X'
# graph.vs().find('16032')['name'] = 'Sega Saturn'
# graph.vs().find('16023')['name'] = 'Dreamcast'
# graph.vs().find('16006')['name'] = 'PC (Microsoft Windows)'



try:
    graph.vs().find('16070')['name'] = 'Nintendo'
except:
    pass

try:
    graph.vs().find('16100')['name'] = 'Sony'
except:
    pass

try:
    graph.vs().find('16128')['name'] = 'Microsoft'
except:
    pass

try:
    graph.vs().find('16112')['name'] = 'Sega'
except:
    pass
# layout = graph.layout_lgl() #talvez mais esparso

# layout = graph.layout_mds()

#layout = graph.layout_sugiyama()

# layout = graph.layout_circle()

# layout = graph.layout_auto()

# layout = graph.layout_fruchterman_reingold()
# coords =  layout.coords
#
# graph_layout = {}
# for v in graph.vs():
#     print v
#     graph_layout.update({v['name']: coords[v.index]})
#
# for key, value in graph_layout.iteritems():
#     print key, value
#
# np.save('graph_layout.npy', graph_layout)

read_dictionary = np.load('graph_layout.npy').item()
coords = []
for v in graph.vs():
    coords.append(read_dictionary[v['name']])

layout = Layout(coords = coords, dim = 2)

colors = []
for v in graph.vs():
    if v['name'] == 'Nintendo':
        colors.append(rgb2hex(255, 0, 0))
    elif v['name'] == 'Sony':
        colors.append(rgb2hex(0, 0, 255))
    elif v['name'] == 'Microsoft':
        colors.append(rgb2hex(0, 255, 0))
    elif v['name'] == 'Sega':
        colors.append(rgb2hex(0, 0, 0))
    else:
        r = 0
        g = 0
        b = 0
        a = False
        for neighbor in v.neighbors():
            if neighbor['name'] == 'Nintendo':
                r = 255
            elif neighbor['name'] == 'Sony':
                b = 255
            elif neighbor['name'] == 'Microsoft':
                g = 255
            elif neighbor['name'] == 'Sega':
                a = True

        if a:
            r = r - 100 if r == 255 else r
            g = g - 100 if g == 255 else g
            b = b - 100 if b == 255 else b

        colors.append(rgb2hex(r, g, b))

# for e in graph.es():
#     print e.source, e.target



max_weight = 0.0

for e in graph.es():
    if e['weight'] > max_weight:
        max_weight = e['weight']

print max_weight


vertex_size = []
for v in graph.vs():
    if v['name'] == 'Nintendo':
        vertex_size.append(50 + (400 * v.indegree() / float(graph.maxdegree())))
    elif v['name'] == 'Sony':
        vertex_size.append(50 + (400 * v.indegree() / float(graph.maxdegree())))
    elif v['name'] == 'Microsoft':
        vertex_size.append(50 + (400 * v.indegree() / float(graph.maxdegree())))
    elif v['name'] == 'Sega':
        vertex_size.append(50 + (400 * v.indegree() / float(graph.maxdegree())))
    else:
        # vertex_size.append(50 + (50 * v.outdegree() / float(graph.maxdegree(mode = 1))))
        weight = 0
        for neighbor in v.neighbors():
            weight += graph.es[graph.get_eid(v.index, neighbor.index)]['weight']

        weight /= len(v.neighbors())
        vertex_size.append(50 + (100 * weight / max_weight))


visual_style = {}
visual_style["vertex_size"] = vertex_size
visual_style["edge_width"] = [5 + (30 * e['weight'] / max_weight) for e in graph.es()]
visual_style["vertex_color"] = colors
visual_style["vertex_label"] = graph.vs["name"]
visual_style["layout"] = layout
visual_style["vertex_label_size"] = [10 + (150 * v.indegree() / float(graph.maxdegree())) for v in graph.vs()]
visual_style["bbox"] = (8192,8192)
visual_style["margin"] = 20


plot(graph, **visual_style)