# Capital Alphabet C using Function
def for_C():
    """ *'s printed in the Shape of Capital C """
    for row in range(9):
        for col in range(6):
            if col ==0 and row%8 !=0 or row %8 ==0 and col !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_C():
    """ *'s printed in the Shape of Capital C """
    row =0
    while row <9:
        col =0
        while col<6:
            if col ==0 and row%8 !=0 or row %8 ==0 and col !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row+=1

    
