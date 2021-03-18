# Small alphabet b using Function
def for_b():
    """ *'s printed in the Shape of Small b """
    for row in range(9):
        for col in range(6):
            if col ==0 or row in (4,8) and col !=5 or row in (5,6,7) and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_b():
    """ *'s printed in the Shape of Small b """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row in (4,8) and col !=5 or row in (5,6,7) and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

