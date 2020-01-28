# creates variables
people = 40
cars = 40
trucks = 15
# checks truth of the statement and prints line 7 if true
if cars > people and cars > trucks:
    print("we like bananas, because they have no bones!")
# prints line 10 if above is false
else:
    print("We still like bananas, because they have no bones!")
# if checks truth of statement cars > people and prints if true
if cars > people:
    print("We should take the cars.")
#prints if cars < people is true
elif cars < people:
    print("We should not take the cars.")
# prints the statement if cars neither > or < people
else:
    print("We can't decide.")

# the rest are similar to the above except with different prints and variables
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
