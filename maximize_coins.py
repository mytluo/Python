def coins(amt):
	""" take in an amount of coins and returns maximized coin allotment using a generator """
	if len(amt) == 1:
		# add a 0 at the end if there is only 1 digit
        amt = amt + "0"
    try:
        amt = int(amt)
        # if there is more than 2 digits, round the number and truncate to 2 digits before passing to divmod()
        if amt > 99:
            round_place = (len(str(amt)) - 2) * -1
            amt = str(round(amt, round_place))
            amt = int(amt[:2])
        first = divmod(amt, 25)
        yield [first[0], "quarter(s)"]
        second = divmod(first[1], 10)
        yield [second[0], "dime(s)"]
        third = divmod(second[1], 5)
        yield [third[0], "nickel(s)"]
        yield [third[1], "pennies"]
    except Exception as e:
        print(e)
if __name__ == '__main__':
    user_input = input("Please enter an amount (less than a dollar): $0.")
    res = coins(user_input)
    print("".join(map(str, res)))
