#Third fizzbuzz with clean and more efficient code
def fizzbuzz_3():
    output = [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0
        else "Fizz" if i % 3 == 0
        else "Buzz" if i % 5 == 0
        else str(i)
        for i in range(1, 101) 
  ]

    return output


if __name__ == "__main__":
    fizzbuzz_output = fizzbuzz_3()
    print("\n".join(fizzbuzz_output))