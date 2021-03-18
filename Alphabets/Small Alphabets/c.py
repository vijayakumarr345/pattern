# Small alphabet c using Function
def for_c():
    """ *'s printed in the Shape of Small c """
    for row in range(5):
        for col in range(5):
            if row %4 !=0 and col ==0 or row %4 ==0 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end =' ')
        print()


def while_c():
    """ *'s printed in the Shape of Small c """
    row =0
    while row <5:
        col =0
        while col <5:
            if row %4 !=0 and col ==0 or row %4 ==0 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end =' ')
            col+=1
        print()
        row +=1
    

