#2nd task
x=0
z=0
quantity=0
while x!="done":
    
    x=input("Please enter your number: ")
    if x.isdecimal():
      
        quantity=quantity+1
        z=int(x)+z
    if x.isdecimal()==False and x!="done":
        print('Please enter only numbers or string "done"')
print('Summary is',z)    
print("Quantity is",quantity)    
print('Arithmetic average is',z/quantity)