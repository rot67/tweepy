import tweepy
# Authenticate to twitter
Auth = tweepy.OAuthHandler("YnyNgiTkvlr0XWHtATWbKlKc9", "Xc937Sci9qqJknWQUwYKmzM6pR47frbGRoqEed8JYeDimDozXi")
Auth.set_access_token("781175424-HwxbnfuoL7Wc8WYPCQkWRwcE8AZuhFy6eYeNlG1l", "4vgQaMMiPWH1uh66Gg2YzTXlF4DY13840GZWxm6WGorIp")
 
api = tweepy.API(Auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
