import networkx as nx
import nltk

s="Tom and Jerry are Rat.Tom loves Jerry"
G = nx.DiGraph()
sen=s.split(".")
for i in sen:
    k=nltk.pos_tag(nltk.word_tokenize(i))
    l=len(k)
    index=0
    noun = []
    i=0
    while i<l and k[i][1] != 'VBZ' and k[i][1] != 'VBN' and k[i][1] != 'VBP':
        if k[i][1] != 'CC' and k[i]!=',':
            noun.append(i)
            i=i+1
        else:
            i=i+1
    first=i-1
    
    for i in noun:
        print(k[i])
    
    for i in range(first+1,l):
        if k[i][1] == 'VBZ' or k[i][1] == 'VBD' or k[i][1] == 'VBN' or k[i][1] == 'VBP':
            second= i
            break
            
    print(k[second][0])
    
    for i in range(second,l):
        if k[i][1] == 'NNP' or k[i][1] == 'NN':
            print(k[i][0])
            for nindex in noun:
                if k[second][0]=='are' :
                    G.add_edge(k[nindex][0],k[i][0],w='is-a')
                else:
                    G.add_edge(k[nindex][0],k[i][0],w=k[second][0])
            
pos = nx.spring_layout(G)
#drawing
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=G.edges,
                       width=6)
#labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(G,'w')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)

#plt.axis('off')
#plt.show()