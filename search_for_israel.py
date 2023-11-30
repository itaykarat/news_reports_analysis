import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
from domain_knowlege.importatnt_urls import url_by_country

for country,urls in url_by_country.items():
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text_data = soup.text
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

            # Plot the word cloud
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title(f"word cloud for {country} - {url}")
            plt.show()


