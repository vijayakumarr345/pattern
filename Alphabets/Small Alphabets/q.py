# Small alphabet q using function
def for_q():
    """ *'s printed in the shape of q """
    for row in range(9):
        for col in range(6):
            if col ==4 or row in (0,4)  and col %5 !=0 or col ==0 and row in (1,2,3) or row ==7 and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_q():
    """ *'s printed in the Shape of Small q """
    row =0
    while row <9:
        col =0
        while col <6:
            if col ==4 or row in (0,4)  and col %5 !=0 or col ==0 and row in (1,2,3) or row ==7 and col ==5:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

