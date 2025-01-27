"""
Here’s a list of all the topics we covered for Python arrays (lists):

1. **Basics of Python Lists**
- Creating a List
- Accessing Elements in a List
- Modifying a List
- Adding and Removing Elements
- List Length

2. **Slicing in Lists**

3. **List Comprehensions**

4. **Advanced List Operations**
- Sorting a List
- Combining Lists
- Nested Lists

5. **Iterating Over Lists**

6. **Advanced Python List Functions**
- `map()`
- `filter()`
- `zip()`

7. **Copying Lists**

8. **Multidimensional Arrays (2D Lists)**

These are the key concepts for working with lists (arrays) in Python!


"""


class arrayInPython:
    def basicsOfPythonLists():              
               

        #   Creating an empty list  
        emptyDeclaredList = []         
        print('emptyDeclaredList -> ', emptyDeclaredList)    


        #   Creating a List
        listWithvalues = [0,1,2,3,4]
        print('listWithvalues -> ', listWithvalues)   
  

        #   Accessing Elements in a List 
        print('value at index 0 -> ', listWithvalues[0])   
        print('value at index -3 -> ', listWithvalues[-3])    
        print('value at index 3 -> ', listWithvalues[3])  
        # will give error as IndexError: list index out of range
        # print('value at index 10 -> ', listWithvalues[10])   
        # print('value at index -10 -> ', listWithvalues[-10])   


        #   Modifying a List
        listWithvalues[1] = 100
        print('list after updating my values at index 1 -> ', listWithvalues)   
    
        #   Adding Elements
        listWithvalues.append(5) 
        print(' append(5)  -> ', listWithvalues)   
        
        listWithvalues.insert(1,1.5)  
        print(' insert(1,1.5) -> ', listWithvalues)     


        # Removing Elements 
        poppedValue = listWithvalues.pop() 
        print(' .pop() -> ', listWithvalues)            # will pop out the last element from array
        print(' poppedValue -> ', poppedValue)          # we can store the popped value


        poppedValue = listWithvalues.pop(3) 
        print(' .pop(3) -> ', listWithvalues)           # pop the value at given index 
        print(' poppedValue -> ', poppedValue)    

        listWithvalues.remove(3)                        # remove exact value from list
        print(' remove(3) -> ', listWithvalues)     
 

        #   List Length             
        print(' len -> ', len(listWithvalues))          # length of list

    
    def slicingInList():
        mylist = [0,1,2,3,4,5,6,7,8,9]
        #  arrayName [startIndex : endIndex : iterator ]
        print(' mylist  ->   ', mylist) 
        print('  mylist[:]  ->   ',  mylist[:]) 
        print('  mylist[:3]  ->   ',  mylist[:3]) 
        print('  mylist[::3]  ->   ',  mylist[::3])
        print('  mylist[::]  ->   ',  mylist[::])


    def listComprehensions():
        #creating count from 1 to 10
        countNumber =  [i for i in range(1,10)]
        print('countNumber -> ',countNumber)  
 

        # Create a list of squares from 1 to 5
        squares = [x**2 for x in range(1, 6)] 
        print('squares -> ',squares)  


        # Create a list of even numbers
        evens = [x for x in range(1, 11) if x % 2 == 0]
        print('evens -> ',evens)  

        
        odds = [x for x in range(1,10) if x%2 != 0]
        print('odds -> ',odds)
 

    def advancedListOperations():
        mylist = [3,4,5,2,1,0,6] 
        print('mylist   -> ', mylist)

        # .sort method updates the original array
        #   Sorting a List    .sort
        sortedList = mylist.copy()
        sortedList.sort()
        print('sortedList   -> ',sortedList) 
        
        #   reverse sorting a list .sort(reverse=True)
        reversedSortedList = mylist.copy()
        reversedSortedList.sort(reverse=True)
        print('reversedSortedList   -> ',reversedSortedList)


        # Sorted() & sorted(reverse=True) don't change any in the original array 
        
        print(' mylist   -> ', mylist) 
        print(' sorted   -> ',sorted(mylist))
        print('reverse sorted   -> ',sorted(mylist,reverse=True))



        



        #   Combining Lists



        #   Nested Lists



    def __init__(self) -> None:
        pass
        # constructor of the python 


        
 

obj = arrayInPython
obj.basicsOfPythonLists()
obj.slicingInList()
obj.listComprehensions()
obj.advancedListOperations()

