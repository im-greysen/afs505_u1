# this section uses functions and strings and the values in the function are actually
# first designated in line 12
def cheese_and_crackers(chese_count, boxes_of_crackers):
    print(f"You have {chese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


# prints the statement then uses the function above and assigns values below to variables in function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# this changes value of variables by defining new variables to be to be 10 and 50 respectively
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# function using above variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints the statement then uses the main function but with values from the addition inside the fn.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Uses above fn with addition to the variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
