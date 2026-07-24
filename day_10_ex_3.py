try:
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
except ValueError:
    print("Please enter valid integers.")
else:
    if start > end:
        print("Start number must be less than or equal to end number.")
    else:
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num)