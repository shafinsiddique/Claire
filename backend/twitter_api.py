import tweepy

def get_urls(keywords):
    auth = tweepy.OAuthHandler("tVbMbW31AeYh7cuUtk7IpvotF", "Ls7wvwDk2TNhzJ83C1B6an9dZiIinY8rHVBMJygeeZEJz3u3xV")
    auth.set_access_token("747290977216323584-pQ135YWmK4mHzRXmceXmK0RqeFfHchJ", "gLoVw2csmDWi7ndkGEE1DiwDH3dN1mQarxWxukUNdtSXg")
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweet_urls = []
    for i in keywords:
        tweets = tweepy.Cursor(api.search, q=i, lang="en").items(10)
        for status in tweets:
            for url in status.entities['urls']:
                if 'twitter' in url['expanded_url']:
                    tweet_urls.append(url['expanded_url'])

    return tweet_urls

