import pandas as pd
import numpy as np
monday = pd.read_excel('monday.xlsx', index_col = 0)
monday.columns=['title','author','rate','tags','like','starting_date'] #컬럼 이름 변경
monday['day']='mon' #요일 추가
monday['rank']=range(1,98) #순위 추가
monday['starting_year'] = monday['starting_year'].map(lambda x: x[:2]) #웹툰 시작일 년도만 표시
#키워드 분석을 위한 전처리 작업
monday['tags'] = monday['tags'].map(lambda x: re.sub('[\n]',' ',x))
monday['tags'] = monday['tags'].map(lambda x: re.sub('[#]','',x))

#월요일부터 일요일까지 각각의 데이터프레임에 위의 과정을 반복

#7개의 데이터 프레임을 하나로 취합
n_web = pd.concat([monday,tuesday,wednesday,thursday, friday, saturday, sunday])
