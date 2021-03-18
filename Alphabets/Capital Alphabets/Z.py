# Capital Alphabet Z using Function
def for_Z():
    """ *'s printed in the Shape of Capital Z """
    for row in range(9):
        for col in range(9):
            if row%8 ==0 or row+col ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_Z():
    """ *'s printed in the Shape of Capital Z """
    row =0
    while row <9:
        col =0
        while col <9:
            if row%8 ==0 or row+col ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
  
