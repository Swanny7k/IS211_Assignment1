## Here I made an argument for the set of # we were testing called numbers. " numbers is == [1,2,3 etc etc] that was given to test
## Using a for loop we ran through the list we would pass as numbers
## We made an empty variable to keep count labeled "x"
## We want to see if our list of numbers would be divisible by our set arg2 called divide. Which is locked in a 2
## If the number was divisible by 2 it would count =1 in x
def listDivide(numbers, divide=2):
    x = 0
    for num in numbers:
        if num%divide == 0 :
            x = x+1
    return x
print (listDivide([1, 2, 4, 5, 6, ]))
#TESTING THE FOR LOOP AND COUNTER and it printed 3 for the 3 numbers that are divisible by arg2 which is divide = 2


#class ListDivideException:
def testListDivide():
    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30,54,63,98,100],divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5],divide=1) ==5
if __name__ == "__main__":
    testListDivide()

##If any number in the list was not divisible by 2 or  == to the integer that was set we would of gotten an error. If
##I were to chnage any number in the listdivide testing portion an error would of been presented

##I hope this is correct I am still new to python and not that familiar with certain processes