class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

graph = {'A': Node('A', None, ['B', 'E', 'C'], None),
         'B': Node('B', None, ['A', 'E', 'D'], None),
         'C': Node('C', None, ['A', 'F', 'G'], None),
         'D': Node('D', None, ['B', 'E'], None),
         'E': Node('E', None, ['A', 'B', 'D'], None),
         'F': Node('F', None, ['C'], None),
         'G': Node('G', None, ['C'], None),
        }

def bfs(g, initialstate, goalstate):
    frontier = {initialstate}
    explored = set()
    while len(frontier) != 0:
        currentNode = frontier.pop()
        explored.add(currentNode)
        for child in g[currentNode].actions:
            if child not in frontier and child not in explored:
                g[child].parent = currentNode
                if g[child].state == goalstate:
                    return actionSequence(g, initialstate, goalstate)
                frontier.add(child)

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

initialstate = input("Enter your initial state of graph: ")
goalstate = input("Enter your goal state of graph: ")

if initialstate.capitalize() in graph.keys():
    if goalstate.capitalize() in graph.keys():
        solution = bfs(graph, initialstate.capitalize(), goalstate.capitalize())
        print(solution)
    else:
        print("Wrong goal state")
else:
    print("Wrong initial state")
