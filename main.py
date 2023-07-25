# Ozner Leyva Mariscal A01742377
# Carolina González Leal A01284948
# Erick Siller Ojeda A01382929
# Valeria Enríquez Limón A00832782
# Santiago Martínez Vallejo A00571878

def read(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().replace('(', '').replace(')', '')
            node_from, node_to = line.split(',')

            
            if node_from in graph:
                graph[node_from].append(node_to)
            else:
                graph[node_from] = [node_to]
                
    return graph


def pagerank(graph, iterations):
    
  # First Iteration
  n = len(graph)
  pageranks = {node: 1 / n for node in graph}
    
  for _ in range(iterations):
    newPageranks = {}
    
    for node in graph: 
      newPageranks[node] = 0
      
      for nextNode in graph: 
        if node in graph[nextNode]:
          outlinks = len(graph[nextNode])
          newPageranks[node] += pageranks[nextNode] / outlinks
  
    pageranks = newPageranks
    
  return pageranks


presentation_example = {
  "1": ["2", "3"],
  "2": [],
  "3": ["1", "2", "5"],
  "4": ["5", "6"],
  "5": ["4", "6"],
  "6": ["4"]
}

graph = read("Nodes_graph_homework_PageRank.txt")

# To test with the presentation example page 13
# scores = pagerank(presentation_example, 2)

scores = pagerank(graph, 5)

# Print the PageRank scores
for node, score in scores.items():
    print(f'Node {node}: {score}')
