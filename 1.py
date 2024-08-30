def insert_on_odd_positions(lst):
  new_elements = []
  num_new_elements = int(input("Введіть кількість нових елементів: "))
  for i in range(num_new_elements):
      element = input(f"Введіть елемент {i+1}: ")
      new_elements.append(element)
  index = 1
  for element in new_elements:
    if index < len(lst):
        lst.insert(index, element)
        index += 2
    else:
      lst.append(element)
      index += 2
  return lst

def print_list(lst):
  print("Список:", lst)

input_str = input("Введіть елементи списку через пробіл: ")
lst = input_str.split()

new_list = insert_on_odd_positions(lst)
print_list(new_list) 