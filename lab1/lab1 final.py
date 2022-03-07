import sys

from maze import Maze, path_from


def bfs(maze):
    start_node = maze.find_node('S')
    q = [start_node]
    while len(q) > 0:
        node = q.pop(0)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                q.append(child)

    return None


def getCost(node):
    return node.cost


def dikstra(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse=False, key=getCost)
        node = q.pop(0)  # FIFO
        node.visited = True
        
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        
        for child in children:
            new_cost = node.cost
            maze.move_cost(node, node)

            if not child.visited:
                if new_cost < child.cost:
                    child.cost = new_cost
                child.parent = node
                q.append(child)

    return None


    
    
    
    
    
    
    
def minDist(curr):
    end_node = maze.find_node('E')
    return abs(curr.x-end_node.x)+abs(curr.y-end_node.y)

def gbfs(maze):
    start_node = maze.find_node('S')
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse=False, key=minDist)
        node = q.pop(0)  # FIFO
        node.visited = True
        
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        
        for child in children:
            if not child.visited:    
                child.parent = node
                q.append(child)

    return None


def getPr(node):
    return node.pr


def astar(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = [start_node]
    while len(q) > 0:
        q.sort(reverse=False, key=getPr)
        node = q.pop(0)  # FIFO
        node.visited = True
        
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        
        for child in children:
            new_cost = node.cost
            if child.type == '!':
                new_cost += 5
            else:
                new_cost += 1

            newPr = minDist(child)
            if new_cost < child.cost:
                child.pr = newPr+new_cost
                child.cost = new_cost
                child.parent = node
                q.append(child)

    return None


    
    
    



maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = astar(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end =' ')
print()
