# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    class dfsNode:
        def __init__(self, state, parent=None, action=None):
            self.state = state
            self.parent = parent
            self.action = action

        def backtrace(self):
            solution = list()
            node = self

            while node.parent != None:
                solution.insert(0, node.action)
                node = node.parent

            return solution

    state = problem.getStartState()
    if problem.isGoalState(state): # already there
        return []

    stack = util.Stack()
    visited = set()

    stack.push(dfsNode(state))

    while stack.isEmpty() == False:
        node = stack.pop()

        if problem.isGoalState(node.state):
            return node.backtrace()

        #print('visit %s' % (str(node.state)))
        visited.add(node.state)
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in visited:
                #print('  successor %s, action %s, stepCost %s' % (str(successor), str(action), str(stepCost)))
                stack.push(dfsNode(successor, node, action))
            else:
                #print('  redundant %s' % (str(successor)))
                pass

    # oops, find no path...
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    class bfsNode:
        def __init__(self, state, parent=None, action=None):
            self.state = state
            self.parent = parent
            self.action = action

        def backtrace(self):
            solution = list()
            node = self

            while node.parent != None:
                solution.insert(0, node.action)
                node = node.parent

            return solution

    state = problem.getStartState()
    if problem.isGoalState(state): # already there
        return []

    queue = util.Queue()
    visited = set()

    queue.push(bfsNode(state))

    while queue.isEmpty() == False:
        node = queue.pop()

        if problem.isGoalState(node.state):
            return node.backtrace()

        # bfs needs this to overcome loop
        if node.state in visited:
            continue

        #print('visit %s' % (str(node.state)))
        visited.add(node.state)
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in visited:
                #print('  successor %s, action %s, stepCost %s' % (str(successor), str(action), str(stepCost)))
                queue.push(bfsNode(successor, node, action))
            else:
                #print('  redundant %s' % (str(successor)))
                pass

    # oops, find no path...
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    class ufsNode:
        def __init__(self, state, parent=None, action=None, cost=0):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost

            if parent != None:
                self.cost += parent.cost

        def backtrace(self):
            solution = list()
            node = self

            while node.parent != None:
                solution.insert(0, node.action)
                node = node.parent

            return solution

    state = problem.getStartState()
    if problem.isGoalState(state): # already there
        return []

    queue = util.PriorityQueue()
    visited = set()

    root = ufsNode(state)
    queue.update(root, root.cost)

    while queue.isEmpty() == False:
        node = queue.pop()

        if problem.isGoalState(node.state):
            return node.backtrace()

        # bfs needs this to overcome loop
        if node.state in visited:
            continue

        #print('visit %s' % (str(node.state)))
        visited.add(node.state)
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in visited:
                #print('  successor %s, action %s, stepCost %s' % (str(successor), str(action), str(stepCost)))
                child = ufsNode(successor, node, action, stepCost)
                queue.update(child, child.cost)
            else:
                #print('  redundant %s' % (str(successor)))
                pass

    # oops, find no path...
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    class astarNode:
        def __init__(self, state, parent=None, action=None, cost=0):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost

            if parent != None:
                self.cost += parent.cost

        def backtrace(self):
            solution = list()
            node = self

            while node.parent != None:
                solution.insert(0, node.action)
                node = node.parent

            return solution

    state = problem.getStartState()
    if problem.isGoalState(state): # already there
        return []

    queue = util.PriorityQueue()
    visited = set()

    root = astarNode(state)
    queue.update(root, root.cost + heuristic(root.state, problem))

    while queue.isEmpty() == False:
        node = queue.pop()

        if problem.isGoalState(node.state):
            return node.backtrace()

        # bfs needs this to overcome loop
        if node.state in visited:
            continue

        #print('visit %s' % (str(node.state)))
        visited.add(node.state)
        for successor, action, stepCost in problem.getSuccessors(node.state):
            if successor not in visited:
                #print('  successor %s, action %s, stepCost %s' % (str(successor), str(action), str(stepCost)))
                child = astarNode(successor, node, action, stepCost)
                queue.update(child, child.cost + heuristic(child.state, problem))
            else:
                #print('  redundant %s' % (str(successor)))
                pass

    # oops, find no path...
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
