# Capital Alphabet L using Functions
def for_L():
    """ *'s printed in the Shape of Capital L """
    for row in range(9):
        for col in range(6):
            if col ==0 or row ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_L():
    """ *'s printed in the Shape of Capital L """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
