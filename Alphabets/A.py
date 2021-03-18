# Capital alphabet A using function
def for_A():
    """ *'s printed in the Shape of Capital A"""
    for row in range(6):
        for col in range(12):
            if row+col ==6 or col -row ==6 or row ==3 and col in (3,4,5,6,7,8):
                print('*',end =' ')
            else:
                print(' ',end=' ')
        print()


def while_A():
    """ *'s printed in the Shape of Capital A """
    row = 0
    while row<6:
        col =0
        while col <12:
            if row+col ==6 or col -row ==6 or row ==3 and col in (3,4,5,6,7,8):
                print('*',end =' ')
            else:
                print(' ',end=' ')
            col +=1
        print()
        row += 1

            

