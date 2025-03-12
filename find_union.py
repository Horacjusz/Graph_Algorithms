class Node :
    def __init__(self,value) :
        self.parent = self
        self.rank = 0
        self.value = value
        
def findset(x) :
    if x.parent != x :
        x.parent = findset(x.parent)
    return x.parent

def union(x,y) :
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank :
        y.parent = x
    else :
        x.parent = y
        if x.rank == y.rank :
            y.rank += 1