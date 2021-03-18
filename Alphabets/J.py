# Capital Alphabet J using Function
def for_J():
    """ *'s printed in the Shape of Capital J """
    for row in range(9):
        for col in range(7):
            if row ==0 or col ==3 and row !=8 or row -col ==6:
                print('*',end =' ')
            else:
                print(' ',end=' ')
        print()

def while_J():
    """ *'s printed in the Shape of Capital J """
    row =0
    while row <9:
        col =0
        while col <7:
            if row ==0 or col ==3 and row !=8 or row -col ==6:
                print('*',end =' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

    
