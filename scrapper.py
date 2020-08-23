#from src.InstagramScrapper import InstagramScrapper
from src.TwitterScrapper import TwitterScrapper

if __name__ == '__main__':

    print("Starting Social Media Scrapper...")
    keyword = str(input("Enter keyword to search for: "))
    twitter_limit = int(input("Enter how many posts to scrape from Twitter: "))

    consumerKey = '9oyfw8phVoKtKl6QRWRhPAIxP'
    consumerSecret = 'oOjSoKvWYRtUIoGZa7tt3ySoVJj5UQNxJ2Txc1FCWJS2LHsa5y'
    accessToken = '920163998523203586-YlL0u7LHhOcw0qBrlDuFtVSXKFki6uB'
    accessTokenSecret = 'VOz1TINUYQFRSGJnMdZxMBY0Y265VaAYfAbiUu0P10MJ4'

    twitter = TwitterScrapper()
    twitter.Scrape_Twitter(Consumer_Key=consumerKey,
                           Consumer_Secret=consumerSecret,
                           Access_Token=accessToken,
                           Access_Token_Secret=accessTokenSecret,
                           tag=keyword,
                           limit=twitter_limit,
                           lang='en')  # Language codes: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


    print("Stopping Social Media Scrapper...")
