import sys

res_list = []

char_list = [".", ",", "?"]

line = input()

word_list = line.split(" ")

for word in word_list:
    if "." in word or "," in word or "?" in word and len(word) > 1:
        char1 = word[-1:]
        char2 = word[0]
        if char1 in char_list and char2 not in char_list:
            res_list.append(word[:-1][::-1] + char1)
        if char1 not in char_list and char2 in char_list:
            res_list.append(char2 + word[1:][::-1])
        if char1 in char_list and char2 in char_list:
            res_list.append(char2 + word[1:-1][::-1] + char1)

    if word in char_list:
        res_list.append(word)
    if word not in char_list and "." not in word and "," not in word and "?" not in word:
        res_list.append(word[::-1])
print(" ".join(res_list))
