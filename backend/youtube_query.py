import requests
from googleapiclient.discovery import build
from google.cloud import vision
api_key = "AIzaSyCw_3pcvHzyWVhepo2aqfubkOnlJFh1oj0"
youtube = build('youtube', 'v3', developerKey=api_key)
subscription_key = "3d6903da0e4f4ccd9bd1aff31a51fb1d"
endpoint = "https://shafinsiddique.cognitiveservices.azure.com/"
import os
keyphrase_url = endpoint + "/text/analytics/v2.1/keyphrases"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'HackTheValley-f1afcc1d51aa.json'

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    message = ""
    for text in texts:
        message += text.description

    return message


def get_link(sentence):
    req = youtube.search().list(part='snippet',
                              q=sentence,
                              type='video',
                              maxResults=5)
    res = req.execute()
    try:
        return "https://www.youtube.com/embed/" + res['items'][0]['id']['videoId']
    except:
        pass

def get_key_phrases(text):
    documents = {"documents": [
        {"id": "1", "language": "en",
         "text": text}]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(keyphrase_url, headers=headers, json=documents)
    key_phrases = response.json()
    return key_phrases['documents'][0]['keyPhrases']


if __name__ == "__main__":
    pass


