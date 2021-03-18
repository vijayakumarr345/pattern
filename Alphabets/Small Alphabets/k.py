# Small alphabet k using function
def for_k():
    """ *'s printed in the shape  of k """
    for row in range(9):
        for col in range(9):
            if col ==0 or row+col ==5 and row >1 or row -col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_k():
    """ *'s printed in the Shape of Small k """
    row =0
    while row <9:
        col =0
        while col <9:
            if col ==0 or row+col ==5 and row >1 or row -col ==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

