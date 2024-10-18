import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report


nltk.download('stopwords')
nltk.download('punkt')


def preprocess(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)


df = pd.read_csv('/content/sentiment_analysis.csv')


df['processed_text'] = df['text'].apply(preprocess)


df['textblob_polarity'] = df['processed_text'].apply(lambda text: TextBlob(text).sentiment.polarity)


polarity = ctrl.Antecedent(np.arange(-1, 1.1, 0.1), 'polarity')
sentiment = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'sentiment')


polarity['negative'] = fuzz.trimf(polarity.universe, [-1, -1, 0])
polarity['neutral'] = fuzz.trimf(polarity.universe, [-0.5, 0, 0.5])
polarity['positive'] = fuzz.trimf(polarity.universe, [0, 1, 1])

sentiment['negative'] = fuzz.trimf(sentiment.universe, [0, 0, 0.3])
sentiment['neutral'] = fuzz.trimf(sentiment.universe, [0.2, 0.5, 0.7])
sentiment['positive'] = fuzz.trimf(sentiment.universe, [0.5, 1, 1])

rule1 = ctrl.Rule(polarity['positive'], sentiment['positive'])
rule2 = ctrl.Rule(polarity['negative'], sentiment['negative'])
rule3 = ctrl.Rule(polarity['neutral'], sentiment['neutral'])

sentiment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sentiment_sim = ctrl.ControlSystemSimulation(sentiment_ctrl)

fuzzy_sentiments = []
for polarity_score in df['textblob_polarity']:
    sentiment_sim.input['polarity'] = polarity_score
    try:
        sentiment_sim.compute()
        fuzzy_sentiments.append(sentiment_sim.output['sentiment'])
    except:
        fuzzy_sentiments.append(np.nan)  

df['fuzzy_sentiment_score'] = fuzzy_sentiments


df['fuzzy_sentiment_score'].fillna(0.5, inplace=True)

def map_sentiment(score):
    if score <= 0.4:
        return 'negative'
    elif score >= 0.6:
        return 'positive'
    else:
        return 'neutral'

df['fuzzy_sentiment'] = df['fuzzy_sentiment_score'].apply(map_sentiment)

report = classification_report(df['sentiment'], df['fuzzy_sentiment'], target_names=['negative', 'neutral', 'positive'])
print(report)
polarity.view()
sentiment.view()
