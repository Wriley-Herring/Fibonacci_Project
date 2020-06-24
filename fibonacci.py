"""
File: countfib.py
Prints the the number of calls of a recursive Fibonacci
function with problem sizes that double.

Modified by: Wriley Herring

Added Memoization functionality to reduce recursive calls

Recursive version was significantly slower and my computer has issues running it for anything larger than n = 32

Iterative was the fastest but recursive with memoization funtionality was just a tad slower
"""

from counter import Counter
from datetime import datetime 


def fibA(n, counter):
    """Count the number of calls of the Fibonacci
    function."""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fibA(n - 1, counter) + fibA(n - 2, counter)

def fibC(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


fibDic = {}
#Modified Recursive Fib Function to add memoization functionality
def fibB(n, counter, dictionary):
    
    
    """Count the number of calls of the Fibonacci
    function."""
    
    #check if fibB(n) has already been found
    if n in dictionary:
        return dictionary[n]
    
    #check if n is less than three and return 1 if True
    elif n < 3:
        dictionary[n] = 1
        return 1
    
    else:
        
        #check if n-1 and n-2 have already been found 
        if all (k in dictionary for k in ((n-1),(n-2))):
            output = dictionary[n-1] + dictionary[n-2]
            dictionary[n] = output
            return output
        
        #otherwise perform recursive operation
        else:
            counter.increment()
            output = fibB(n - 1, counter, dictionary) + fibB(n - 2, counter, dictionary)
            dictionary[n] = output
            return output

#set calculation objective
problemSize = 2
print('Memoization Fib:')
print("%12s%15s%75s%30s" % ("Problem Size", "Calls", "Fibonacci", "Time"))
for count in range(8):
    counter = Counter()

    #start timer
    startTime = datetime.now()
    
    # The start of the algorithm
    fib = fibB(problemSize, counter, fibDic)
    # The end of the algorithm
    
    #stop timer
    time = str(datetime.now() - startTime)
    
    #print outputs
    print("%12d%15s%75s%30s" % (problemSize, counter, fib, time))
    
    #increase size of problem
    problemSize *= 2


#set calculation objective
problemSize = 2
print('\n')
print('Recursive Fib:')
print("%12s%15s%75s%30s" % ("Problem Size", "Calls", "Fibonacci", "Time"))
for count in range(5):
    counter = Counter()

    #start timer
    startTime = datetime.now()
    
    # The start of the algorithm
    fib = fibA(problemSize, counter)
    # The end of the algorithm
    
    #stop timer
    time = str(datetime.now() - startTime)
    
    #print outputs
    print("%12d%15s%75s%30s" % (problemSize, counter, fib, time))
    
    #increase size of problem
    problemSize *= 2

#set calculation objective
problemSize = 2
print('\n')
print('Iterative Fib:')
print("%12s%75s%30s" % ("Problem Size", "Fibonacci", "Time"))
for count in range(8):
    counter = Counter()

    #start timer
    startTime = datetime.now()
    
    # The start of the algorithm
    fib = fibC(problemSize)
    # The end of the algorithm
    
    #stop timer
    time = str(datetime.now() - startTime)
    
    #print outputs
    print("%12d%75s%30s" % (problemSize, fib, time))
    
    #increase size of problem
    problemSize *= 2