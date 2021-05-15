sentence = input("please enter a sentence")

sentence= list(sentence)

list_words = []
number_words = []

for i in sentence:
    if i in list_words:
        pass
    list_words.append(i)
    x = sentence.count(i)
    number_words.append(x)

my_dict = zip(list_words,number_words)
print(dict(my_dict))
