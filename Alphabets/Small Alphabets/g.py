# Small alphabet g using function
def for_g():
    """ *'s printed in the Shape of small g """
    for row in range(9):
        for col in range(5):
            if col ==4 and row%8!=0 or row%4 ==0 and col%4 !=0 or col ==0 and row in (1,2,3,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_g():
    """ *'s printed in the Shape of Small a """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==4 and row%8!=0 or row%4 ==0 and col%4 !=0 or col ==0 and row in (1,2,3,7):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

