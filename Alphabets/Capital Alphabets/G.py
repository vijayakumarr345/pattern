# Capitla Alphabet G using Function
def for_G():
    """ *'s printed in the Shape of Capital G """
    for row in range(9):
        for col in range(6):
            if col ==0 and row%8 !=0 or row %8 ==0 and col %5 !=0 or col ==5 and row in (1,2,6,7) or row ==6 and col>2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_G():
    """ *'s printed in the Shape of Capital G """
    row =0
    while row <9:
        col =0
        while col <6:
             if col ==0 and row%8 !=0 or row %8 ==0 and col %5 !=0 or col ==5 and row in (1,2,6,7) or row ==6 and col>2:
                print('*',end=' ')
             else:
                print(' ',end=' ')
             col +=1
        print()
        row +=1

        
            
