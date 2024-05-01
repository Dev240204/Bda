j1_max = int(input("Enter capacity of jug1"))
j2_max = int(input("Enter capacity of jug2"))
goal = int(input("Enter the goal"))

method = input("BFS OR DFS ")
if method == "BFS":
    index = 0
else:
    index = -1

visited = []
queue = [(0,0)]
while(queue):
    current = queue[index]

    queue.pop(index)
    if current not in visited:
        visited.append(current)
        j1=current[0]
        j2=current[1]
        if((j1<j1_max)):
            queue.append((j1_max,j2))
        if((j2<j2_max)):
            queue.append((j1,j2_max))

        if((j1>0)):
            queue.append((0,j2))
        if((j2>0)):
            queue.append((j1,0))
        
        if((j1+j2)<=j1_max and j2>0):
            queue.append((j1+j2,0))
        if((j1+j2)<=j2_max and j1>0):
            queue.append((0,j1+j2))
        
        if((j1+j2)>j1_max and (j2 - (j1_max-j1)>0 and (current!=(j1_max,j2_max)))):
            queue.append((j1_max,j2-(j1_max-j1)))

        if((j1+j2)>j2_max and (j1 - (j2_max-j2)>0 and (current!=(j1_max,j2_max)))):
            queue.append((j1-(j2_max-j2),j2_max))
        
        if((current[0]==0 and current[1]==goal)or(current[0]==goal and current[1]==0)):
            break
print(visited)
        
        
