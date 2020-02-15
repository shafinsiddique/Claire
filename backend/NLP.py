from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
# Instantiates a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'HackTheValley-f1afcc1d51aa.json'

client = language.LanguageServiceClient()

# The text to analyze
text = 'I am extremely depressed. Over the last few weeks, i hav ebeen feeling very sick.'
document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
m
sentiment = client.analyze_sentiment(document=document)

print(sentiment)
