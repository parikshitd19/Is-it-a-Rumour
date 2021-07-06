import jsonlines
import json
import re
from Tweet_Info_Obj import *

FLAGS = re.MULTILINE | re.DOTALL

def extract_data(filepath):
    tweets_corpus=[]
    tweet_id=[]
    tweet_info=[]
    with jsonlines.open(filepath) as reader:
        for obj in reader:
            tweet_group=[]
            tweet_id.append(obj[0]['id'])
            t_info=[]
            for i in obj:
                tweet_group.append(i['text'])
                tobj=Tweet_Info_Obj(i['id'],i['retweet_count'],i['user']['followers_count'])
                t_info.append(tobj)
            tweets_corpus.append(tweet_group)
            tweet_info.append(t_info)

    return tweets_corpus,tweet_id,tweet_info

def get_labels(filename,ids):
    label_list=[]
    label_dict=json.load(open(filename))
    for _id in ids:
        label_list.append(label_dict.get(str(_id)))
    return label_list

def hashtag(text):
    text = text.group()
    hashtag_body = text[1:]
    if hashtag_body.isupper():
        result = "<hashtag> {} <allcaps>".format(hashtag_body.lower())
    else:
        result = " ".join(["<hashtag>"] + re.split(r"(?=[A-Z])", hashtag_body, flags=FLAGS))
    return result

def allcaps(text):
    text = text.group()
    return text.lower() + " <allcaps> " # amackcrane added trailing space


def tokenize(text):
    #This has been taken from https://gist.github.com/tokestermw/cb87a97113da12acb388 
    # Different regex parts for smiley faces
    eyes = r"[8:=;]"
    nose = r"['`\-]?"

    # function so code less repetitive
    def re_sub(pattern, repl):
        return re.sub(pattern, repl, text, flags=FLAGS)

    text = re_sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", "<url>")
    text = re_sub(r"@\w+", "<user>")
    text = re_sub(r"{}{}[)dD]+|[)dD]+{}{}".format(eyes, nose, nose, eyes), "<smile>")
    text = re_sub(r"{}{}p+".format(eyes, nose), "<lolface>")
    text = re_sub(r"{}{}\(+|\)+{}{}".format(eyes, nose, nose, eyes), "<sadface>")
    text = re_sub(r"{}{}[\/|l*]".format(eyes, nose), "<neutralface>")
    text = re_sub(r"/"," / ")
    text = re_sub(r"<3","<heart>")
    text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "<number>")
    text = re_sub(r"#\w+", hashtag)  # amackcrane edit
    text = re_sub(r"([!?.]){2,}", r"\1 <repeat>")
    text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2 <elong>")
    

    ## -- I just don't understand why the Ruby script adds <allcaps> to everything so I limited the selection.
    # text = re_sub(r"([^a-z0-9()<>'`\-]){2,}", allcaps)
    #text = re_sub(r"([A-Z]){2,}", allcaps)  # moved below -amackcrane

    # amackcrane additions
    text = re_sub(r"([a-zA-Z<>()])([?!.:;,])", r"\1 \2")
    text = re_sub(r"\(([a-zA-Z<>]+)\)", r"( \1 )")
    text = re_sub(r"  ", r" ")
    text = re_sub(r" ([A-Z]){2,} ", allcaps)
    
    return text.lower()

def preprocees_tweets(corpous):
    processed_corpous=[]
    for collection in corpous:
        processed_collection=[]
        for tweet in collection:
            processed_collection.append(tokenize(tweet))
        processed_corpous.append(processed_collection)
    return processed_corpous

def preprocees_tweets(corpous):
    processed_corpous=[]
    for collection in corpous:
        processed_collection=[]
        for tweet in collection:
            processed_collection.append(tokenize(tweet))
        processed_corpous.append(processed_collection)
    return processed_corpous