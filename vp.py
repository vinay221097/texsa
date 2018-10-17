from summarizer import inverse_sentence_frequency
with open("training.txt") as file:
    text = file.read()
words=inverse_sentence_frequency(text)
for word in words:
	print(word,":",words[word])