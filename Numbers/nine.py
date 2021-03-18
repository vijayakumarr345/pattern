# Shape of number 9 using fucntions
def for_9():
    """ *'s printed in the shape of number 9 """
    for row in range(9):
        for col in range(5):
            if row % 4 ==0 and col %4 !=0 or row %8 !=0 and col ==4 or col ==0 and row in (1,2,3,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_9():
    """ *'s printed in the shape of number 9 """
    row =0
    while row<9:
        col =0
        while col <5:
            if row % 4 ==0 and col %4 !=0 or row %8 !=0 and col ==4 or col ==0 and row in (1,2,3,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1
    

