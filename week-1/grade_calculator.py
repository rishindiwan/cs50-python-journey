n = int(input("Enter the marks: "))

if n >= 0 and n <= 100:

    if 90 <= n <= 100:
        print("Grade: A")

    elif 70 <= n < 90:
        print("Grade: B")

    elif 60 <= n < 70:
        print("Grade: C")

    elif 40 <= n < 60:
        print("Grade: D")

    else:
        print("Grade: E")

else:
    print("Invalid Marks")
