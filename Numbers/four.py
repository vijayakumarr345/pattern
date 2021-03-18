# Shape of number 4 using fucntions
def for_4():
    """ *'s printed in the shape of number 4 """
    for row in range(9):
        for col in range(7):
            if row+col ==6 or row ==6 or col ==5 and row>3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_4():
    """ *'s printed in the shape of number 4 """
    row =0
    while row<9:
        col =0
        while col <7:
            if row+col ==6 or row ==6 or col ==5 and row>3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

