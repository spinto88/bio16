#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Uso la librería igraph y pandas.
import igraph
import pandas as pd

# ------- Cargo la informacion del problema ------------- #

# Cargo en el objeto graph la red de dolphins.gml.
graph = igraph.read('dolphins.gml')

# Leo la info sobre el sexo de los delfines.
dolphins_sex = pd.read_table('dolphinsGender.txt', header = None)    

# Le asigno a cada vértice la información sobre el nombre
# y el sexo, reflejado en el color del vertice en el plot.
# Verde es sexo desconocido.
color_dict = {'m': "blue", 'f': "pink"}
for i in range(len(dolphins_sex)):
    dolphin_name = dolphins_sex[0][i]
    dolphin_sex = dolphins_sex[1][i]
    for vs in graph.vs:
        if vs['label'] == dolphin_name:
            vs['name'] = dolphin_name
            vs['sex'] = dolphin_sex
            try:
                vs["color"] = color_dict[vs['sex']]
            except:
                vs["color"] = "green"


# -------------- Distintos layouts ------------------- #

# Grafo circular
layout = graph.layout_circle()
igraph.plot(graph, layout = layout)


# Grafo DrL
layout = graph.layout_drl()
igraph.plot(graph, layout = layout)


# Grafo Fruchterman - Reingold
layout = graph.layout_fruchterman_reingold()
igraph.plot(graph, layout = layout)

# Grafo Kamada Kawai
layout = graph.layout_kamada_kawai()
igraph.plot(graph, layout = layout)

# Grafo Large Graph Layout
layout = graph.layout_lgl()
igraph.plot(graph, layout = layout)

# Grafo Multidimensional Scaling
layout = graph.layout_mds()
igraph.plot(graph, layout = layout)

# Grafo Random
layout = graph.layout_random()
igraph.plot(graph, layout = layout)

# Grafo Reingold Tilford
layout = graph.layout_reingold_tilford()
igraph.plot(graph, layout = layout)

# Grafo Star
layout = graph.layout_star()
igraph.plot(graph, layout = layout)

# --------------------------------------------------- #
