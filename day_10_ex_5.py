rows = int(input("Enter number of rows: "))
if rows <= 0:
	print("Please enter a positive integer.")
else:
    for i in range(1, rows + 1): 
        print(" " * (rows - i) + "* " * i)
        print(" " * (rows - i) + "*" * (2 * i - 1))


