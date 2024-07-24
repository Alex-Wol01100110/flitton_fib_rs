import argparse
from .flitton_fib_rs import fibonacci_number

def fib_number_command() -> None:
    parser = argparse.ArgumentParser(description='Calculate Fibonacci numbers')
    parser.add_argument(
        '--number',
        action='store',
        type=int,
        required=True,
        help="Fibonacci number to becalculated"
    )
    args = parser.parse_args()
    print(
        "Your Fibonacci number is: "
        f"{fibonacci_number(n=args.number)}"
    )