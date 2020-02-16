import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class twitter_streamer():

    auth = tweepy.OAuthHandler("tVbMbW31AeYh7cuUtk7IpvotF", "Ls7wvwDk2TNhzJ83C1B6an9dZiIinY8rHVBMJygeeZEJz3u3xV")
    auth.set_access_token("747290977216323584-pQ135YWmK4mHzRXmceXmK0RqeFfHchJ", "gLoVw2csmDWi7ndkGEE1DiwDH3dN1mQarxWxukUNdtSXg")
    stream = Stream(auth,)

    #def stream_tweets(self, filename, keywords):



