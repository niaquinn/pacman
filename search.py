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

# from searchAgents import PositionSearchProblem
import util
from game import Agent

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
    """
    frontier = util.Stack()

    startNode = Node(problem.getStartState(), None, [], 0, 0)
    frontier.push(startNode)
    explored = {}

    while not frontier.isEmpty():
        currentNode = frontier.pop()
        state = currentNode.getState()
        actions = currentNode.getActions()
        pathCost = problem.getCostOfActions(actions)

        if problem.isGoalState(state):
            print(f"the goal state is: {state}")
            return actions

        explored[state] = pathCost
        successors = problem.getSuccessors(state)

        for successorState, successorAction, successorCost in successors:
            if successorState not in explored:
                successorActions = actions + [successorAction]
                successorPathCost = problem.getCostOfActions(successorActions)
                nextNode = Node(successorState, currentNode, successorActions, successorCost, successorPathCost)
                frontier.push(nextNode)
    return []                    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
        
    frontier = util.Queue()
    startNode = Node(problem.getStartState(), None, [], 0, 0)
    frontier.push(startNode)
    explored = {}

    while not frontier.isEmpty():
        currentNode = frontier.pop()
        state = currentNode.getState()
        actions = currentNode.getActions()
        pathCost = problem.getCostOfActions(actions)

        if problem.isGoalState(state):
            print(f"the goal state is: {state}")
            return actions

        explored[state] = pathCost
        successors = problem.getSuccessors(state)

        for successorState, successorAction, successorCost in successors:
            if successorState not in explored:
                successorActions = actions + [successorAction]
                successorPathCost = problem.getCostOfActions(successorActions)
                nextNode = Node(successorState, currentNode, successorActions, successorCost, successorPathCost)
                frontier.push(nextNode)
    return []  

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

#### THE NODE CLASS
class Node:
    """
    This class outlines the structure of a Node. 
    """
    
    def __init__(self, state, parentNode, actions, stepCost : int, pathCost : int): 
        
        self.state = state # the current position of an agent in the maze

        self.parentNode = parentNode # node preceding the current node

        self.actions = actions # list of actions leading to the node's current state

        self.stepCost = stepCost # the cost of the step taken to end at the current state

        self.pathCost = pathCost # sum of costs of all steps taken to end at the current state

    def getState(self):
        """
        Returns the GameState associated with this node. 
        """
        return self.state
    
    def getActions(self):
        """
        Returns the action to the current state.
        """
        return self.actions
    
    def getStepCost(self):
        """
        Returns the step cost of the action leading to the current state of the Node.
        """
        return self.stepCost

    def getPathCost(self):
        """
        Returns the integer representing the cost of the path to the current state of this node.
        """
        return self.pathCost
    
    def toString(self):
        """
        Formats the field of this Node object such that the fields are readily readable for debugging purposes.

        ex= Node(currentState, parentNode, actions, stepCost, pathCost)
        """
        return f"Node: currentState = {self.state}, parentNode = {self.parentNode}, actions = {self.actions}, stepCost = {self.stepCost}, pathCost = {self.pathCost}"
