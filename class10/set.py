prime_number = {2 ,3 , 5 , 7 ,11 , 11}
even_number = { 2 , 4 , 6 , 8 , 10 , 12}


print(prime_number)
print(even_number)


print(prime_number  | even_number)
print(prime_number & even_number)
print(prime_number - even_number)
print(prime_number ^ even_number)

prime_number.add(13)
print(prime_number)
even_number.remove(10)
print(even_number)
