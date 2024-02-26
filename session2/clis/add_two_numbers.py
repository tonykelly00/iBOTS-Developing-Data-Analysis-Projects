import argparse

#create an argument parser
parser = argparse.ArgumentParser(description='sum of 2 numbers=.')

#create positional arguments
parser.add_argument('num1', type=int, help='1st number')

#create optional arguments
parser.add_argument('num2', type=int, help='2nd number')


#parse the argument
args = parser.parse_args()

#args takes from terminal, but can take from the script
#args = parser.parse_args(['tony'])

#python code


print(f'Hello, {args.num1} + {args.num2} is equal to {args.num1+args.num2}')