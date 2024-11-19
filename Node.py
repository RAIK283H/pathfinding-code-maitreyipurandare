class Node:
    def __init__(self, index, priority):
        self.index = index
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    

    def __eq__(self, other):
        return self.index == other.index and self.priority == other.priority
    
    def __repr__(self):
        return f"Node({self.node_id}, {self.priority})"
    
    

      