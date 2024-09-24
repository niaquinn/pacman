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

from searchAgents import PositionSearchProblem
import util
import pacman
import game

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
    """
    print("Start: ", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    frontier = util.Stack()
    # add initial node to frontier

    startNode = Node()
    frontier.push(startNode)

    explored = {}

    while not frontier.isEmpty():

        nextNode = frontier.pop()
        state = nextNode.getState()
        successors = nextNode.allSuccessors()

        if state.isGoalState():
            actions = []
            for successor in successors:
                actions.append(successor.getAction())
            return actions 
        
        explored[state] = nextNode.getPathCost()

        for successor in successors:
            if successor.getState() not in explored:
                frontier.push(successor)
    
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # TODO
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # TODO    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


class Node:
    """
    This class outlines the structure of a Node. 
    """
    
    def __init__(self, state : pacman.GameState, parentNode, actionToState : game.Actions, stepCost : int, pathCost : int): 
        
        self.state = state # the current position of an agent in the maze

        self.parentNode = parentNode # node preceding the current node

        self.actionToState = actionToState # action leading to the node's current state

        self.stepCost = stepCost # the cost of the step taken to end at the current state

        self.pathCost = pathCost # sum of costs of all steps taken to end at the current state

    def allSuccessors(self):
        """
        Gets all successor nodes that follow from node at current point. 

        Returns a list of new Nodes
        """
        # (successor, action, stepCost), where 'successor' is a
        #  successor to the current state, 'action' is the action
        #  required to get there, and 'stepCost' is the incremental
        #  cost of expanding to that successor
        successors = PositionSearchProblem.getSuccessors(self.state)
        nodes = []
        parentNode = Node(self.state, self.parentNode, self.actionToState, self.stepCost, self.pathCost)
        actions = [self.actionToState]

        for successor in successors:
            prevState = successor[0]
            action = successor[1]
            stepCost = successor[2]
            actions.append(action)

            newNode = Node(prevState, parentNode, action, stepCost, PositionSearchProblem.getCostOfActions(actions))

            nodes.append(newNode)

            parentNode = newNode

        return nodes
    
    def getState(self):
        """
        Returns the GameState associated with this node. 
        """
        return self.state
    
    def getAction(self):
        """
        Returns the action to the current state.
        """
        return self.actionToState

    def getPathCost(self):
        """
        Returns the integer representing the cost of the path to the current state of this node.
        """
        return self.pathCost