


while (True):
    
    operation = input("""
                      
          Welcome to the calculator
          If you want one of the followings operations
          select the correct number
          sum - 1
          res - 2
          mul - 3
          div - 4
          exit - 0
        """)
    
    if operation == "1":
        num1 = input(' Enter your first integer ');
        num2 = input(' Enter your second integer ');
        try:
            print('Answer = ', int(num1) + int(num2))
        except:
            print("""Your numbers are invalid
                  Run your application again if you want to""");

    elif operation == "2":
        num1 = input(' Enter your first integer ');
        num2 = input(' Enter your second integer ');
        try:
            print('Answer= ',int(num1) - int(num2));
        except:
            print("""Your numbers are invalid
                  Run your application again if you want to""");

    elif operation == "3":
        num1 = input(' Enter your first integer ');
        num2 = input(' Enter your second integer ');
        try:
            print('Answer= ',int(num1) * int(num2));
        except:
            print("""Your numbers are invalid
                  Run your application again if you want to""");
    elif operation == "4":
        num1 = input(' Enter your first integer ');
        num2 = input(' Enter your second integer ');
        try:
            if(int(num2) > 0):
                print('Answer= ',int(num1) / int(num2));
            else:
                print("The second number must not be 2");
                
        except:
            print("""Your numbers are invalid
                  Run your application again if you want to""");
    elif operation == "0":
    
        print("Bye bye")
        break;
    else:
        print("Your number is not in the options. Try again")
        break;