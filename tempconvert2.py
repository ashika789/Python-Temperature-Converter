import temps2

def main():
    print ("\nTemperature Converter\n\n"+\
          "1. Celsius to Fahrenheit\n"+\
          "2. Fahrenheit to Celsius\n")
    user_input = input("Specify which conversion:")
    if user_input == 1:
        t = input('Enter a Celcius value:')
        print (t, 'Degrees Celcius is', temps2.c2f(t), ' Degrees Fahrenheit')
    elif user_input == 2:
        t = input('Enter a Fahrenheit value:')
        print (t , 'Degrees Fahrenheit is ' , temps2.f2c(t) ,  ' Degrees Celsius')
    else:
        print ('Invalid Entry')

main()