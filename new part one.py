while True:
    text = input("Enter a word: ").strip()
    if text == "":
        print("Please enter a non-empty string. Try again.")
        continue
    # reject inputs that represent numbers (int or float)
    try:
        float(text)
        print("Please enter a string, not a number. Try again.")
        continue
    except ValueError:
        pass
    reverse_text = text[::-1]
    print("Reversed word:", reverse_text)
    break
