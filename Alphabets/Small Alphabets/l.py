# Small alphabet l using function
def for_l():
    """ *'s printed in the shape of l """
    for row in range(9):
        for col in range(5):
            if col ==2 or row ==8 and col >2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_l():
    """ *'s printed in the Shape of Small l """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==2 or row ==8 and col >2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

