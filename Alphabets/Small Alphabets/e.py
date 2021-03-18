# Small alphabet e using Function
def for_e():
    """ *'s printed in the Shape of small e """
    for row in range(5):
        for col in range(5):
            if col ==0 and row %4 !=0 or row %4 ==0 and col %4 !=0 or row ==1 or row ==3 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end =' ')
        print()

def while_e():
    """ *'s printed in the Shape of Small e """
    row =0
    while row <5:
        col =0
        while col <5:
            if col ==0 and row %4 !=0 or row %4 ==0 and col %4 !=0 or row ==1 or row ==3 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end =' ')
            col+=1
        print()
        row +=1

