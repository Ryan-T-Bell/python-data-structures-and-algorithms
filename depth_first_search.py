
# Implement iterative deepening search
class DepthFirstSearch:

    def __init__(self, node):
        self.iterative_deepening_search(node)
    
    
    def iterative_deepening_search(self, node):
        depth_limit = 0
        
        while True:
            result = self.depth_limited_search(node, depth_limit)
            
            if self.is_cutoff(result):
                return result
            else:
                depth_limit = depth_limit + 1
                
    
    def depth_limited_search(self, node, depth_limit):
        
        if self.goal_test(node):
            return node
        
        elif depth_limit == 0:
            return "cutoff"
        
        else:
            cutoff_occured = False
            
            for child in expand_node(node):
                result = self.depth_limited_search(child, depth_limit - 1)
                
                if self.is_cutoff(result):
                    cutoff_occured = True
                
                elif self.is_failure(result):
                    return result
                
            if cutoff_occured:
                return "cutoff"
            else:
                return "failure"
    
    
    def is_cutoff(result):
        if result == "cutoff":
            return True
        else:
            return False
    
    
    def is_failure(result):
        if result == "failure":
            return True
        else:
            return False
    
    
    def goal_test(node):
        # TODO: Implement goal test on node
        return True