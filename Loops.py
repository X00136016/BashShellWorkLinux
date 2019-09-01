#For Loop
def loopfunc():

    a = ["Walt","Gus","Jesse"]
    for element in a:
        print(element)

def nextfloop():

    b = [5,9,3]
    #Total begins at 0
    total = 0
    #the Figures in b
    for math in b:
        #The new total is the sum to the old total + maths in b.
        total = total + math
        print(total)


def aloopfunc():
    totaltwo = 0
    for i in range(1, 5):
        #The new value of totaltwo is the sum of the old value of totaltwo
        totaltwo += i 
        print(totaltwo)

def bloopfunc():
        total=1
        for i in range(5):
                total = total + i
                print(total)

def nestedLoop():

        A = ["Walter","Hank","Gus"]
        B = ["White","Schrader","Fring"]

        for i in A:

                for j in B:

                        print(i + "" + j)
                        print("-----")


def numnestedLoop():

        a = [1,1]
        b = [24,55,2]

#defining a variable.
        total = 0
        total2 = 0
        
        #Nested loop I am going to increment by beginning with a for loop
        for i in a:
                total = total + i
        
        print("The answer is : ",total)

        for j in b:
  
                #The new sum of total is equal to the old sum of total plus i (The elements of variable a)
                total2 = total2 + j

        
        print("The answer is : ",total2)
                
def mulnestedLoop():        
#Creating three varaibles to do a nested loop times 3               
        x = [55,100,167]
        y = [58,70]
        z = [1565, 4444,6767,9999]

#for loop 
        total = 0
        total1 = 0
        total2 = 0

        #Nested loop number 1
        for i in x:
                total = total + i
        
        print("The answer is  :",total)
        print("--------------")


        #Nested loop number 2
        for j in y:
                total1 = total1 + j
        
        print("The answer is  :",total1)
        print("--------------")


        #Nested loop number 3
        for k in z:
                total2 = total2 + k
        
        print("The answer is  :",total2)
        print("--------------")


def wloop():

        print("Hello, in w loop.")



loopfunc()
nextfloop()
aloopfunc()
bloopfunc()
nestedLoop()
numnestedLoop()
mulnestedLoop()
wloop()