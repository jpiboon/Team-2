from user_interface import userInterface

user_input = raw_input("Welcome to Ecosystem Modeling Analysis. Would you like to launch this " +
"program? (Yes/No): ")

if user_input.lower() == 'yes':
    userInterface()
elif user_input.lower() == 'no':
    print "Good bye."
else:
    print "Please run this program again later."