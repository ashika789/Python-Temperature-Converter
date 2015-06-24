import temps

# Define main function
def main():
	f = float(input('Enter a degree fahrenheit: '))
	# Display the temperature in degrees celsius.
	print('In degrees celsius the temperature is')
	print(format(temps.fahr_to_celsius(f), '.2f'))

	c = input('Enter a degree celsius:')
	# Display the temperature in degrees fahrenheit.
	print('In degrees fahrenheit the temperature is')
	print(format(temps.celsius_to_fahr(c), '.2f'))

main()