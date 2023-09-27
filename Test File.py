a = int(input()) 
b = int(input()) 
c = int(input()) 
d = int(input()) ** 2 

diag1 = a ** 2 + b ** 2 
diag2 = a ** 2 + c ** 2 
diag3 = b ** 2 + c ** 2 

if diag1 <= d or diag2 <= d or diag3 <= d: 
    print("Yes") 
else: 
    print("No") 