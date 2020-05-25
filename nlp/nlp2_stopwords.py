from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = "I am going to the zoo tomorrow"

stop_words = set(stopwords.words("english"))
words = word_tokenize(example)

filtered_words = []

for w in words:
    if w not in stop_words:
        filtered_words.append(w)
print(filtered_words)


