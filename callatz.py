#Eliza Cabrera, December 15th 2023
#callatz.py
#description

#variables
string = []
number = 0

#ask the user for a positive integer
start = int(input('Enter a positive integer: '))

if start == 1:
    string.append(1)
number = start + number


#callatz function
def callatz(n):
    #check if the integer is odd
    while n > 1:
        string.append(n)
    #check if integer is even
        if (n % 2) ==  0:
            n = n / 2
            
    #repeat checking
        elif n % 2 == 1:
            n = (3 * n) + 1

    string.append(1)
    
#check if long

def long(s):
    if len(string) > s:
        print('this sequence is LONG')
        
#perform the callatz function with original start
callatz(number)
print(string)
long(start)


#
for i in len(string):
    callatz(i)
    

    
        
