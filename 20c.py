__author__ = 'natahlie'
import numpy as np
import sys
import collections
from heapq import heappush, heappop
import Queue



def find_shortest_distance(dist, unprocessed_nodes, n):
    print dist
    shortest_distance = sys.maxint
    count = 0
    shortest_distance_node = -1

    while(count < n):
        if unprocessed_nodes[count]== 0:
            if dist[count+1] < shortest_distance:
                shortest_distance = dist[count]
                shortest_distance_node = count

        count +=1

    print shortest_distance_node
    return shortest_distance_node



#construct our adjacency matrix
first_line = raw_input().split(" ")
n = int(first_line[0])
adj_list = collections.defaultdict(dict)

m = int(first_line[1])

i = 0
while i != m:
    temp_input = raw_input().split(" ")
    adj_list[int(temp_input[0])][int(temp_input[1])] = int(temp_input[2])
    adj_list[int(temp_input[1])][int(temp_input[0])] = int(temp_input[2])
    i+=1

print adj_list

dist = [None] * n
processed = []
unprocessed = []
parent = [None] * n

i = 1
while i <= n:
    dist[i-1] = sys.maxint
    parent[i-1] = None
    unprocessed.append(i)
    i+=1


dist[0] = 0

print unprocessed
while len(processed)!=n:
    #find node with the smallest length
    min_node = find_shortest_distance(dist, unprocessed, n)
    if min_node == n:
        break
    processed.append(min_node)
    unprocessed.remove(min_node)

    for j in unprocessed:
        if dist[min_node] + adj_list[min_node][j] < dist[j]:
            dist[j] = dist[min_node] + adj_list[min_node[j]]
            parent[j] = min_node


print dist[n]




'''
origin_node = 1
A = [None] * n
queue = [(0, origin_node)]

while queue:
    path_len, v = heappop(queue)
    if A[v] is None:
        A[v] = path_len
        for w in adj_list[v]:
            if A[w-1] is None:
                edge_len = adj_list[v][w]
                heappush(queue, (path_len + edge_len, w))


print [0 if x is None else x for x in A]
'''