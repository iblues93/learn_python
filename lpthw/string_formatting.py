"""
Exercise 5
"""

my_string = "Hello World!"
dates = [5,7,9]
exchange_rate = 1.5/7

#formatting string

formated_string = f"{my_string} Today is {dates[1]}th and the exchange rate is {round(exchange_rate,2)}."
formated_string2 = "{0} Today is {1[1]}th and the exchange rate is {2:.2f}.".format(my_string,dates,exchange_rate)

print(formated_string)

print(formated_string2)
