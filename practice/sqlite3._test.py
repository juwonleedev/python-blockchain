import sqlite3
import pandas as pd

# sample.db라는 파일에 connection 만들기 (실제 폴더에 sample.db 파일 생성됨)
conn = sqlite3.connect('sample.db')

## pandas에서 csv 파일로 저장하는 방식과 동일하게 Dataframe 생성
df = pd.DataFrame()
df['seller'] = pd.Series(['tom', 'james', 'kaka'])
df['buyer'] = pd.Series(['pepe', 'alex', 'mike'])
df['amount'] = pd.Series([10,30,20])
df.to_sql('test_transaction',conn)

## 다시 connection(sample.db)의 test_transaction에서 SQL문으로 데이터를 불러온다
df = pd.read_sql_query("SELECT * FROM test_transaction", conn)
print(df)

# connection에 쿼리문 (test 테이블에서 seller='tom'인 데이터를 불러와라)
df = pd.read_sql_query("SELECT * FROM test_transaction where seller = 'tom", conn)
print(df)