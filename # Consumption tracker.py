# Consumption tracker

# FURTHER UPDATES WILL BE MADE, ID LIKE TO

# You shoule be able to:
# Set targets - Daily intake, weight loss etc
# Maybe you can scan items or receites to recieve calories intake etc
# input your personal details relevant to your health, physical attributes
# create daily intake plans
# Input daily intake, example input each item or amount of calories and it updates and tracks your progress

# Welcome message
print("Welcome to your Consumption tracker")

# Consumption tracker list
tracker = ['a','b','c']
# Targert tracker list
targets = []

while True:
    # The initial questions provides the options view or update
    question = input("""Would you like to:
    1 - Action Tracker
    2 - Action Targets
    3 - Action Intake
    Please input tracker, target or intake in lower case.
    """)
    
    if question == 'tracker':

    # Option view the tracker
        if question == 'view':
            print(tracker)
        
        # Update your consumption tracker
        elif question == 'update':
            # User choosing update, provides two additioanl options, to either add or remove
            question2 = input("Would you like to 'add' to your tracker or 'remove' :")
                # User choosing add will allow them to append the tracker list
            if question2 == 'add':
                    add_question = input("What would you like to add? :")
                    add = tracker.append(add_question)
                    print(f"{add_question} added")
            elif question2 == 'remove':
                    remove_question = input("What would you like to remove? ")
                    remove = tracker.remove(remove_question)
                    print("remove")
            else:
                    print("Please input add in lowercase or remove")
            
        else:
            print("Please input in lowercase view or update")

    elif question == 'target':
        print("target")

    elif question == 'intake':
        print("intake")
