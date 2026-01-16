from typing import Union

def fizzbuzz(n: int) -> Union[str, int]:
    """
    Returns 'fizz' for multiples of 3, 'buzz' for multiples of 5,
    'fizzbuzz' for multiples of both, and the number otherwise.
    """
    if n % 15 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return n

def main():
    for i in range(16, 31):
        print(fizzbuzz(i))

if __name__ == "__main__":
    main()
