# Q1-
def list(num_list):
    even_num = []
    for number in num_list:
        if number % 2 == 0:
            even_num.append(number)
    return even_num


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_num = list(num_list)
print(even_num)


# Q2-
def count(text):
    cons = 0
    vow = 0
    space = 0
    text = text.lower()
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vow += 1
        elif i == ' ':
            space += 1
        else:
            cons += 1
    return {"vowels": vow, "consonants": cons, "spaces": space}


text = input("Enter a string: ")
result = count(text)
print("Vowels:", result["vowels"])
print("Consonants:", result["consonants"])
print("Spaces:", result["spaces"])


# Q3-
def longestWord(words):
    longest_W = ""
    longest_index = -1
    for i, word in enumerate(words):
        if len(word) > len(longest_W):
            longest_W = word
            longest_index = i
        elif len(word) == len(longest_W):
            longest_W = word
    print("Longest word:", longest_W, "at index:", longest_index)
    return longest_W, longest_index


words = ["wap", "wdg", "train", "linkhoffman", "busch", "track", "word"]
longest_word, longest_index = longestWord(words)
