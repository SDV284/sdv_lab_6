def process_set(text):
    result_set = set()
    result_list = []

    for char in text:
        if char.isalpha() and char not in result_set:
            result_set.add(char)
            result_list.append(char)

    print("".join(result_list))

text = "abracadabra"
process_set(text) 