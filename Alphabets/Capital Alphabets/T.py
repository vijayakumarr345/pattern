# Capital Alphabet T using Function
def for_T():
    """ *'s printed in the Shape of Capital T """
    for row in range(9):
        for col in range(7):
            if row ==0 or col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_T():
    """ *'s printed in the Shape of Capital T """
    row =0
    while row <9:
        col =0
        while col <7:
            if row ==0 or col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
                

