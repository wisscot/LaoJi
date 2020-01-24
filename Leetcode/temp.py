def f(a, b):
    
    res = []
    loc = 0
    def f1(c):
        res.append(1)
        return loc
                
    print(f1(1))
    
f(1,2)