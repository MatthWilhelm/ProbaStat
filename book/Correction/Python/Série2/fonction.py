def f1(x):
    X = [0,1,2,3,4,5,6,7,8,9,10]
    if not (x in X):
        raise("La fonction f1 est définie sur l'ensemble des entiers compris entre 0 et 10.")
    else:
        if x in [0,1,2,3]:
            return 0.25
        else:
            return 0.
        
def f2(x):
    X = [0,1,2,3,4,5,6,7,8,9,10]
    if not (x in X):
        raise("La fonction f2 est définie sur l'ensemble des entiers compris entre 0 et 10.")
    else:
        if x in [0,1,2,3]:
            return 0.15
        else:
            return 0.
        
def f3(x):
    X = [0,1,2,3,4,5,6,7,8,9,10]
    if not (x in X):
        raise("La fonction f3 est définie sur l'ensemble des entiers compris entre 0 et 10.")
    else:
        if x in [0,5]:
            return 0.03
        elif x in [1,4]:
            return 0.16
        elif x in [2,3]:
            return 0.31
        else:
            return 0.

def f4(x):
    X = [0,1,2,3,4,5,6,7,8,9,10]
    if not (x in X):
        raise("La fonction f4 est définie sur l'ensemble des entiers compris entre 0 et 10.")
    else:
        if x == 0:
            return 0.3
        elif x == 1:
            return 0.21
        elif x == 2:
            return 0.15
        elif x == 3:
            return 0.1
        elif x == 4:
            return 0.07
        elif x == 5:
            return 0.05
        elif x == 6:
            return 0.04
        elif x == 7:
            return 0.02
        elif x == 8:
            return 0.02
        elif x == 9:
            return -0.01
        elif x == 10:
            return 0.03