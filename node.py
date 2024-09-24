# node.py
# ---------
# Represents a node object containing the state, parent node, action
# leading to the state, step cost, and the path cost to reach that
# specific node.

class Node:
    """
    This class outlines the structure of a Node. 

    state: the current position of an agent in the maze

    parentNode: node preceding the current node

    actionToState: action leading to the node's current state

    stepCost: the cost of the step taken to end at the current state

    pathCost: sum of costs of all steps taken to end at the current state
    """

    def __init__(self, state , parentNode, actionToState, stepCost, pathCost):
        
        self.state = state

        self.parentNode = parentNode

        self.actionToState = actionToState

        self.stepCost = stepCost

        self.pathCost = pathCost
        pass

    def allSuccessors(self):
        """
        Gets all successor nodes that follow from the given node at
        a certain point. 
        """
        return
    
    def getState(self):
        """
        Returns the state associated with this node. 
        """
        return self.state


# use the built in functions -> likely directly correlate to what's already needed
# what's the best data structure for each?