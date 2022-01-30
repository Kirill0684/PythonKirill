name = input('input name: ')
surname = input('input surname: ')
year = input('input year of birth: ')
number = input('tel. number: ')
city = input('input city: ')
email = input('email: ')

def func(name, surname, year, city, number, email):
    print(f'name - {name}, surname -{surname}, year - {year}, city - {city}, number - {number}, email - {email}')


func(name, surname, year, city, number, email)