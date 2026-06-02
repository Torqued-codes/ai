from textblob import TextBlob

class SentimentAnalyzer:
    @staticmethod
    def get_sentiment(text):
        
        score = TextBlob(text).sentiment.polarity
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'