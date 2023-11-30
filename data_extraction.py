import requests
from bs4 import BeautifulSoup
import plotly.express as px
import nltk
from analysis import get_sentence_sentiment
from domain_knowlege.importatnt_urls import url_by_country

nltk.download("punkt")  # Download for sentence parsing

# Define URL list for iterating over
positive_counts = {}  # Use a dictionary to store counts for each country
negative_counts = {}

search_words = [
    "nova", "israel", "palestine", "idf", "hamas", "gaza",
    "conflict", "peace", "border", "negotiation", "security",
    "west bank", "jerusalem", "settlements", "ceasefire", "annexation",
    "two-state solution", "un", "human rights", "refugees", "blockade",
    "rockets", "intifada", "diplomacy", "occupied territories", "east jerusalem",
    "trump plan", "bds", "golan heights", "unrwa", "temple mount",
    "security fence", "al-aqsa mosque", "haganah", "yom kippur war", "oslo accords",
    "hezbollah", "iron dome", "west bank barrier", "right of return", "operation cast lead",
    "mossad", "fatah", "united nations security council", "middle east peace process", "sabra and shatila massacre",
    "hebron", "beirut", "lebanon", "hizbullah", "rafah", "jericho",
    "syria", "egypt", "jordan", "arab league", "camp david accords",
    "jerusalem embassy act", "gaza strip withdrawal", "nakba", "palestinian authority", "plo",
    "israeli settlements", "yitzhak rabin", "golda meir", "ariel sharon", "menachem begin",
    "david ben-gurion", "yasser arafat", "hussein of jordan", "sadat", "balfour declaration",
    "palestinian liberation organization", "haganah", "hamas charter", "palestinian national charter", "western wall"
]

for country, urls in url_by_country.items():  # Assuming url_by_country is a dictionary
    positive_count = 0
    negative_count = 0

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.text
            sentences = nltk.sent_tokenize(text)

            for sentence in sentences:
                lower_sentence = sentence.lower()

                for word in search_words:
                    if word in lower_sentence:
                        sentiment = get_sentence_sentiment(lower_sentence)
                        if sentiment == "Positive":
                            positive_count += 1
                        if sentiment == "Negative":
                            negative_count += 1

    positive_counts[country] = positive_count
    negative_counts[country] = negative_count

# Create a bar chart for positive sentiment counts
fig_positive = px.bar(
    x=list(positive_counts.keys()),
    y=list(positive_counts.values()),
    title="Positive Sentiment Counts by Country"
)
fig_positive.show()

# Create a bar chart for negative sentiment counts
fig_negative = px.bar(
    x=list(negative_counts.keys()),
    y=list(negative_counts.values()),
    title="Negative Sentiment Counts by Country"
)
fig_negative.show()
