#Maciej Sudol
#countskip
#The user enters a starting number, a ending number and a number to count by.
#The program takes the three numbers and outputs the results.


print ("Hello, let me do some counting for you!")

starting_num = int (input("Please give me a starting number. "))
ending_num = int (input("Please give me an ending number. "))
count_by = int (input("By which amount am I to count? "))

print ("Counting:")
for i in range(starting_num, ending_num, count_by):
    print (i)
