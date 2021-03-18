# Capital Alphabet K using Function
def for_K():
    """ *'s printed in the Shape of Capital K """
    for row in range(9):
        for col in range(6):
            if col ==0 or row+col ==5 or row -col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()



def while_K():
    """ *'s printed in the Shape of Capital K """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==0 or row+col ==5 or row -col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
   
