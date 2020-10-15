class Cell():

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.isVisited = False
        self.top = True
        self.left = True
        self.bottom = True
        self.right = True
    
    def __repr__(self):
        return f"Cell({self.i}, {self.j})"
