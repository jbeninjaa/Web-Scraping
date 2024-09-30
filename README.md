# Project: Automatic Wikipedia Summary Generator (Web Scraping and NLP Project)

## Objective

The goal of this project is to scrape full Wikipedia articles and generate automatic summaries using Natural Language Processing (NLP) techniques. The project utilizes the Python-NLTK Library to handle the summarization and text processing.

## Features

- Web Scraping: The program fetches full Wikipedia articles using requests and BeautifulSoup libraries.
- Text Summarization: Using NLP methods from the NLTK library, the scraped content is processed and summarized into concise information.

## Project Overview

This project automates the process of extracting and summarizing large Wikipedia articles to deliver a shorter, more manageable summary. By extracting the content of the article through its URL.

## Libraries and Tools Used

- requests: For sending HTTP requests to Wikipedia pages.
- BeautifulSoup: For parsing and navigating the HTML content of Wikipedia articles.
- NLTK: For performing Natural Language Processing and text summarization.
- IDE: Jupyter Notebook via VS Code Extensions
- Python: Programming Language

## How It Works

- The script scrapes a specified Wikipedia article using requests and BeautifulSoup.
- The text is cleaned and processed by removing unnecessary HTML elements.
- The cleaned text is tokenized and summarized using the NLTK library's NLP functions.

## Future Enhancements

- Clean the extracted data (could use some more)
- Implement additional summarization algorithms for better summaries.
- Develop a web interface/GUI for easier usage