# Shape of number 3 using fucntions
def for_3():
    """ *'s printed in the shape of number 3 """
    for row in range(9):
        for col in range(5):
            if row % 4 ==0 and col!=4 or col ==4 and row %4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_3():
    """ *'s printed in the shape of number 3 """
    row =0
    while row<9:
        col =0
        while col <5:
            if row % 4 ==0 and col!=4 or col ==4 and row %4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1

