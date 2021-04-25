def account_validation(number):
    if number:
        if len(str(number)) == 10:
            try:
                int(number)
                return True
            except ValueError:
                print("Account number must integer")
                return False
        elif len(number) != 10:
            print("Account number must be 10-digits number")
            return False
    else:
        print("The field is required")
        return False