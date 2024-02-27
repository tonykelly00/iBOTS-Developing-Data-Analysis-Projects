import argparse

#create an argument parser
parser = argparse.ArgumentParser(description='Gretting user.')

#create positional arguments
parser.add_argument('name', type=str, help='name of the user')

#create optional arguments
parser.add_argument('--group', type=str, default='iBehave', help='group name')

#parse the argument
args = parser.parse_args()

#args takes from terminal, but can take from the script
#args = parser.parse_args(['tony'])

#python code

#not good practice
func(args)

#better practice to specify excatly the input.
func(args.name, args.name)

print(f'Hello, {args.name}! is part of {args.group}')