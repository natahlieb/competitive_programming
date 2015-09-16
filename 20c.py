__author__ = 'natahlie'
import numpy as np


def find_shortest_distance(adj_matrix, origin_node, n):
    count = 0
    shortest_distance = 10000
    shortest_distance_node = -1
    while(count < n):
        if adj_matrix[origin_node][count]<shortest_distance:
            shortest_distance = adj_matrix[origin_node][count]
            shortest_distance_node = (count+1)
        count +=1

    return shortest_distance_node




first_line = raw_input().split(" ")
n = int(first_line[0])
m = int(first_line[1])
print n
adj_matrix = np.empty((n, n))
adj_matrix.fill(100000)
print adj_matrix

i = 0
while i != m:
    temp_input = raw_input().split(" ")
    adj_matrix[int(temp_input[0])-1, int(temp_input[1])-1] = int(temp_input[2])
    adj_matrix[int(temp_input[1])-1, int(temp_input[0])-1] = int(temp_input[2])
    i+=1

origin = 1
goal = n

dist = np.empty(n)
dist[origin-1] = 0
prev = np.empty(n)
prev[origin] = -1

nodes_not_visited = []

count = 1
nodes_not_visited.append(1)

while(count < n-1):
    dist[count] = 10000
    prev[count] = -1
    nodes_not_visited.append(count+1)
    count+=1


print nodes_not_visited
print dist
print count

while len(nodes_not_visited)!=0:
    shortest_distance

'''
print adj_matrix

nodes_not_visited = []
count = 1
while(count <= n):
    nodes_not_visited.append(count)
    count +=1



print nodes_not_visited

'''
'''

nodes_visited  = np.zeros(n)
nodes_visited[0] = 1

i = 1
distance_graph = np.empty(n)

while ( i < n):
    distance_graph[n]= adj_matrix[1][i]
    i+=1


distance_graph = np.empty(n)
distance_graph.fill(100000)
distance_graph[0] = 0

'''