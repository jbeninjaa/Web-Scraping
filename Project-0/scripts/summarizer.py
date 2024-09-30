# import libraries 
import requests
from bs4 import BeautifulSoup

# text processing
import nltk  
from nltk.corpus import stopwords                               
from nltk.tokenize import word_tokenize, sent_tokenize 
nltk.download('stopwords')
nltk.download('punkt_tab')

## make an HTTP request using (requests)
wikipedia_url = "https://en.wikipedia.org/wiki/Machine_learning"

response = requests.get(wikipedia_url)

# check for errors
if(response.status_code == 200):
    print('Page Fetched Successfully')
else:
    print('Failed to Fetch Page')

print("hello world!")

# parse request using beautifulsoup html parser
page_content = response.text
soup = BeautifulSoup(page_content, 'html.parser')


# identify and segregate needed data
page_title = soup.find('h1', id='firstHeading').text

page_content = soup.find('div', id='bodyContent')

## page headings 
page_headings = page_content.find_all('div', class_='mw-heading')
# for heading in page_headings:
#     # print(heading.text)

## page body
paragraph_string = ""
for article in page_body:
    paragraph_string = paragraph_string + article.text

paragraph_string

# text processing
stopWords = set(stopwords.words('english'))
words = word_tokenize(paragraph_string)

print(words)