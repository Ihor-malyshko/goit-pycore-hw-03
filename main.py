import datetime

def get_days_from_today(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.date.today()
    delta = today - date
    return delta.days

# data = input("Enter a date in YYYY-MM-DD format: ")
# res = get_days_from_today(data)
# print(res)

import random

def get_numbers_ticket(min, max, quantity):
  if quantity > (max - min + 1):
    return "Кількість чисел перевищує діапазон!"
  numbers = []
  for i in range(quantity):
      while True:
          number = random.randint(min, max)
          if number not in numbers:
              numbers.append(number)
              break
  numbers.sort()
  return numbers

# lottery_numbers = get_numbers_ticket(1, 49, 6)
# print("Ваші лотерейні числа:", lottery_numbers)

import re

def normalize_phone(phone_number):
  # phone_number = phone_number.strip().replace("\\t", "").replace("\\n", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
  # make some magic
  phone_number = re.sub(r'\D', '', phone_number) 
  if phone_number.startswith("0"):
      phone_number = '+380' + phone_number[1:]
  elif phone_number.startswith("380"):
      phone_number = '+' + phone_number
  return phone_number

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


def get_upcoming_birthdays(users):
    today = datetime.datetime.today().date()
    upcoming = []
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if (birthday_this_year - today).days >= 0 and (birthday_this_year - today).days < 8:
          if birthday_this_year.weekday() == 5:
            upcoming.append({"name": user["name"], "congratulation_date": (birthday_this_year + datetime.timedelta(days=2)).strftime("%Y-%m-%d")})
          elif birthday_this_year.weekday() == 6:
            upcoming.append({"name": user["name"], "congratulation_date": (birthday_this_year + datetime.timedelta(days=1)).strftime("%Y-%m-%d")})
          else:
            upcoming.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y-%m-%d")})

    return upcoming

# users = [
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "John Doe", "birthday": "1985.06.15"},
#     {"name": "John Doe", "birthday": "1985.06.16"},
#     {"name": "John Doe", "birthday": "1985.06.17"},
#     {"name": "John Doe", "birthday": "1985.06.21"},
#     {"name": "John Doe", "birthday": "1985.06.22"},
#     {"name": "John Doe", "birthday": "1985.06.23"},
#     {"name": "Jane Smith", "birthday": "1990.07.27"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)
