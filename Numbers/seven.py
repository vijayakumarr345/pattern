# shape of number 7 using functions
def for_7():
    """ *'s printed in the shape of number 7 """
    for row in range(9):
        for col in range(7):
            if row ==0 and col<5 or col ==4 or row ==4 and col in (2,3,5,6):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_7():
    """ *'s printed in the shape of number 7 """
    row =0
    while row<9:
        col =0
        while col <7:
            if row ==0 and col<5 or col ==4 or row ==4 and col in (2,3,5,6):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

    
