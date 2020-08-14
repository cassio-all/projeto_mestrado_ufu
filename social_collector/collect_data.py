import configparser

import tweepy as tw
import pandas as pd

from api.api import Api
from data.data_handler import DataHandler


class CollectData(object):

    # search_words: Term for related tweets
    # social_networks: Social networks that will be collected the data

    def __init__(self, social_networks, tt_user):

        self.tt_user = tt_user
        self.social_networks = social_networks

    def network_handler(self):

        for social_network in self.social_networks:

            if social_network == 'twitter':
                self.get_tweets()

    def get_tweets(self):

        api = Api.twitter_api()  
        tweets = api.user_timeline(screen_name=self.tt_user,
                                   count=200,
                                   include_rts=False,
                                   exclude_replies=True)
        last_id = tweets[-1].id
        while (True):
            more_tweets = api.user_timeline(screen_name=self.tt_user,
                                            count=200,
                                            include_rts=False,
                                            exclude_replies=True,
                                            max_id=last_id-1)
            # There are no more tweets
            if (len(more_tweets) == 0):
                break
            else:
                last_id = more_tweets[-1].id-1
                tweets = tweets + more_tweets

        text = []
        created = []
        image_url = []

        for tweet in tweets:

            text.append(tweet.text.encode('utf-8')) # Get tweets
            created.append(tweet.created_at) # Get timestamp
            try:
                image_url.append(tweet.entities['media'][0]['media_url'])
            except:
                image_url.append('')

        dataset = pd.DataFrame({"Created_at": created,
                                "text": text,
                                "image_url": image_url})
        
        store_data = DataHandler('twitter', self.tt_user)
        store_data.store_network_dataset(dataset)
        import pdb; pdb.set_trace()
        print('a')
