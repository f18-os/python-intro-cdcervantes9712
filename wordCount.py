import sys

f = open(sys.argv[1], 'r')

data = f.read()
word_list = data.split(" ")

word_list[:] = (value for value in word_list if value != '\t')

wordCounter = {}

for word in word_list:
    wordCounter[word] = wordCounter.get(word, 0) + 1

word_freq = []
for key, value in wordCounter.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)
print(word_freq)
