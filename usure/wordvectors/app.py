import logging
import time 
from usure.wordvectors.infrastructure import FbWord2VecDAO, TwitterWord2VecDAO
from usure.wordvectors.vectorizerfabric import VectorizerFabric


logging.basicConfig(level=logging.INFO)
vectorizerfabric = VectorizerFabric()
fbword2vecdao = FbWord2VecDAO()
twitterword2vecdao = TwitterWord2VecDAO()

def run_fb_smallwindow():
    vectorizer = vectorizerfabric.create_fb_bigwindow()
    vectorizer.feed()
    print(len(vectorizer.w2v.wv.vocab))
    print(vectorizer.w2v.epochs)
    logging.info(f"Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    vectorizer.train()
    logging.info(f"Finish time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    fbword2vecdao.save_model(vectorizer.w2v)

def run_tw_smallwindow():
    vectorizer = vectorizerfabric.create_twitter_smallwindow()
    vectorizer.feed()
    print(len(vectorizer.w2v.wv.vocab))
    print(vectorizer.w2v.epochs)
    logging.info(f"Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    vectorizer.train()
    logging.info(f"Finish time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    twitterword2vecdao.save_model(vectorizer.w2v)

def run_tw_bigwindow():
    vectorizer = vectorizerfabric.create_twitter_bigwindow()
    vectorizer.feed()
    print(len(vectorizer.w2v.wv.vocab))
    print(vectorizer.w2v.epochs)
    logging.info(f"Starting time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    vectorizer.train()
    logging.info(f"Finish time:{time.strftime('%H:%M:%S', time.localtime(time.time()))}")
    twitterword2vecdao.save_model(vectorizer.w2v)

if __name__ == "__main__":
    run_tw_bigwindow()