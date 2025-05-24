import requests
from bs4 import BeautifulSoup
import string
import os
import re

base_url = input("Input the URL:\n> ")
HEADERS = {'Accept-Language': 'en-US,en;q=0.5'}
files_list = []


def create_file_name(title):
    title = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
    return f'{title}.txt'


def get_article_content(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_body = soup.find('div', {'class': 'c-article-body main-content'})
    if not article_body:
        article_body = soup.find('div', {'class': 'c-article-body'})
    if not article_body:
        article_body = soup.find('div', {'class': 'article__body cleared'})
    if article_body:
        return article_body.get_text(strip=True)
    else:
        return 'No content found.'


def main():
    pages = int(input('Enter the number of pages to search:\n>'))
    article_type = input('Enter the article type:\n>')
    cleaned_url = re.sub(r'([&?])page=\d+', '', base_url).rstrip('&?')
    for page in range(1, pages + 1):
        if '?' in cleaned_url:
            page_url = f'{cleaned_url}&page={page}'
        else:
            page_url = f'{cleaned_url}?page={page}'
        folder_name = f'Page_{page}'
        os.makedirs(folder_name, exist_ok=True)
        response = requests.get(page_url, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            article_type_tag = article.find('span', {'data-test': 'article.type'})
            if article_type_tag and article_type_tag.text.strip() == article_type:
                article_link = article.find('a', {'data-track-action': 'view article'})
                if article_link:
                    article_url = 'https://www.nature.com' + article_link.get('href')
                    article_title = article_link.text.strip()
                    file_name = create_file_name(article_title)
                    article_content = get_article_content(article_url)
                    file_path = os.path.join(folder_name, file_name)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(article_content)
                    files_list.append(file_name)
                else:
                    continue
    print(f"Saved articles: {files_list}")

if __name__ == "__main__":
    main()
