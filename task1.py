def total_salary(path):
  try:
    with open(path, 'r') as file:
      total = 0
      worker = 0
      for line in file:
          parts = line.strip().split(',')
          if len(parts) == 2:
              try:
                  salary = int(parts[1])
                  total += salary
                  worker += 1
              except ValueError:
                  print(f"Неправильний формат зарплати: {parts[1]}")
      average = total / worker if worker > 0 else 0
    return total, average
  except FileNotFoundError:
    print(f"не знайдено path: '{path}'")
    return 0, 0
  except Exception as e:
    print(f"помилка: {e}. path: {path}")
    return 0, 0
  

# useFn
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")
