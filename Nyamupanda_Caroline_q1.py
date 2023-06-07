# Caroline NYAMUPANDA
# R00206878

def details():
    name = input("Whats is your name?")
    birth_date = input(int("What is year were you born ?"))
    return name, birth_date


def process_details():
    uppers = 0
    year = 0
    for value in details():
        if value.isupper():
            uppers += 3
        elif value.isnumeric():
            year += 1

    return details, year


def main():
    print(details())
    print(process_details())


if __name__ == '__main__':
    main()
