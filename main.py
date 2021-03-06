import argparse
import wget

import pandas as pd

from pre_process.pre_prossessing import Processing
from social_collector.collect_data import CollectData


def get_args():

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--ttuser',
      '-tt',
      default = 'camilafarani',
      type = str,
      help = 'user that will be researched on twitter')
  parser.add_argument(
      '--social-network',
      '-sn',
      default = ['twitter'],
      nargs='+',
      help = 'social network that will be researched, can be more than one')

  return parser.parse_args()


if __name__ == "__main__":

    args = get_args()

    collector = CollectData(args.social_network, args.ttuser)
    collector.network_handler()

    processing = Processing(args.social_network, args.search_words)
    processing.pre_processing()
