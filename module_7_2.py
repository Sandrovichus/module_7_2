def custom_write(file_name: str, strings: list) -> dict:
    file_dict = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        file_dict[(strings.index(i) + 1, file.tell())] = i
        file.write(f'{i}\n')
    file.close()
    return file_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

