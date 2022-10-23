Activity#01

class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost

graph = {'A': Node('A', None, ['B','C','E'], None),
         'B': Node('B', None, ['A','D','E'], None),
         'C': Node('C', None, ['A','F','G'], None),
         'D': Node('D', None, ['A','E'], None),
         'E': Node('E', None, ['A','B','D'], None),
         'F': Node('F', None, ['C'], None),
         'G': Node('G', None, ['C'], None)}

def BFS():
    initialState = 'D'
    goalState = 'F'
    graph = {'A': Node('A', None, ['B','C','E'], None),
            'B': Node('B', None, ['A','D','E'], None),
            'C': Node('C', None, ['A','F','G'], None),
            'D': Node('D', None, ['A','E'], None),
            'E': Node('E', None, ['A','B','D'], None),
            'F': Node('F', None, ['C'], None),
            'G': Node('G', None, ['C'], None)}
    frontier = [initialState]
    explored = []
while len(frontier)!=0:
    currentNode = frontier.pop(0)
    explored.append(currentNode)
    for child in graph [currentNode].actions:
        if child not in frontier and child not in explored:
            graph[child].parent = currentNode
            if graph[child].state == goalState:
                return actionSequence(graph, initialState, goalState)
            frontier.appenf(child)

solution = BFS()
print (solution)


Task#01

class Node :

    def __init__(self,state,parent,actions,cost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.cost=cost
def BFSCost():
    inital="Arad"
    goal="Neamt"
    graph={'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
           'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
           'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
           'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
           'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
           'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
           'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
           'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
           'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
           'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
           'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
           'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
           'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
           'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
           'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
           'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
           'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
           'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
           'Giurgiu' : Node('Giurgiu',None,[],[]),
           'Neamt' : Node('Neamt',None,[],[] ),
        }
    front=[inital]
    exp=[]
   
    while(len(front)!=0) : 
          cNode=front.pop(0)
          exp.append(cNode)
          print (cNode)
          for i in graph[cNode].actions :
              if i not in front and i not in exp:
                  graph[i].parent==cNode
                  if graph[i].state==goal:
                      return actionSequence(graph,inital,goal)
                  front.append(i)
def actionSequence(graph,inital,goal):
    sol=[goal]
    cp=graph[goal].parent
    while cp!=None:
        sol.append(cp)
        cp=graph[cp].parent
    sol.reverse()
    return sol
sol=BFSCost()
print(sol)

