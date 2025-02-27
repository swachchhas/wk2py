books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10
}

bookname = input("Enter the book name: ")

if bookname in books:
    while True:
        copies = input("Enter the number of copies: ")
        if copies.isdigit():
            copies = int(copies)
            break
        print("Invalid input. Please enter a valid number.")

    if copies <= books[bookname]:
        print("Available")
    else:
        print("Partially Available")
else:
    print("Unavailable")
