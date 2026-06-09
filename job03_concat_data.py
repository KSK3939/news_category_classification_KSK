import pandas as pd

df = pd.read_csv('data/news_titles.csv')
print(df.head())

df_temp = pd.read_csv('data/naver_headline_news_economy.csv')
print(df_temp.head())
df = pd.concat([df_temp, df], ignore_index = True)

df_temp = pd.read_csv('data/naver_headline_news_exepct_economy.csv')
print(df_temp.head())
df = pd.concat([df_temp, df], ignore_index = True)

df_temp = pd.read_csv('data/naver_headline_news_20260609.csv')
print(df_temp.head())
df = pd.concat([df_temp, df], ignore_index = True)

df.info()
df = df.drop_duplicates()

print(df.category.value_counts())
print(df.isnull().sum())
df.info()
df.to_csv('./data/news_titles_add.csv', index = False)