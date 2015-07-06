#!/usr/bin/python

# Python script to demonstrate use of methods on a list

def main():
    snacks=['idly','dosa','vada','bisibelebhath','chowchowbhat']
    lunch_items=['chapati','rice','pulao']
    sweets=['mysorepaak','chiroti','kazubarfi','rasmalai']

    snacks_cap=[s.capitalize() for s in snacks]
    print "==Snack List:==" 
    print snacks_cap
    print ""

    print "==Lunch List:==" 
    lunch_up=[l.upper() for l in lunch_items]
    print lunch_up
    print ""

    # I didn't know that + works for list as well
    all_food=snacks + lunch_items + sweets
    print "==Everything:==" 
    print all_food
    print ""

    # Reverse act in-place
    all_food.reverse()
    print all_food
    # Give me idly and keep remaining list
    print "I love to eat " + all_food.pop() + " as breakfast"
    print all_food.pop() + " is my favorite "

    # I keep remaining list
    print all_food

if __name__ == "__main__":
    main()
