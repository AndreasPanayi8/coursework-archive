class AmortizedPQA:
    """Amortized Priority Queue with Attrition (PQA) by Sundar"""
    
    def __init__(self):
        self.C = []
        self.D = []
    
    def insert(self, x):
        if self.D and self.D[0] >= x:
            self.D = [x]
        else:
            self.D.append(x)
    
    def delete_min(self):
        if self.D and self.C and self.C[0] >= self.D[0]:
            self.C = []
        
        if not self.C:
            if not self.D:
                raise IndexError("Cannot delete from empty priority queue")
            
            # Backward cleanup: scan D in reverse, delete each item with smaller or equal successor
            cleaned = []
            min_seen = float('inf')
            for i in range(len(self.D) - 1, -1, -1):
                x = self.D[i]
                if x < min_seen:
                    cleaned.append(x)
                    min_seen = x
            cleaned.reverse()
            
            self.C = cleaned
            self.D = []
        
        return self.C.pop(0)