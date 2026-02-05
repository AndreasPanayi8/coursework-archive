class WorstCasePQA:
    """Worst Case Priority Queue with Attrition (PQA) by Sundar"""

    def __init__(self):
        self.C = []
        self.B = []
        self.D_f = []
        self.D_r = []
    
    def insert(self, x):
        if self.C and self.C[0] >= x:
            self.C = [x]
            self.B = []
            self.D_f = []
            self.D_r = []
        elif self.C and self.C[-1] >= x:
            self.B = self.C[1:]
            self.C = [self.C[0]]
            self.D_f = [x]
            self.D_r = []
        else:
            self.D_r.append(x)
        
        self._bias()
        self._bias()
    
    def delete_min(self):
        self._bias()
        if not self.C:
            raise IndexError("Cannot delete from empty priority queue")
        return self.C.pop(0)
    
    def _bias(self):
        if self.D_r:
            if self.D_f and self.D_f[-1] >= self.D_r[0]:
                self.D_f.pop()
            else:
                self._pass(self.D_r, self.D_f)
        elif self.D_f and (not self.B or self.B[0] >= self.D_f[0]):
            self.C.extend(self.D_f)
            self.D_f = []
            self.B = []
        elif self.B:
            self._pass(self.B, self.C)
    
    def _pass(self, A, B):
        if A:
            B.append(A.pop(0))