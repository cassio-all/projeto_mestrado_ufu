import configparser

import tweepy as tw
import pandas as pd
import numpy as np

from api.api import Api
from data.data_handler import DataHandler


class CollectData(object):

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
            if (len(more_tweets) == 0):
                break
            else:
                last_id = more_tweets[-1].id-1
                tweets = tweets + more_tweets

        created = []
        tweet_id = []
        text = []
        hashtags = []
        symbols = []
        image_url = []
        user_mentions = []
        user_id = []
        user_name = []
        user_screen_name = []
        user_location = []
        user_description = []
        user_protected = []
        user_followers_count = []
        user_friends_count = []
        user_listed_count = []
        user_created_at = []
        user_favourites_count = []
        user_utc_offset = []
        user_timezone = []
        user_geo_enabled = []
        user_verified = []
        user_statuses_count = []
        user_lang = []
        user_contributors_enabled = []
        user_is_translator = []
        user_is_translation_enabled = []
        quoted_status = []
        quoted_text = []
        quoted_media = []
        quoted_user_id = []
        import pdb; pdb.set_trace()
        for tweet in tweets:
            
            created.append(tweet.created_at)
            tweet_id.append(tweet.id)
            text.append(tweet.text)
            hashtags.append(tweet.entities['hashtags'])
            symbols.append(tweet.entities['symbols'])
            user_mentions.append(tweet.entities['user_mentions'])
            user_id.append(tweet.user.id)
            user_name.append(tweet.user.name)
            user_screen_name.append(tweet.user.screen_name)
            user_location.append(tweet.user.location)
            user_description.append(tweet.user.description)
            user_protected.append(tweet.user.protected)
            user_followers_count.append(tweet.user.followers_count)
            user_friends_count.append(tweet.user.friends_count)
            user_listed_count.append(tweet.user.listed_count)
            user_created_at.append(tweet.user.created_at.strftime("%Y-%m-%d"))
            user_favourites_count.append(tweet.user.favourites_count)
            user_utc_offset.append(tweet.user.utc_offset)
            user_timezone.append(tweet.user.time_zone)
            user_geo_enabled.append(tweet.user.geo_enabled)
            user_verified.append(tweet.user.verified)
            user_statuses_count.append(tweet.user.statuses_count)
            user_lang.append(tweet.user.lang)
            user_contributors_enabled.append(tweet.user.contributors_enabled)
            user_is_translator.append(tweet.user.is_translator)
            user_is_translation_enabled.append(tweet.user.is_translation_enabled)
            
            if tweet.is_quote_status == True:

                try:
                    quoted_text.append(tweet.quoted_status.text)
                except AttributeError:
                    quoted_text.append(np.nan)
                try:
                    quoted_user_id.append(tweet.quoted_status.user.id)
                except AttributeError:
                    quoted_user_id.append(np.nan)
                try:
                    quoted_media.append(tweet.quoted_status.entities['media'][0]['media_url'])
                except Exception:
                    quoted_media.append(np.nan)
            else:
                quoted_text.append(np.nan)
                quoted_user_id.append(np.nan)
                quoted_media.append(np.nan)

            try:
                image_url.append(tweet.entities['media'][0]['media_url'])
            except:
                image_url.append(np.nan)
            
        dataset = pd.DataFrame({"created_at": created,
                                "tweet_id": tweet_id,
                                "text": text,
                                "hashtags": hashtags,
                                "symbols": symbols,
                                "image_url": image_url,
                                "user_mentions": user_mentions,
                                "user_id": user_id,
                                "user_name": user_name,
                                "user_screen_name": user_screen_name,
                                "user_location": user_location,
                                "user_description": user_description,
                                "user_protected": user_protected,
                                "user_followers_count": user_followers_count,
                                "user_friends_count": user_friends_count,
                                "user_listed_count": user_listed_count,
                                "user_created_at": user_created_at,
                                "user_favourites_count": user_favourites_count,
                                "user_utc_offset": user_utc_offset,
                                "user_timezone": user_timezone,
                                "user_geo_enabled": user_geo_enabled,
                                "user_verified": user_verified,
                                "user_statuses_count": user_statuses_count,
                                "user_lang": user_lang,
                                "user_contributors_enabled": user_contributors_enabled,
                                "user_is_translator": user_is_translator,
                                "user_is_translation_enabled": user_is_translation_enabled,
                                "quoted_text": quoted_text,
                                "quoted_media": quoted_media,
                                "quoted_user_id": quoted_user_id,
                                })
        import pdb; pdb.set_trace()
        store_data = DataHandler('twitter', self.tt_user)
        store_data.store_network_dataset(dataset)
        import pdb; pdb.set_trace()
        print('a')
