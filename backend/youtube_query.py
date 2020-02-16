from googleapiclient.discovery import build
api_key = "AIzaSyCw_3pcvHzyWVhepo2aqfubkOnlJFh1oj0"
youtube = build('youtube', 'v3', developerKey=api_key)

def get_link(sentence):
    req = youtube.search().list(part='snippet',
                              q=sentence,
                              type='video',
                              maxResults=5)
    res = req.execute()
    return "https://www.youtube.com/embed/" + res['items'][0]['id']['videoId']

def get_tweets(sentence):
    
print(get_link("The Avengers: Tony Stark"))
