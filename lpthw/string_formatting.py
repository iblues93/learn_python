"""
Exercise 5
"""

my_string = "Hello World!"
dates = [5,7,9]
exchange_rate = 1.5

#formatting string

formated_string = f"{my_string} Today is {dates[1]}th and the exchange rate is {exchange_rate}."
formated_string2 = "{0} Today is {1[1]}th and the exchange rate is {2:.2f}.".format(my_string,dates,exchange_rate/7)

print(formated_string)

print(formated_string2)
