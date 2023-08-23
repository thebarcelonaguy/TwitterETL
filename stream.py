import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os
import subprocess

# importing file which sets env variable
subprocess.call("./settings.sh", shell=True)
print('successfully loaded')


print(os.environ)
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
password = os.environ.get('PASSWORD')


print(consumer_key,consumer_secret,access_token,access_token_secret)


def connect(id, username, created_at, tweet, retweet_count, place, location):
	try:
		con = mysql.connector.connect(host='localhost',
		database='twitterdb', user='purvi', password=password, charset='utf8')

		if con.is_connected():
			"""
			Insert twitter data
			"""
			cursor = con.cursor()
			# twitter, golf
			query = "INSERT INTO tweets (id, username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(query, (id, username, created_at, tweet, retweet_count, place, location))
			con.commit()
			print('INSERTED!!!!!!!!!!!!!!')


	except Error as e:
		print(e)

	cursor.close()
	con.close()

	return


class Streamlistener(tweepy.StreamListener):

	def on_connect(self):
		print("You are connected to the Twitter API")

	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	def on_data(self, data):

		try:
			raw_data = json.loads(data)
			# print('RAW DATA',raw_data)

			if 'text' in raw_data:
				username = raw_data['user']['screen_name']
				id = raw_data['id_str']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None

				location = raw_data['user']['location']

				# insert data just collected into MySQL database
				connect(id, username, created_at, tweet, retweet_count, place, location)
				print('Tweet Content:', id, username, created_at, tweet, retweet_count, place, location)

				print("Tweet collected at: {} ".format(str(created_at)))
		except Error as e:
			print(e)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    listener = Streamlistener(api =api)
    stream = tweepy.Stream(auth, listener = listener)
    track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
    
    stream.filter(track = track,languages = ['en'])