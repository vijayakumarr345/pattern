# Capitla Alphabet P using Fucntion
def for_P():
    """ *'s printed in the Shape of Capital P """
    for row in range(9):
        for col in range(6):
            if col ==0 or row in (0,4) and col !=5 or row in(1,2,3) and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_P():
    """ *'s prined in the Shape of Capital P """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row in (0,4) and col !=5 or row in(1,2,3) and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

