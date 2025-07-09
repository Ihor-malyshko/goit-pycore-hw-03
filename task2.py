
def get_cats_info(path):
  cats_info = []
  try:
    with open(path, 'r', encoding='utf-8') as file:
      for line in file:
        parts = line.strip().split(',')
        cat = {
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]
              }
        cats_info.append(cat)
  except Exception as e:
    print(f"Error reading file: {e}")
  return cats_info

# useFn
cats_info = get_cats_info("cats_file.txt")
print(cats_info)