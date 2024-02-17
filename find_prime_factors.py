def finding_prime_factors():
    # finding all divisors of the numbers
    while True:
        try:
            number = float(input("Enter the number for which you want to find prime factors: "))
        except ValueError:
            print(f"Number doesn't have prime factors or giving data isn't a number at all!")
            continue

        if number <= 1 or number % 1 != 0:
            print(f"Number {number} doesn't have prime factors")
            return

        number = int(number)
        list_prime_factors = []

        while number % 2 == 0:
            results = number // 2
            number = results
            list_prime_factors.append(2)
        while number % 3 == 0:
            results = number // 3
            number = results
            list_prime_factors.append(3)
        while number % 5 == 0:
            results = number // 5
            number = results
            list_prime_factors.append(5)
        while number % 7 == 0:
            results = number // 7
            number = results
            list_prime_factors.append(7)
        if number % number == 0 and number != 1:
            list_prime_factors.append(number)
            str_list = str(list_prime_factors)
            print(f"Prime factors: {str_list} that contains last divisor")
        else:
            str_list = str(list_prime_factors)
            print(f"Prime factors: {str_list} that doesn't contain last divisor because it's = '1' ")
        return

finding_prime_factors()