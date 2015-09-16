__author__ = 'natahlie'
import numpy as np
import sys

def find_shortest_distance(dist, visited_set, n):
    shortest_distance = sys.maxint
    count = 0
    shortest_distance_node = -1

    while(count < n):
        if visited_set[count]== False & dist[count] <= shortest_distance:
            shortest_distance = dist[count]
            shortest_distance_node = count

        count +=1

    return shortest_distance_node



#construct our adjacency matrix
first_line = raw_input().split(" ")
n = int(first_line[0])
m = int(first_line[1])
print n
adj_matrix = np.empty((n, n))
adj_matrix.fill(sys.maxint)
print adj_matrix

i = 0
while i != m:
    temp_input = raw_input().split(" ")
    adj_matrix[int(temp_input[0])-1, int(temp_input[1])-1] = int(temp_input[2])
    adj_matrix[int(temp_input[1])-1, int(temp_input[0])-1] = int(temp_input[2])
    i+=1

origin = 0
goal = n-1

dist = np.empty(n)
shortest_set = np.empty(n)
count = 0

while(count < n):
    dist[count] =  sys.maxint
    shortest_set = 'FALSE'
    count+=1

dist[origin] =0

i = 0

while(i < n):
    #find min distance vertex from those not yet processed
    min_node = find_shortest_distance(dist, shortest_set,n)
    shortest_set[min_node] = True
    j = 0
    while(j < n):
        if(shortest_set[j]==False & adj_matrix[min_node][j])!=sys.maxint & dist[min_node]+adj_matrix[min_node][j] < dist[i]:
            dist[i] = dist[min_node] + adj_matrix[i][j]
        j += 1

    i += 1

i = 0
for i< n:
    print "Vertex: " + str(i+1) + " Distance from source: " + str(dist[i])
    i+=1
