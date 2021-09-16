class DFA:
   
    def __init__(self, S, Q, q0, F, d, c):# Self must be provided as a First parameter to the Instance method and constructor. If you don’t provide it, it will cause an error.
        self.S = S
        self.Q = Q
        self.q0 = q0
        #self.q = q0
        self.F = F
        self.d = d
        self.c = c