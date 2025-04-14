def main():
    # Step 1: User se number lena
    curr_value = int(input("Enter a number: "))

    # Step 2: Jab tak value 100 se chhoti hai, loop chalayen
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
