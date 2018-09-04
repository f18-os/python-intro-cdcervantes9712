import sys, re, string, timeit

fsource = open(sys.argv[1], 'r')
data = fsource.read()

for char in '-.,\n':
    data = data.replace(char, ' ')
data = data.lower()

word_list = data.split()
word_list[:] = (value for value in word_list if value != '\t')

fsource.close()

wordCounter = {}

for word in word_list:
    wordCounter[word] = wordCounter.get(word, 0) + 1

word_freq = []

for key, value in wordCounter.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)

ftarg = open(sys.argv[2], 'w+')

for word in word_freq:
    ftarg.write(word[1] + ", " + str(word[0]) + "\n")

ftarg.close()
