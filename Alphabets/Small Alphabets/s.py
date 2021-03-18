# Small alphabet s using function
def for_s():
    """ *'s printed in the shape of small s """
    for row in range(5):
        for col in range(5):
            if row%2 ==0 and col %4 !=0 or row ==1 and col ==0 or row ==3 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


def while_s():
    """ *'s printed in the Shape of Small s """
    row =0
    while row <5:
        col =0
        while col <5:
            if row%2 ==0 and col %4 !=0 or row ==1 and col ==0 or row ==3 and col ==4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            col+=1
        print()
        row +=1

