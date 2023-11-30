from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")

def get_sentence_sentiment(sentence):
    # Initialize the VADER sentiment analysis tool
    analyzer = SentimentIntensityAnalyzer()

    # Input sentence
    # sentence = "I love this product! It's amazing."

    # Compute the sentiment scores
    sentiment_scores = analyzer.polarity_scores(sentence)

    # Determine the sentiment label based on the scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Print the sentiment scores and label
    print("Sentiment Scores:", sentiment_scores)
    if sentiment == "Positive":
        print("Sentiment:", sentiment)

    if sentiment == "Negative":
        print(f"\033[91m{sentiment}\033[0m")

    return sentiment







