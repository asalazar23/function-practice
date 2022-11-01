#functions printing and returning

#print something is only for displaying some data, you are doing nothing with the date

#when you return in a function, you are going to use it in another part of your program
from addfruit import add_fruit
from subtractfruit import subtract_fruit
from dividefruit import divide_fruit
from displayfruit import display_fruit



apples = int(input("how many appleS? "))
oranges = int(input("how many oranges? "))

#add fruit
#whenever you return a value, you must put the returned value inside of a variable
fruit_added = add_fruit(apples,oranges)
print(fruit_added)
#subtract fruit
fruit_subtracted = subtract_fruit(apples,oranges)
print(fruit_subtracted)
#divide fruit
fruit_divided = divide_fruit(apples,oranges)
print(fruit_divided)
#display the added fruit, subtracted fruit, and the divided fruit
fruit_displayed = display_fruit(fruit_added, fruit_subtracted, fruit_divided)



