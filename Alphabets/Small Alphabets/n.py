# Small alphabet n using function
def for_n():
    """ *'s printed in the shape of n """
    for row in range(5):
        for col in range(5):
            if row !=0 and col %4 ==0 or row ==0 and col %4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def while_n():
    """ *'s printed in the Shape of Small n """
    row =0
    while row <5:
        col =0
        while col <5:
            if row !=0 and col %4 ==0 or row ==0 and col %4 !=0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1
 
