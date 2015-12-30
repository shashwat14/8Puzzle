from DataStructures import Queue, Node, Stack


def UP(stateNode):
    state2 = stateNode.state[:]
    space = state2.index(0)
    if space>2 and space<9:
        temp = state2[space-3]
        state2[space] = temp
        state2[space-3] = 0
        leafNode = Node(' ')
        leafNode.state = state2
        leafNode.parent = stateNode
        leafNode.move = "Up"
        leafNode.distance = -1
        return leafNode
    else:
        return False

def DOWN(stateNode):
    state2 = stateNode.state[:]
    space = state2.index(0)
    if space>-1 and space<6:
        temp = state2[space+3]
        state2[space] = temp
        state2[space+3] = 0
        leafNode = Node(' ')
        leafNode.state = state2
        leafNode.parent = stateNode
        leafNode.move = "Down"
        leafNode.distance = -1
        return leafNode
    else:
        return False

def LEFT(stateNode):
    state2 = stateNode.state[:]
    space = state2.index(0)
    if space!= 0 and space != 3 and space != 6:
        temp = state2[space-1]
        state2[space] = temp
        state2[space-1] = 0
        leafNode = Node(' ')
        leafNode.state = state2
        leafNode.parent = stateNode
        leafNode.move = "Left"
        leafNode.distance = -1
        return leafNode
    else:
        return False


    

def RIGHT(stateNode):
    state2 = stateNode.state[:]
    space = state2.index(0)
    if space!= 2 and space != 5 and space != 8:
        temp = state2[space+1]
        state2[space] = temp
        state2[space+1] = 0
        leafNode = Node(' ')
        leafNode.state = state2
        leafNode.parent = stateNode
        leafNode.move = "Right"
        leafNode.distance = -1
        return leafNode
    else:
        return False
    
def moveGen(state):
    state1 = UP(state)
    state2 = DOWN(state)
    state3 = LEFT(state)
    state4 = RIGHT(state)

    states = [state1,state2,state3,state4]
    try:
        states.remove(False)
        states.remove(False)
    except:
        pass
    return states


def bfs(node,goal):
    print "Expanding Nodes.."
    Q = Queue()   
    Q.queue(node)

    count = 0
    visited = []
    while Q.size():
        current = Q.dequeue()
        count += 1
        #print count
        for node in moveGen(current):
            if node.state not in visited:
                visited.append(node.state)
                if node.state == goal.state:
                    return(node)
                Q.queue(node)


def reConst(goal):
    node = goal
    stack = Stack()
    while node!=None:
        stack.push(node)
        node = node.parent
    return stack


start = [1,2,3,4,6,8,7,5,0]
n = Node(' ')
n.state = start
n.parent = None
n.move = None
n.distance = -1

goal = [1,2,3,4,5,6,7,8,0]
p = Node(' ')
p.state = goal
p.parent = None
p.move = None
p.distance = -1

s = bfs(n,p)
print "Finished"
ss = reConst(s)
ss.pop()
print "Move the space tile in the following order: "
while ss.size():
    print ss.pop().move
