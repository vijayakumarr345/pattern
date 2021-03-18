# Capital Alphabet X using Function
def for_X():
    """ *'s printed in the Shape of Capital X """
    for row in range(9):
        for col in range(9):
            if row==col or col+row ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_X():
    """ *'s printed in the Shape of Capital X """
    row =0
    while row <9:
        col =0
        while col <9:
            if row==col or col+row ==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    
                 
                
