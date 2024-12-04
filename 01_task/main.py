import math
from collections import Counter
import string

# Чтение и очистка текста
with open(r'C:\Users\nikon\Documents\MIREA\Discrete_mathematics\01_task\read-file.txt', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation + ' ')).replace('\n', '')

with open(r'C:\Users\nikon\Documents\MIREA\Discrete_mathematics\01_task\write-file.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

# Частота однобуквенных сочетаний
char_count = Counter(cleaned_text)
total_chars = len(cleaned_text)
char_frequencies = [count / total_chars for count in char_count.values()]

# Частота двухбуквенных сочетаний
pairs = [cleaned_text[i:i+2] for i in range(len(cleaned_text) - 1)]
pair_count = Counter(pairs)
total_pairs = len(pairs)
pair_frequencies = [count / total_pairs for count in pair_count.values()]

# Энтропия
def entropy(freq_list):
    return -sum(freq * math.log2(freq) for freq in freq_list if freq > 0)

print("Энтропия на одну букву:", entropy(char_frequencies))
print("Энтропия на одно двухбуквенное сочетание:", entropy(pair_frequencies))

# Длина кода и избыточность
length_code = math.ceil(math.log2(len(char_count)))
rounding_redundancy = 1 - (math.log2(len(char_count)) / length_code)
information_redundancy = 1 - (entropy(char_frequencies) / math.log2(len(char_count)))

print("Длина кода:", length_code)
print("Избыточность округления:", rounding_redundancy)
print("Информационная избыточность:", information_redundancy)

# Удаление 20% наиболее частых символов
top_20_percent = int(len(char_count) * 0.2)
most_common_chars = [char for char, _ in char_count.most_common(top_20_percent)]
filtered_text_most_common = ''.join(char for char in cleaned_text if char not in most_common_chars)
filtered_char_frequencies = [count / len(filtered_text_most_common) for count in Counter(filtered_text_most_common).values()]
print("Энтропия после удаления частых символов:", entropy(filtered_char_frequencies))

# Удаление 20% наименее частых символов
least_common_chars = [char for char, _ in char_count.most_common()[-top_20_percent:]]
filtered_text_least_common = ''.join(char for char in cleaned_text if char not in least_common_chars)
filtered_char_frequencies = [count / len(filtered_text_least_common) for count in Counter(filtered_text_least_common).values()]
print("Энтропия после удаления редких символов:", entropy(filtered_char_frequencies))
