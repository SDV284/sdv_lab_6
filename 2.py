def swap_max_min(lst):
  if not lst:
    return lst

  max_val = max(lst)
  min_val = min(lst)

  max_index = lst.index(max_val)
  min_index = lst.index(min_val)

  new_lst = lst[:]
  new_lst[max_index] = min_val
  new_lst[min_index] = max_val

  return new_lst

my_list = list(map(int,input("Введіть елементи списку через пробіл: ").split()))
new_list = swap_max_min(my_list)
print(f"Оригінальний список: {my_list}")
print(f"Список з поміняними місцями max та min: {new_list}") 