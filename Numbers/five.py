# Shape of number 5 using fucntions
def for_5():
    """ *'s printed in the shape of number 5 """
    for row in range(9):
        for col in range(5):
            if row ==0 or col ==0 and row <5 or row in (2,8) and col in (2,3) or row in (3,4,5,6,7) and col ==4 or row ==7 and col ==0 or col ==1 and row in (3,8):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_5():
    """ *'s printed in the shape of number 5 """
    row =0
    while row<9:
        col =0
        while col <5:
            if row ==0 or col ==0 and row <5 or row in (2,8) and col in (2,3) or row in (3,4,5,6,7) and col ==4 or row ==7 and col ==0 or col ==1 and row in (3,8):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row += 1
    

