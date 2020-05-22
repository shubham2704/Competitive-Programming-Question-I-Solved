##Question##

Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs
from the others.
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program
that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Example:-
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

##Code##

def iq_test(n):
    n1 = list(map(int, n.split()))
    even = [int(x) for x in n1 if x%2==0]
    odd = [int(x) for x in n1 if x%2!=0]
    
    return n1.index(even[0])+1 if len(even)==1 else n1.index(odd[0])+1
n = "2 4 7 8 10"
iq_test(n)
