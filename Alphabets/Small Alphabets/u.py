# Small alphabet u using function
def for_u():
    """ *'s printed in the shape of small u """
    for row in range(5):
        for col in range(5):
            if col %4 ==0 and row !=4 or row ==4 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_u():
    """ *'s printed in the Shape of Small u """
    row =0
    while row <5:
        col =0
        while col <5:
            if col %4 ==0 and row !=4 or row ==4 and col%4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

