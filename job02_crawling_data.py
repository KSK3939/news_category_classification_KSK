# 파일명은 naver_news_section.csv로 해주세요.
# 컬럼명은 titles, category로 해주세요.
# 00님이 정치, 경제
# 01님이 사회, 문화
# 02님이 세계, IT
# 다 되면 PR 부탁합니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time

options = ChromeOptions()
options.add_argument('lang=ko_KR')
#options.add_argument('headless')

service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = options)

sections = [['World', '104'], ['IT', '105']]

df_titles = pd.DataFrame(columns = ['titles', 'category'])
for category, section_num in sections:
    url = 'https://news.naver.com/section/{}'.format(section_num)
    driver.get(url)
    time.sleep(1)
    button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]/a'
    for i in range(30):
        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(0.5)

#'//*[@id="newsct"]/div[4]/div/div[1]/div[20]/ul/li[5]/div/div/div[2]/a/strong'
#'//*[@id="newsct"]/div[4]/div/div[1]/div[20]/ul/li[6]/div/div/div[2]/a/strong'
#'//*[@id="newsct"]/div[4]/div/div[1]/div[21]/ul/li[2]/div/div/div[2]/a/strong'
#'//*[@id="newsct"]/div[4]/div/div[1]/div[3]/div/p'

    titles = []

    for i in range(1, 188):
        for j in range(1, 7):
            try:
                title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i, j)
                title = driver.find_element(By.XPATH, title_xpath).text

                titles.append(title)
                print(title)
            except:
                print('error', i, j)

    titles = list(dict.fromkeys(titles))
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category
    df_titles = pd.concat([df_titles, df_section_titles], ignore_index=True)

print(df_titles.head())
df_titles.info()
df_titles.to_csv('./data/naver_headline_news_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d')), index = False)