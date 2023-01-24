def exo1():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("ThreeFive")
            continue
        if (i % 3 == 0):
            print("Three")
            continue
        if (i % 5 == 0):
            print("Five")
            continue
        print(i)

exo1()