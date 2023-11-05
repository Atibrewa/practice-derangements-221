import random
import time
import random

D = [] # List of all derangements!

def GenDerangements(initialSet, curPerm = []):
    """
    Backtracking Algorithm to find all derangements of a given set!
    """
    # Edge Case with length 0 or 1
    if len(initialSet) == 0 or len(initialSet) == 0 :
        return
    
    if len(curPerm) == len(initialSet):
        # Adding valid permutations/derangements to the collection of all derangements
        if curPerm not in D:
            D.append(list(curPerm))
    else:
        for elem in initialSet:
            #print ("out", curPerm)
            if checkNoOfOccurences(initialSet, curPerm, elem):
                curPerm.append(elem)
                a = indices(initialSet, elem)
                b = indices(curPerm, elem)
                if CompareLists(a, b):
                    GenDerangements(initialSet, curPerm)
                curPerm.remove(elem)

def indices(L, s):
    """
    Returns a list of the indices at which the element s occurs in the list L
    """
    indList = [i for i, x in enumerate(L) if x == s]
    return indList

def checkNoOfOccurences(L, C, s):
    """
    Returns true if the element s occurs less times in the list C than in list L
    """
    Initial = indices(L, s)
    Current = indices(C, s)
    if len(Current) < len(Initial):
        return True
    return False

def CompareLists(p, q):
    """
    Checks if any element of p is in q
    """
    for elem in p:
        if elem in q:
            return False
    return True

# Test initialSet!
Test1 = [7, 2, 7, 9]

# Generating Large, Random Lists!

def generateRandomList(length, r):
    """
    length: length of list
    range: max possible value to be added to list
    """
    return random.choices(list(range(0 , r+1)), weights = [1] * (r+1), k = length)


# Running algorithm on test list!
starttime1 = time.time()
GenDerangements(Test1)
endtime1 = time.time()
print ("Number of Derangements of ", Test1, ": ", len(D))
print('length', len(Test1), 'time =' , endtime1 - starttime1)
print (D)


print("---------")

# Running algorithm on the generated List
D = []
RandomList = generateRandomList(4, 2)
starttime2 = time.time()
GenDerangements(RandomList)
endtime2 = time.time()
print(RandomList)
print ("Number of Derangements of ", RandomList, ": ", len(D))
print('length', len(RandomList), 'time =' , endtime2 - starttime2)
print ("Number of Derangements of ", Test1, ": ", len(D))
print (D)

print("---------")
D = []
RandomList = generateRandomList(5, 20)
starttime2 = time.time()
GenDerangements(RandomList)
endtime2 = time.time()
print(RandomList)
print ("Number of Derangements of ", RandomList, ": ", len(D))
print('length', len(RandomList), 'time =' , endtime2 - starttime2)
print ("Number of Derangements of ", Test1, ": ", len(D))
#print (D)

print("---------")
D = []
RandomList = generateRandomList(6, 20)
starttime2 = time.time()
GenDerangements(RandomList)
endtime2 = time.time()
print(RandomList)
print ("Number of Derangements of ", RandomList, ": ", len(D))
print('length', len(RandomList), 'time =' , endtime2 - starttime2)
print ("Number of Derangements of ", Test1, ": ", len(D))
#print (D)

print("---------")
D = []
RandomList = generateRandomList(7, 20)
starttime2 = time.time()
GenDerangements(RandomList)
endtime2 = time.time()
print(RandomList)
print ("Number of Derangements of ", RandomList, ": ", len(D))
print('length', len(RandomList), 'time =' , endtime2 - starttime2)
print ("Number of Derangements of ", Test1, ": ", len(D))
#print (D)

print("---------")
D = []
RandomList = generateRandomList(8, 20)
starttime2 = time.time()
GenDerangements(RandomList)
endtime2 = time.time()
print(RandomList)
print ("Number of Derangements of ", RandomList, ": ", len(D))
print('length', len(RandomList), 'time =' , endtime2 - starttime2)
print ("Number of Derangements of ", Test1, ": ", len(D))
#print (D)

