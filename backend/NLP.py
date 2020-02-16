from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
from nltk.corpus import stopwords
import nltk
from nltk import FreqDist
# import boto3
# Instantiates a client
# aws_client = boto3.client("comprehend")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'HackTheValley-f1afcc1d51aa.json'
client = language.LanguageServiceClient()

def remove_stopwords(word_list):
        processed_word_list = []
        for word in word_list:
            word = word.lower() # in case they arenet all lower cased
            if word not in stopwords.words("english") and word.isalnum():
                processed_word_list.append(word)
        return processed_word_list

def get_sentiment(text):
    """Get the sentiment score for a certain text from the GCP API."""
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return sentiment.score

def word_freq(text):
    word_tokenized = nltk.word_tokenize(text)
    without_stopwords = remove_stopwords(word_tokenized)
    fdist = FreqDist(without_stopwords)

    print(fdist.keys())


if __name__ == "__main__":
    word_freq("Hi, i am very very very very very very depressed like depressed depressed.")



