from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

example = "The plane was grounded. It was due a passenger misbehaving"

words = word_tokenize(example)
stop_words = set(stopwords.words("english"))

filtered_words =[]
for w in words:
    if w not in stop_words:
        filtered_words.append(w)


ps = PorterStemmer()

for w in filtered_words:
    print(ps.stem(w))


