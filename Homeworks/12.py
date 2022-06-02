'''Implement lambda function to return "Full name: <name> - <surname>" string,
 taking name and surname from args,  assign to variable and apply on given user inputs, print result'''
import sys

first_name = sys.argv[1]
last_name = sys.argv[2]
full_name = lambda first_name, lastname: f'{first_name} {last_name}'

print(full_name(first_name,last_name))
