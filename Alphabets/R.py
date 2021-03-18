# Capital Alphabet R using Function
def for_R():
    """ *'s printed in the Shape of Capital R """
    for row in range(9):
        for col in range(6):
            if col ==0 or row in (0,4) and col != 5 or row in (1,2,3) and col ==5 or row - col ==4:
                print('*',end =' ')
            else:
                print(' ',end=' ')
        print()

def while_R():
    """ *'s printed in the Shape of Capital R """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row in (0,4) and col != 5 or row in (1,2,3) and col ==5 or row - col ==4:
                print('*',end =' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

