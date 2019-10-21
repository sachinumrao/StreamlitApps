import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = {}
    score = analyzer.polarity_scores(text)
    score.pop('compound')
    sentiment_map = {'pos':'Positive',
                    'neg': 'Negative',
                    'neu': 'Neutral'}
    sent = max(score, key=lambda key: score[key])
    return sentiment_map[sent]


# Create title and header for page
st.title('Sentment Analyzer')
st.header('What Do You Have in Mind...')

# Get text from user
txt = st.text_area('','')

sentiment = None

# Get Sentiment button
if st.button('Get Sentiment'):
    sentiment = get_sentiment(txt)

# Display sentiment in webpage
st.write('Sentiment:', sentiment)

# Ballons if sentiment is positive
if sentiment is 'Positive':
    st.balloons()

