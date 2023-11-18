""" This script takes a float input, rounds it up if the last digit is 5 or greater """


def main():
    ex: float = float(input("Enter a float number: "))

    if int(str(ex)[-1]) >= 5:
        result = ex + 1 / 10 ** cdp(ex)
    else:
        result = ex

    print(f"                    : \x1b[1m{result}\x1b[0m")


def cdp(number):
    num_str = str(number)

    if '.' in num_str:
        decimal_part = num_str.split('.')[1]
        return len(decimal_part)
    else:
        return 0


if __name__ == "__main__":
    main()
