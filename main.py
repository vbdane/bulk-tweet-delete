import tweepy
import webbrowser
import time

consumer_key = "" #INSERT YOUR TWITTER DEVELOPER KEY
consumer_secret = "" #DEVELOPER SECRET
my_uri = 'oob'


def login(key, secret, uri):
    oauth = tweepy.OAuthHandler(key, secret, uri)
    auth_link = oauth.get_authorization_url()
    webbrowser.open(auth_link)

    code = input("Enter your verification code: ")
    try:
        oauth.get_access_token(code)
        return tweepy.API(oauth)

    except Exception as e:
        print(e)
        time.sleep(5)
        quit()


def delete(api):
    tweets = 0
    for tweet in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(tweet.id)
            print("Tweet ID %s Deleted" % tweet.id)
            tweets += 1
        except Exception as e:
            print("Failed to delete Tweet ID: ", tweet.id)
            print("Error: ", e)
            time.sleep(5)
            quit()
    print("Success! %s tweets deleted" % tweets)


if __name__ == '__main__':
    api_intf = login(consumer_key, consumer_secret, my_uri)
    delete(api_intf)
