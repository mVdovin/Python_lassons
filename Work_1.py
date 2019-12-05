print('1','=' * 50)

list = [0, 1, 2, 3, 4, 5]
for i in range(len(list)):
    print(list[i])

print('2', '=' * 50)

Capitals = dict([('Russia', 'Moscow'), ('Ukraine', 'Kiyv'), ('USA', 'Washington')])
Countries = ['Russia', 'Poland']

for country in Countries:
    if country in Capitals:
        print('The capital of ' + country + ' is ' + Capitals[country])
    else:
        print('The capital of ' + country + ' is unknown')

print('3', '=' * 50)

for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 15 == 0:
        print("FizzBuzz")
    else:
        print(x)

print('4', '=' * 50)

def bank(a, years, proc):
    for year in range(years):
        a = a*(proc/100)+a
    return a
a=int(input('Введите сумму вклада: '))
years=int(input('Введите на сколько лет: '))
proc=int(input('Введите процент: '))
print(bank(a, years, proc))