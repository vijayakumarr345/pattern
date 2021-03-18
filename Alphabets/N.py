# Capital Alphabet N using Function
def for_N():
    """ *'s printed in the Shape of Capital N """
    for row in range(9):
        for col in range(9):
            if col %8 ==0 or row -col ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_N():
    """ *'s printed in the Shape of Capital N """
    row =0
    while row <9:
        col =0
        while col <9:
            if col %8 ==0 or row -col ==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

