# import joblib

# salary = joblib.load("salary-predictor.pk1")

# x = float(input("Enter the number of years: "))

# salary2 = salary.predict([[x]])  

# print(salary2[0])


# [0] as in index 0, it helps to not get value in array form iykyk


# float instead of int b/c we'll provide float values also

import joblib
salary = joblib.load("salary-predictor.pk1")

print("\t\t\tWelcome to the AI predictor")
print("\t\t\t...........................")
print()          #To leave some space
 
    
while True:
    print("press 1: Analyse marks")
    print("press 2: predict salary")
    print("press 3: predict weather")
    print("press 4: To exit")

    print("Enter your choice: ", end = '') #python bydefault uses end = '/n' which breaks to  next line, we r simply removing it.

    ch = int(input())

    print(ch)

    if ch == 1:
        print("Enter year Exp : ", end ='')
        x = input()
        X = float(x)
        print("predicted salary : ", salary.predict([[X]])[0])
        
    elif ch == 2:
        print("predicting salary.........")
    
    elif ch == 3:
        print("predicting weather.........")
        
    elif ch == 4:
        exit()     #this is use to exit the program
        
    else:
        print("Wrong choice")

    
#(salary.predict([[X]])) without print, it does'nt print anything like it does in jupyter b/c jupyter is a live interpreter like repl but our text file is not
 