from num2words import num2words
dict_words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять',
              'eleven': 'одиннадцать', 'twelve': 'двенадцать'}
with open("dz4_in.txt", "r", encoding="utf-8") as f, open("dz4_out.txt", "w", encoding="utf-8") as w:
    for line in f.read().splitlines():
        words = line.split(" - ")
        words[0] = dict_words[num2words(words[1])].capitalize()
        w.write(" - ".join(words) + "\n")
        