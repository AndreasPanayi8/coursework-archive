from collections import deque
#library just to implement pop(0) efficiently

class WorstCasePQA:
    """Worst Case Priority Queue with Attrition (PQA) by Sundar"""

    def __init__(self):
        self.C = deque()
        self.B = deque()
        self.D_f = deque()
        self.D_r = deque()
    
    def insert(self, x):
        if self.C and self.C[0] >= x:
            self.C = deque([x])
            self.B = deque()
            self.D_f = deque()
            self.D_r = deque()
        elif self.C and self.C[-1] >= x:
            self.B = deque(list(self.C)[1:])
            self.C = deque([self.C[0]])
            self.D_f = deque([x])
            self.D_r = deque()
        else:
            self.D_r.append(x)
        
        self._bias()
        self._bias()
    
    def delete_min(self):
        self._bias()
        if not self.C:
            raise IndexError("Cannot delete from empty priority queue")
        return self.C.popleft()
    
    def _bias(self):
        if self.D_r:
            if self.D_f and self.D_f[-1] >= self.D_r[0]:
                self.D_f.pop()
            else:
                self._pass(self.D_r, self.D_f)
        elif self.D_f and (not self.B or self.B[0] >= self.D_f[0]):
            self.C.extend(self.D_f)
            self.D_f = deque()
            self.B = deque()
        elif self.B:
            self._pass(self.B, self.C)
    
    def _pass(self, A, B):
        if A:
            # could also used B.append(A.pop(0)) but deque is more efficient this way
            B.append(A.popleft())