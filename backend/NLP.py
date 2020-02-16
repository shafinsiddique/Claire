from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os

# Instantiates a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'HackTheValley-f1afcc1d51aa.json'
client = language.LanguageServiceClient()

def get_sentiment(text):
    """Get the sentiment score for a certain text from the GCP API."""
    document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return sentiment.score



