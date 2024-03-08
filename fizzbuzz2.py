# Second fizzbuzz with more condensed code
def fizzbuzz_2():
    for i in range(1, 101):
        # Made a seperate "if" statement for easier reading and cleanliness
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz_2()