#!/usr/bin/env python

import sys
import os
import gv

def clean(text):
    text = text.replace('/','_')
    text = text.replace('.','_')
    return text

subgraphs = {}

def subgraphfun(graph,name,label):
    try:
        subgraph = subgraphs[name]
    except:
        subgraph = gv.graph(graph, 'cluster_' + name)
        gv.setv(subgraph, 'label', label)
        subgraphs[name] = subgraph

    return subgraph


graph = gv.digraph('filegraph')


for dirpath, dirnames, filenames in os.walk('src'):
    
    try:
        subgraph = subgraphs[clean(dirpath)]
    except:
        subgraph = gv.graph(graph, 'cluster_' + clean(dirpath))
        gv.setv(subgraph, 'label', dirpath)
        subgraphs[clean(dirpath)] = subgraph
    
    print clean(dirpath)
    print dirnames
    print filenames

    for filename in filenames:
        node = gv.node(subgraph, clean(filename))
        gv.setv(node, 'label', filename)


    for dirname in dirnames:
        subgraphfun(subgraph, clean(os.path.join(dirpath,dirname)), dirname)

gv.write(graph, 'graph.dot')

os.system('dot -Tpdf -ograph.pdf graph.dot')
#os.system('neato -Tpdf -ofilegraph.pdf filegraph.dot')
    
