def calculator():
    print("""
	
	                   calculator
	
	""")
    while True:
        try:
            num1 = float(input("Please enter first number:\n"))
            num2 = float(input("please enter second number:\n"))
            break
        except ValueError:
            print("Please type a number only.")
    print('\n\n')

    operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
× for multiplication
÷ for division 
		    ''')

    print('\n\n')

    if_operation = """
	
                     ====================    
                    ||                  ||
                             {}        
                    ||                  ||
                     ====================
	
	
	
	"""

    if operation == '+':
        print(if_operation.format(num1+num2))
    elif operation == '-':
        print(if_operation.format(num1-num2))
    elif operation == '×':
        print(if_operation.format(num1*num2))
    elif operation == '÷':
        print(if_operation.format(num1/num2))
    else:
        print("You have not typed a valid operator, please run the program again.")

    print('\n\n')

    program_again = input("Do you want to calculate again? (yes or no)\n")

    if program_again.upper() == 'NO':
        print('\nThanks for use. see you later')
    elif program_again.upper() == 'YES':
        calculator()


calculator()
