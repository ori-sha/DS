import unittest

def my_function():
  print("Hello from a function")

my_function()

#@Pre Array[i] is a number, for 1<=i<=n
#@Post Max value in array is printed to screen
#@Test : Find_Max(A) -> 2
def Find_Max(Array) :
    n = len(Array)
    max = Array[0]
    for x in range(n) :
        if Array[x] > max:
            max = Array[x]
    print("Max number in Array: " , max)


A = [0,1,2,3,4,5,6,7,9]
#Testing - Expected : "Max number in Array:  2"
Find_Max(A)
#@Pre Array[i] is a number, for 1<=i<=n
#@Post Max value in array is printed to screen
#@Test : Find_Max(A) -> 2
def Find_SeCond_Max(Array) :
    n = len(Array)
    max = Array[0]
    index = 0
    for x in range(n):
        if Array[x] > max:
            max = Array[x]
            index = x
    del(Array[index])
    if len(Array) == 0 :
        print("Only one Max value: ",max)
        return
    SecondMax = Array[0]
    for x in range(n-1):
        if Array[x] > SecondMax :
            SecondMax = Array[x]
    print("Max Value is: ",max, ", Second Max value: ", SecondMax)

Find_SeCond_Max(A)

#given a sorted array A of n integers and an integer x, determines whether or not there exist two elements in A whose sum is exactly x
#@Pre Array[i] is a number, for 1<=i<=n
#@Test : Two_Sum([0,1,2,3,4,5,6,7,9],11) -> 4  +  7 = 11
def Two_Sum(Array,Sum) :
    p = 0
    q = len(Array)-1
    while p < q :
        if Array[p] + Array[q] == Sum :
            print("Found Two Sum : ",Array[p]," + ",Array[q],"=",Sum)
            return
        elif Array[p] + Array[q] < Sum :
            p = p + 1
        else:
            q = q -1
    print("No Two Sum")

Two_Sum(A,11)




class TestStringMethods(unittest.TestCase):

    def test_Find_Max(self):
        self.assertEqual(Find_Max(A),2)

    if __name__ == '__main__':
            unittest.main()