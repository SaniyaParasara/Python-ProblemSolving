from collections import deque
#function to generate possible next states
def get_next_states(state):
    a,b = state

    #capacities of jugs
    jugA = 4
    jugB = 3

    states = []

    #fill jug A completely
    states.append((jugA,b))

    #fill jug B completely
    states.append((a,jugB))

    #Empty Jug A
    states.append((0,b))

    #Empty Jug B
    states.append((a,0))

    #pour water from A to B
    pour = min(a,jugB-b)
    states.append(a-pour,b+pour)

    
    #pour water from A to B
    pour = min(a,jugB-b)
    states.append(a+pour,b-pour)

    return states

#BFS implementation
def bfs():
    start = (0,0)
    goal = 2

    #queue for BFS
    queue = degue()

    #store state and path
    queue.append((start,[]))

    #to avoid visiting same states
    visited = set()

    while queue():
        current, path = queue.popft()
        a,b = current

        #if goal found
        if a == goal:
            return path +[current]

        #Mark state visited
        if current in visited:
            continue
        visited.add(current)
        
        #generate child states 
        for next_state in get_next_states(current):
            if next_state not in visited:
                queue.append((next_state,path +[current]))
            return none

        #run BFS
        solution = bfs()
        print('steps to reach goal :')

        for step in solution:
            print(step)
        














    
    










