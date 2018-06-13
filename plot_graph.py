from igraph import *

graph = Graph.Read_Ncol("games_graph.txt", directed=True)
graph.simplify()

print graph.maxdegree()

layout = graph.layout_fruchterman_reingold()

graph.vs().find('130')['name'] = 'Nintendo Switch'
graph.vs().find('87')['name'] = 'Virtual Boy'
graph.vs().find('99')['name'] = 'Family Computer (FAMICOM)'
graph.vs().find('33')['name'] = 'Game Boy'
graph.vs().find('22')['name'] = 'Game Boy Color'
graph.vs().find('19')['name'] = 'Super Nintendo Entertainment System (SNES)'
graph.vs().find('58')['name'] = 'Super Famicom'
graph.vs().find('21')['name'] = 'Nintendo GameCube'
graph.vs().find('4')['name'] = 'Nintendo 64'
graph.vs().find('5')['name'] = 'Wii'
graph.vs().find('159')['name'] = 'Nintendo DSi'
graph.vs().find('20')['name'] = 'Nintendo DS'
graph.vs().find('37')['name'] = 'Nintendo 3DS'
graph.vs().find('41')['name'] = 'Wii U'
graph.vs().find('137')['name'] = 'New Nintendo 3DS'
graph.vs().find('18')['name'] = 'Nintendo Entertainment System (NES)'
graph.vs().find('24')['name'] = 'Game Boy Advance'
graph.vs().find('7')['name'] = 'PlayStation'
graph.vs().find('8')['name'] = 'PlayStation 2'
graph.vs().find('38')['name'] = 'PlayStation Portable'
graph.vs().find('46')['name'] = 'PlayStation Vita'
graph.vs().find('48')['name'] = 'PlayStation 4'
graph.vs().find('9')['name'] = 'PlayStation 3'
graph.vs().find('12')['name'] = 'Xbox 360'
graph.vs().find('11')['name'] = 'Xbox'
graph.vs().find('49')['name'] = 'Xbox One'
graph.vs().find('64')['name'] = 'Sega Master System'
graph.vs().find('29')['name'] = 'Sega Mega Drive'
graph.vs().find('78')['name'] = 'Sega CD'
graph.vs().find('35')['name'] = 'Sega Game Gear'
graph.vs().find('30')['name'] = 'Sega 32X'
graph.vs().find('32')['name'] = 'Sega Saturn'
graph.vs().find('23')['name'] = 'Dreamcast'
graph.vs().find('6')['name'] = 'PC (Microsoft Windows)'


# layout = graph.layout_lgl() #talvez mais esparso

# layout = graph.layout_mds()

# layout = graph.layout_sugiyama()


visual_style = {}
visual_style["vertex_size"] = [20 + (200 * v.indegree() / float(graph.maxdegree())) for v in graph.vs()]
# visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
visual_style["vertex_label"] = graph.vs["name"]
# visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
visual_style["layout"] = layout
visual_style["bbox"] = (4096,4096)
visual_style["margin"] = 20

plot(graph, **visual_style)