# Small alphabet i using function
def for_i():
    """ *'s printed in the Shape of small i """
    for row in range(9):
        for col in range(5):
            if col ==2 and row !=1 or row ==8 or row==3 and col ==1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_i():
    """ *'s printed in the Shape of Small i """
    row =0
    while row <9:
        col =0
        while col <5:
            if col ==2 and row !=1 or row ==8 or row==3 and col ==1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
    

