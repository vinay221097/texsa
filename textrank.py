import sys, getopt, os

from summarizer import summarize


# Types of summarization
SENTENCE = 1
WORD = 0

def textrank(text,ratio,summarize_by=SENTENCE,words=None, additional_stopwords=None):
    return summarize(text, ratio, words, additional_stopwords=additional_stopwords)
    

def main():
    ratio =float(sys.argv[1])

    with open("training.txt") as file:
        text = file.read()
    print(textrank(text, ratio))


if __name__ == "__main__":
    main()
