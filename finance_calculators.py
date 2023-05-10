import math

#message string displays user a message to prompt them to type 'investment' or 'bond'
message = """investment - to calculate the amount of interest you will earn on your investment
bond       - to calculate the amount you will have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: \n"""

#Users input is then transformed into lowercase
user_input = input(message).lower()

#if,elif,else statement is used to provide conditions. If user enters 'investment' the block of code for investment is run.
if user_input == 'investment' :
    deposit = float(input("How much are you depositing\n"))
    rate1 = float(input("What is the interest rate as a percentage\n"))
    years = int(input("How many years do plan on investing?\n"))
    interest = (input("Would you like 'simple' or 'compound' interest?\n").lower())
    if interest == "simple":
        print("Your answer is :" , deposit*(1+(rate1/100)*years))
    elif interest == "compound" :
        print("Your amount at the end of your investment peroid :", deposit*math.pow(1 +(rate1/100),years))

#otherwise 'elif' meaning else if the user enters bond the condition is met and the block code for bond is run
elif user_input == 'bond' :
    value = float(input("What is the present value of the house ?\n"))
    rate2 = float(input("What is the interest rate?\n"))
    months = int(input("How many months do plan to repay the bond?\n"))
    monthly_rate = (rate2 / 100) / 12  # Calculates the monthly interest rate
    repayment = (monthly_rate * value) / (1 - (1 + monthly_rate) ** (-months))
    print(f"Your monthy repayment is: {repayment}")

#Lastly 'else' if neither condition are met, code for 'else'statment is run as investment nor bond was entered.
else:
    print("Invalid input. Options are investment or bond")
