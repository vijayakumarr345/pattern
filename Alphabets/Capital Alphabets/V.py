# Capital Alphabet V using Function
def for_V():
    """ *'s printed in the Shape of Capital V """
    for row in range(9):
        for col in range(17):
            if row -col ==0 or row +col ==16: 
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_V():
    """ *'s printed in the Shape of Capital V """
    row =0
    while row <9:
        col =0
        while col <17:
            if row -col ==0 or row +col ==16: 
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

