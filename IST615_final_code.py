{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "IST615_final_code.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sharvil-Turbadkar/Analyzing-Sale-trends-for-FudgeCorporation-/blob/master/IST615_final_code.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DQ3xJMKLgMYe"
      },
      "source": [
        "# Import Libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "from textblob import TextBlob\n",
        "from wordcloud import WordCloud\n",
        "import plotly.graph_objects as go\n",
        "import plotly.express as px\n",
        "import json\n",
        "import os\n",
        "import tweepy\n",
        "import pandas as pd\n",
        "import re\n",
        "import string"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kTE175lbh-Az"
      },
      "source": [
        "#accessing credentials file to scrape twitter API\n",
        "with open('credentials.txt') as cred_data:\n",
        "        info = json.load(cred_data)\n",
        "        consumer_key = info['CONSUMER_KEY']\n",
        "        consumer_secret = info['CONSUMER_SECRET']\n",
        "        access_key = info['ACCESS_KEY']\n",
        "        access_secret = info['ACCESS_SECRET']\n",
        "        #google_api = info['GOOGLE_API']\n",
        "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
        "auth.set_access_token(access_key, access_secret)\n",
        "api = tweepy.API(auth, wait_on_rate_limit=True)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RY-no_lglrQb"
      },
      "source": [
        "search_words = [\"realDonaldTrump\"]\n",
        "search_words1 =[\"JoeBiden\"]\n",
        "date_since = '2020-11-16'"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K5alLGASjb0k",
        "outputId": "f6f4d7a2-fa25-4fa4-d9d2-3d5286352ad9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 441
        }
      },
      "source": [
        "#using tweepy.Cursor to format dataframe\n",
        "tweets = tweepy.Cursor(\n",
        "   api.search,\n",
        "   q = search_words,\n",
        "   lang = 'en',\n",
        "   since = date_since,\n",
        "   tweet_mode='extended' #attempt to retrieve full_text from truncated tweets\n",
        ").items(2500)\n",
        "\n",
        "tweet_details = [[tweet.full_text, tweet.user.screen_name, tweet.user.location] for tweet in tweets]\n",
        "Trump_Reviews = pd.DataFrame(data=tweet_details, columns=['text','user','location'])\n",
        "\n",
        "#pd.set_option('max_colwidth',800)\n",
        "Trump_Reviews.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    376\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 2.7, use buffering of HTTP responses\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 377\u001b[0;31m                 \u001b[0mhttplib_response\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetresponse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbuffering\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    378\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: getresponse() got an unexpected keyword argument 'buffering'",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-36-798882407cdf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m ).items(2500)\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mtweet_details\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfull_text\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocation\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtweets\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0mTrump_Reviews\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtweet_details\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcolumns\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'user'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'location'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-36-798882407cdf>\u001b[0m in \u001b[0;36m<listcomp>\u001b[0;34m(.0)\u001b[0m\n\u001b[1;32m      8\u001b[0m ).items(2500)\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mtweet_details\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfull_text\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscreen_name\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocation\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtweets\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0mTrump_Reviews\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtweet_details\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcolumns\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'user'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'location'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36m__next__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     47\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     48\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__next__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 49\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36mnext\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    195\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_index\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    196\u001b[0m             \u001b[0;31m# Reached end of current page, get the next page...\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 197\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_iterator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    198\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_index\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    199\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_index\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36mnext\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    106\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    107\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m \u001b[0;34m>=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mresults\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 108\u001b[0;31m             \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmax_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmax_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparser\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mRawParser\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    109\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    110\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'__self__'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tweepy/binder.py\u001b[0m in \u001b[0;36m_call\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    248\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 250\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    251\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m     \u001b[0;31m# Set pagination mode\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/tweepy/binder.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    188\u001b[0m                                                 \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    189\u001b[0m                                                 \u001b[0mauth\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mauth\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 190\u001b[0;31m                                                 proxies=self.api.proxy)\n\u001b[0m\u001b[1;32m    191\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    192\u001b[0m                     \u001b[0msix\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreraise\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mTweepError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mTweepError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Failed to send request: %s'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/sessions.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)\u001b[0m\n\u001b[1;32m    528\u001b[0m         }\n\u001b[1;32m    529\u001b[0m         \u001b[0msend_kwargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msettings\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 530\u001b[0;31m         \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprep\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0msend_kwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    531\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    532\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/sessions.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, **kwargs)\u001b[0m\n\u001b[1;32m    641\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    642\u001b[0m         \u001b[0;31m# Send the request\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 643\u001b[0;31m         \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0madapter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    645\u001b[0m         \u001b[0;31m# Total elapsed time of the request (approximately)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/requests/adapters.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, request, stream, timeout, verify, cert, proxies)\u001b[0m\n\u001b[1;32m    447\u001b[0m                     \u001b[0mdecode_content\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    448\u001b[0m                     \u001b[0mretries\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmax_retries\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 449\u001b[0;31m                     \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    450\u001b[0m                 )\n\u001b[1;32m    451\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    598\u001b[0m                                                   \u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout_obj\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    599\u001b[0m                                                   \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 600\u001b[0;31m                                                   chunked=chunked)\n\u001b[0m\u001b[1;32m    601\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    602\u001b[0m             \u001b[0;31m# If we're going to release the connection in ``finally:``, then\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    378\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m  \u001b[0;31m# Python 3\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    379\u001b[0m                 \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 380\u001b[0;31m                     \u001b[0mhttplib_response\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetresponse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    381\u001b[0m                 \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    382\u001b[0m                     \u001b[0;31m# Remove the TypeError from the exception chain in Python 3;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36mgetresponse\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   1371\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1372\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1373\u001b[0;31m                 \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbegin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1374\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mConnectionError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1375\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36mbegin\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    309\u001b[0m         \u001b[0;31m# read until we get a non-100 response\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    310\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 311\u001b[0;31m             \u001b[0mversion\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstatus\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreason\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_read_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    312\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mstatus\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mCONTINUE\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    313\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/http/client.py\u001b[0m in \u001b[0;36m_read_status\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    270\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    271\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_read_status\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 272\u001b[0;31m         \u001b[0mline\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_MAXLINE\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"iso-8859-1\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    273\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0m_MAXLINE\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    274\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mLineTooLong\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"status line\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/socket.py\u001b[0m in \u001b[0;36mreadinto\u001b[0;34m(self, b)\u001b[0m\n\u001b[1;32m    584\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    585\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 586\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mb\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    587\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    588\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_timeout_occurred\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mrecv_into\u001b[0;34m(self, buffer, nbytes, flags)\u001b[0m\n\u001b[1;32m   1010\u001b[0m                   \u001b[0;34m\"non-zero flags not allowed in calls to recv_into() on %s\"\u001b[0m \u001b[0;34m%\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1011\u001b[0m                   self.__class__)\n\u001b[0;32m-> 1012\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbytes\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1013\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1014\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_into\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnbytes\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, len, buffer)\u001b[0m\n\u001b[1;32m    872\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Read on closed or unwrapped SSL socket.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    873\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 874\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    875\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mSSLError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    876\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mSSL_ERROR_EOF\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msuppress_ragged_eofs\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.6/ssl.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, len, buffer)\u001b[0m\n\u001b[1;32m    629\u001b[0m         \"\"\"\n\u001b[1;32m    630\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mbuffer\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 631\u001b[0;31m             \u001b[0mv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbuffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    632\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    633\u001b[0m             \u001b[0mv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_sslobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T3Pub5Tarv45"
      },
      "source": [
        "Trump_reviews = tweet_df1\n",
        "Biden_reviews = Biden_Reviews"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yH4HcOqv-rxS"
      },
      "source": [
        "Trump_reviews.to_csv('trump.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "diwboxknD27f"
      },
      "source": [
        "Biden_reviews.to_csv('biden.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zNoiOWGxgQS8"
      },
      "source": [
        "#Visualizing text\n",
        "Trump_reviews['text'][10]\n",
        "Biden_reviews['text'][10]\n",
        "\n",
        "# Finding sentiments using TextBlob\n",
        "text_blob_object1 = TextBlob(Trump_reviews['text'][10])\n",
        "print(text_blob_object1.sentiment)\n",
        "text_blob_object2 = TextBlob(Biden_reviews['text'][500])\n",
        "print(text_blob_object2.sentiment)\n",
        "\n",
        "# Sentence  with zero polarity and subjectivity\n",
        "text_blob_object2 = TextBlob(Biden_reviews['text'][100])\n",
        "print(text_blob_object2.sentiment)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "H5O7MXpHjDU-"
      },
      "source": [
        "# Donald Trump\n",
        "def find_pol(review):\n",
        "    return TextBlob(review).sentiment.polarity\n",
        "\n",
        "Trump_reviews['Sentiment_Polarity'] = Trump_reviews['text'].apply(find_pol)\n",
        "Trump_reviews.tail()\n",
        "\n",
        "# Joe Biden\n",
        "def find_pol(review):\n",
        "    return TextBlob(review).sentiment.polarity\n",
        "\n",
        "Biden_reviews['Sentiment_Polarity'] = Biden_reviews['text'].apply(find_pol)\n",
        "Biden_reviews.tail()\n",
        "      "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UZSlbmbW6jG3"
      },
      "source": [
        "# Adding one more attribute for Expression Label\n",
        "# Donald Trump\n",
        "Trump_reviews['Expression Label'] = np.where(Trump_reviews['Sentiment_Polarity']>0,'positive', 'negative')\n",
        "Trump_reviews['Expression Label'][Trump_reviews.Sentiment_Polarity ==0] = \"Neutral\"\n",
        "Trump_reviews.tail()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BApjAEyi6t0g"
      },
      "source": [
        "# Joe Biden\n",
        "Biden_reviews['Expression Label'] = np.where(Biden_reviews['Sentiment_Polarity']>0,'positive', 'negative')\n",
        "Biden_reviews['Expression Label'][Biden_reviews.Sentiment_Polarity ==0] = \"Neutral\"\n",
        "Biden_reviews.tail()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DMmH-qW56VLw"
      },
      "source": [
        "# Analyzing Positive, Negative and Neutral replies on Trump's tweets.     \n",
        "new1 = Trump_reviews.groupby('Expression Label').count()\n",
        "x = list(new1['Sentiment_Polarity'])\n",
        "y = list(new1.index)\n",
        "tuple_list = list(zip(x,y))\n",
        "df = pd.DataFrame(tuple_list, columns=['x','y'])\n",
        "df['color'] = 'blue'\n",
        "df['color'][1] = 'red'\n",
        "df['color'][2] = 'green'\n",
        "fig = go.Figure(go.Bar(x=df['x'],\n",
        "                y=df['y'],\n",
        "                orientation ='h',\n",
        "                marker={'color': df['color']}))\n",
        "fig.update_layout(title_text='Trump\\'s Reviews Analysis' )\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QS1zQpw763xZ"
      },
      "source": [
        "# Analyzing Positive, Negative and Neutral replies on Biden's tweets\n",
        "new2 = Biden_reviews.groupby('Expression Label').count()\n",
        "x = list(new2['Sentiment_Polarity'])\n",
        "y = list(new2.index)\n",
        "tuple_list = list(zip(x,y))\n",
        "df = pd.DataFrame(tuple_list, columns=['x','y'])\n",
        "df['color'] = 'blue'\n",
        "df['color'][1] = 'red'\n",
        "df['color'][2] = 'green'\n",
        "fig = go.Figure(go.Bar(x=df['x'],\n",
        "                y=df['y'],\n",
        "                orientation ='h',\n",
        "                marker={'color': df['color']}))\n",
        "fig.update_layout(title_text='Biden\\'s Reviews Analysis' )\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GRthVsUt672K"
      },
      "source": [
        "# Dropping all the statements having zero polarity\n",
        "\n",
        "# Donald Trump      \n",
        "reviews1 = Trump_reviews[Trump_reviews['Sentiment_Polarity'] == 0.0000]\n",
        "reviews1.shape\n",
        "cond1 = Trump_reviews['Sentiment_Polarity'].isin(reviews1['Sentiment_Polarity'])\n",
        "Trump_reviews.drop(Trump_reviews[cond1].index, inplace = True)\n",
        "Trump_reviews.shape "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7UzlEEAp7CGI"
      },
      "source": [
        "# Joe Biden      \n",
        "reviews2 = Biden_reviews[Biden_reviews['Sentiment_Polarity'] == 0.0000]\n",
        "reviews2.shape\n",
        "cond2 = Biden_reviews['Sentiment_Polarity'].isin(reviews1['Sentiment_Polarity'])\n",
        "Biden_reviews.drop(Biden_reviews[cond2].index, inplace = True)\n",
        "Biden_reviews.shape\n",
        "\n",
        "# Let's make both the datasets balanced now. So we will just take 1000 rows from both datasets and drop rest of them."
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jo6Xw3Xn7EvU"
      },
      "source": [
        "# Donald Trump      \n",
        "np.random.seed(10)\n",
        "remove_n =324\n",
        "drop_indices = np.random.choice(Trump_reviews.index, remove_n, replace=False)\n",
        "df_subset_trump = Trump_reviews.drop(drop_indices)\n",
        "df_subset_trump.shape"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LI1eXgdP7JY6"
      },
      "source": [
        "# Joe biden            \n",
        "np.random.seed(10)\n",
        "remove_n =31\n",
        "drop_indices = np.random.choice(Biden_reviews.index, remove_n, replace=False)\n",
        "df_subset_biden = Biden_reviews.drop(drop_indices)\n",
        "df_subset_biden.shape\n",
        " \n",
        "# Data Visualiization\n",
        "\n",
        "# Donald Trump      \n",
        "sns.distplot(df_subset_trump['Sentiment_Polarity'])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i7pyy6Xd7f-T"
      },
      "source": [
        "sns.boxplot(df_subset_trump['Sentiment_Polarity'])\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1lYutjqq7Miv"
      },
      "source": [
        "# Joe Biden      \n",
        "sns.distplot(df_subset_biden['Sentiment_Polarity'])\n",
        "sns.boxplot(df_subset_biden['Sentiment_Polarity'])\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Vx9nXXYe7ueU"
      },
      "source": [
        "# Percentage count for Donald Trump\n",
        "count_1 = df_subset_trump.groupby('Expression Label').count()\n",
        "print(count_1)\n",
        "negative_per1 = (count_1['Sentiment_Polarity'][0]/1000)*100\n",
        "positive_per1 = (count_1['Sentiment_Polarity'][1]/1000)*100\n",
        "\n",
        "# Percentage count for Joe Biden      \n",
        "count_2 = df_subset_biden.groupby('Expression Label').count()\n",
        "print(count_2)\n",
        "negative_per2 = (count_2['Sentiment_Polarity'][0]/1000)*100\n",
        "positive_per2 = (count_2['Sentiment_Polarity'][1]/1000)*100"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "D1v3WDwC7yYl"
      },
      "source": [
        "# Analysis of Positive and Negative comments on both the handle\n",
        "\n",
        "Politicians = ['Donald Trump', 'Joe Biden']\n",
        "lis_pos = [positive_per1, positive_per2]\n",
        "lis_neg = [negative_per1, negative_per2]\n",
        "\n",
        "fig = go.Figure(data=[\n",
        "    go.Bar(name='Positive', x=Politicians, y=lis_pos),\n",
        "    go.Bar(name='Negative', x=Politicians, y=lis_neg)\n",
        "])\n",
        "# Change the bar mode\n",
        "fig.update_layout(barmode='group')\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "azrnb1mz8EYq"
      },
      "source": [
        "# Most Positive and Most Negative comments on both the Twitter handles\n",
        "\n",
        "# Donald Trump\n",
        "# Most positive replies      \n",
        "most_positive1 = df_subset_trump[df_subset_trump.Sentiment_Polarity == 1].text.head()\n",
        "pos_txt1 = list(most_positive1)\n",
        "pos1 = df_subset_trump[df_subset_trump.Sentiment_Polarity == 1].Sentiment_Polarity.head()\n",
        "pos_pol1 = list(pos1)\n",
        "fig = go.Figure(data=[go.Table(columnorder = [1,2], \n",
        "                               columnwidth = [50,400],\n",
        "                               header=dict(values=['Polarity','Positive Trump Tweets'],\n",
        "                               fill_color='turquoise',\n",
        "                               align='left'),\n",
        "               cells=dict(values=[pos_pol1, pos_txt1],\n",
        "                               fill_color='white',\n",
        "                               align='left'))])\n",
        " \n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kjOd3zxu8HsC"
      },
      "source": [
        "# Most Negative Replies      \n",
        "most_negative1 = df_subset_trump[df_subset_trump.Sentiment_Polarity == -1].text.head()\n",
        "neg_txt1 = list(most_negative1)\n",
        "neg1 = df_subset_trump[df_subset_trump.Sentiment_Polarity == -1].Sentiment_Polarity.head()\n",
        "neg_pol1 = list(neg1)\n",
        "fig = go.Figure(data=[go.Table(columnorder = [1,2],\n",
        "                               columnwidth = [50,400],\n",
        "                               header=dict(values=['Polarity','Negative Trump Replies'],\n",
        "                               fill_color='turquoise',\n",
        "                               align='left'),\n",
        "                cells=dict(values=[neg_pol1, neg_txt1],\n",
        "                           fill_color='white',\n",
        "                           align='left'))])\n",
        "\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gtPSFqhT8M8D"
      },
      "source": [
        "# Joe Biden\n",
        "# Most Positive replies      \n",
        "most_positive2 = df_subset_biden[df_subset_biden.Sentiment_Polarity == 1].text.tail()\n",
        "pos_txt2 = list(most_positive2)\n",
        "pos2 = df_subset_biden[df_subset_biden.Sentiment_Polarity == 1].Sentiment_Polarity.tail()\n",
        "pos_pol2 = list(pos2)\n",
        "fig = go.Figure(data=[go.Table(columnorder = [1,2],\n",
        "                               columnwidth = [50,400],\n",
        "                               header=dict(values=['Polarity','Most Positive Biden Tweets'],\n",
        "                               fill_color='turquoise',\n",
        "                               align='left'),\n",
        "                cells=dict(values=[pos_pol2, pos_txt2],\n",
        "                           fill_color='white',\n",
        "                           align='left'))])\n",
        "\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sOpdbsoh-HHI"
      },
      "source": [
        "most_negative2"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-oNui3CI8QFk"
      },
      "source": [
        "# Most negative replies\n",
        "most_negative2 = df_subset_biden[df_subset_biden.Sentiment_Polarity == -0.8].text.head()\n",
        "neg_txt2 = list(most_negative2)\n",
        "neg2 = df_subset_biden[df_subset_biden.Sentiment_Polarity == -1].Sentiment_Polarity.head()\n",
        "neg_pol2 = list(neg2)\n",
        "fig = go.Figure(data=[go.Table(columnorder = [1,2],\n",
        "                               columnwidth = [50,400],\n",
        "                               header=dict(values=['Polarity','Most Negative Replies on Biden\\'s handle'],\n",
        "                               fill_color='turquoise',\n",
        "                               align='left'),\n",
        "                cells=dict(values=[neg_pol2, neg_txt2],\n",
        "                           fill_color='white',\n",
        "                           align='left'))])\n",
        "\n",
        "fig.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3iDHjrH38THB"
      },
      "source": [
        "# WordCloud for Donald Trump      \n",
        "# Start with one review:\n",
        "text = str(df_subset_biden.text)\n",
        "# Create and generate a word cloud image:\n",
        "wordcloud = WordCloud(max_font_size=100, max_words=500, scale=10, relative_scaling=.6, background_color=\"black\", colormap = \"rainbow\").generate(text)\n",
        "# Display the generated image:\n",
        "plt.figure(figsize=(15,10))\n",
        "plt.imshow(wordcloud, interpolation='bilinear')\n",
        "plt.axis(\"off\")\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xfyH9xBP8X7M"
      },
      "source": [
        "# WordCloud for Joe Biden      \n",
        "# Start with one review:\n",
        "text = str(Biden_reviews.text)\n",
        "# Create and generate a word cloud image:\n",
        "wordcloud = WordCloud(max_font_size=100, max_words=500,scale=10,relative_scaling=.6,background_color=\"black\", colormap = \"rainbow\").generate(text)\n",
        "# Display the generated image:\n",
        "plt.figure(figsize=(15,10))\n",
        "plt.imshow(wordcloud, interpolation='bilinear')\n",
        "plt.axis(\"off\")\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XWMFiUqv8amR"
      },
      "source": [
        "# Comparison between negative comments on both      \n",
        "labels =  ['Negative_Trump', 'Negative_Biden'] \n",
        "sizes = lis_neg\n",
        "explode = (0.1, 0.1)\n",
        "fig1, ax1 = plt.subplots()\n",
        "ax1.pie(sizes, explode=explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle=90)\n",
        "ax1.set_title('Negative tweets on both the handles')\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9B7nGfBN8dEi"
      },
      "source": [
        "# Comparison between Positive comments on both      \n",
        "labels =  ['Positive_Trump', 'Positive_Biden'] \n",
        "sizes = lis_pos\n",
        "explode = (0.1, 0.1)\n",
        "fig1, ax1 = plt.subplots()\n",
        "ax1.pie(sizes, explode=explode, labels = labels, autopct = '%1.1f%%', shadow = True, startangle=90)\n",
        "ax1.set_title('Positive tweets on both the handles')\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}