# Shape of number 1
def for_1():
    """ *'s printed in the shape of number 1 """
    for row in range(8):
        for col in range(7):
            if col ==3 or row ==7 or row ==1 and col ==2 or row ==2 and col ==1:
                print('*',end =' ')
            else:
                print(' ',end =' ')
        print()

def while_1():
    """ *'s printed in the shape of number 1 """
    row =0
    while row<8:
        col =0
        while col<7:
            if col ==3 or row ==7 or row ==1 and col ==2 or row ==2 and col ==1:
                print('*',end =' ')
            else:
                print(' ',end =' ')
            col+=1
        print()
        row += 1
    

