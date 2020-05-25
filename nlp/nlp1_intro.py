from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. R, how are you doing today? I heard you are learning NLP."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)