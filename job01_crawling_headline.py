from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()

#'https://news.naver.com/section/100'  정치
#'https://news.naver.com/section/101'  경제
#'https://news.naver.com/section/102'  사회
#'https://news.naver.com/section/103'  문화
#'https://news.naver.com/section/105'  IT
#'https://news.naver.com/section/104'  세계

for i in range(6):
    url = 'https://news.naver.com/section/10{}'.format(i)
    resp = requests.get(url)
    # print(list(resp))
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup)
    title_tag = soup.select('.sa_text_strong')
    print(title_tag)
    titles = []
    for title in title_tag:
        titles.append(title.text)
    print(titles)
    df_section_titles = pd.DataFrame(titles, columns = ['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], ignore_index = True)
print(df_titles.head())
df_titles.info()
df_titles.to_csv('./data/naver_headline_news_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d')), index = False)