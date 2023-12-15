# 기존 csv에 저장하고 다시 csv를 읽어오는 익숙한 방식
import pandas as pd

df = pd.DataFrame()
df['seller'] = pd.Series(['tom','james','kaka'])
df['buyer'] = pd.Series(['pepe', 'alex','mike'])
df['amount'] = pd.Series([10,30,20])
df.to_csv('sample_transaction.csv')
df = pd.read_csv('sample_transaction.csv', index_col=0)
print(df)

# 2. SQLite3로 저장하기

#package 불러오기
import sqlite3

## sample.db라는 파일에 connection 만들기 (실제 폴더에 sample.db 파일이 생성된다)
conn = sqlite3.connect('sample.db')

## 1번 방식과 동일하게 Dataframe 생성
df = pd.DataFrame()
df['seller'] = pd.Series(['tom','james','kaka'])
df['buyer'] = pd.Series(['pepe', 'alex','mike'])
df['amount'] = pd.Series([10,30,20])
## to_sql 함수 활용하여 connection(sample.db)의 test_transaction에 저장한다
df.to_sql('test_transaction', conn)

## 다시 connection(sample.db)의 test_transaction에서 SQL문으로 데이터를 불러온다
df = pd.read_sql_query("SELECT * FROM test_transaction", conn)
print(df)

# connection에 쿼리문 (test 테이블에서 seller = 'tom'인 데이터를 불러와라)를 사용해서 데이터 호출
df = pd.read_sql_query("SELECT * FROM test_transaction where seller = 'tom'", conn)