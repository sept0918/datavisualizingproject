#요일별 순위 상위 10개의 태그
top_10_by_day = nweb.groupby('day').apply(lambda x: x.nsmallest(10, 'rank')).reset_index(drop=True)
#시리즈를 리스트로 변경
tags1 = [tags.split(' ') for tags in list(top_10_by_day['tags'])] 
import itertools
tags2 = list(itertools.chain.from_iterable(tags1))
#순위 상위 10개의 최빈 키워드 
df_tags1 = pd.DataFrame({'tags' : tags2})
df_tags1['count']= df_tags1['tags'].str.len()
tagcount = df_tags1.groupby('tags', as_index=False).agg(n=('tags','count')).sort_values('n', ascending=False)
tagcount.head(10)

#요일별 순위 하위 10개의 태그
bottom_10_by_day = nweb.groupby('day').apply(lambda x: x.nlargest(10, 'rank')).reset_index(drop=True)
#시리즈를 리스트로 변경
tags3 = [tags.split(' ') for tags in list(bottom_10_by_day ['tags'])]
tags4 = list(itertools.chain.from_iterable(tags3))
#순위 하위 10개의 최빈 키워드
df_tags2 = pd.DataFrame({'tags' : tags4})
bottomcount = df_tags1.groupby('tags', as_index=False).agg(n=('tags','count')).sort_values('n', ascending=False)
bottomcount.head(10)

#시각화
fig1 = px.bar(tagcount.head(10), x='tags', y='n',
             title='상위 10개 웹툰에서 가장 많이 나타나는 키워드 Top 10',
             color='n',  # 색상을 빈도수에 따라 변경
             color_continuous_scale=color_scale)

fig2 = px.bar(bottomcount.head(10), x='tags', y='n',
             title='하위 10개 웹툰에서 가장 많이 나타나는 키워드 Top 10',
             color='n',  # 색상을 빈도수에 따라 변경
             color_continuous_scale=color_scale)

# 두 개의 데이터프레임을 병합하여 겹치는 키워드만 선택
merged_df = pd.merge(bottomcount.head(10), tagcount.head(10), on='tags', how='inner')

# 겹치는 키워드에 대한 바 차트
fig3 = px.bar(merged_df, x='tags', y=['n_x', 'n_y'], 
              title='상위 10개 웹툰과 하위 10개 웹툰에서 겹치는 키워드 Top 10',
              color_discrete_sequence=color_scale)

# x 및 y 축의 제목을 설정
fig1.update_xaxes(title_text='키워드')
fig1.update_yaxes(title_text='빈도수')

fig2.update_xaxes(title_text='키워드')
fig2.update_yaxes(title_text='빈도수')

fig3.update_xaxes(title_text='키워드')
fig3.update_yaxes(title_text='빈도수')

# 서브플롯을 생성하여 세 개의 그래프를 나란히 표시
subfig = make_subplots(rows=1, cols=3, subplot_titles=['상위 10개 웹툰', '하위 10개 웹툰', '겹치는 키워드'])
subfig.add_trace(fig1['data'][0], row=1, col=1)
subfig.add_trace(fig2['data'][0], row=1, col=2)
subfig.add_trace(fig3['data'][0], row=1, col=3)

# 전체 레이아웃 설정
subfig.update_layout(title='키워드 비교', showlegend=False)
subfig.show()

#키워드와 순위의 상관관계
import plotly.express as px

# 색상 설정
color_scale = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
               '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# 상관관계를 시각화하는 산점도 그래프
scatter_fig = px.scatter(merged_df, x='n_x', y='n_y', text='tags',
                         title='키워드와 순위 간의 상관관계',
                         color_discrete_sequence=color_scale)

# x 및 y 축의 제목
scatter_fig.update_xaxes(title_text='하위 10개 웹툰 빈도수')
scatter_fig.update_yaxes(title_text='상위 10개 웹툰 빈도수')

scatter_fig.update_traces(textposition='top center')
scatter_fig.show()

#년도별 키워드 정리
nweb_20 = nweb[nweb['starting_year'] == 20]
list(nweb_20['tags'])
tags20= [tags.split(' ') for tags in list(nweb_20['tags'])]
import itertools
tags20 = list(itertools.chain.from_iterable(tags20))
df_tags20 = pd.DataFrame({'tags' : tags20})
df_tags20['count']= df_tags20['tags'].str.len()
tagcount20 = df_tags20.groupby('tags', as_index=False).agg(n=('tags','count')).sort_values('n', ascending=False)

#20년, 21년, 22년, 23년 반복
merged_df = count20.merge(count21, on='tags', how='inner')
merged_df = count20.merge(count22, on='tags', how='inner')
df = count20.merge(count23, on='tags', how='inner')

#시각화
df = pd.DataFrame(data)

# 데이터를 'tags' 열을 기준으로 년도 열과 값 열로 변환
df_melted = df.melt(id_vars=['tags'], var_name='year', value_name='count')

# 그래프 생성
fig = px.line(df_melted, x='year', y='count', color='tags', title='년도별 키워드 변화', 
              text='count')
fig.update_traces(textposition='top right')
fig.update_xaxes(title_text='년도')
fig.update_yaxes(title_text='빈도수')

fig.show()

#656개 모든 웹툰의 키워드 분석
list(nweb['tags'])
totaltags= [tags.split(' ') for tags in list(nweb['tags'])]
import itertools
tagst = list(itertools.chain.from_iterable(totaltags))
df_tagst = pd.DataFrame({'tags' : tagst})
df_tagst['count']= df_tagst['tags'].str.len()
tagcountt = df_tagst.groupby('tags', as_index=False).agg(n=('tags','count')).sort_values('n', ascending=False)

#시각화
fig = px.pie(
    tagcountt.head(20),
    values='n',
    names='tags',
    title=' Top 20 키워드의 빈도수',
)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

#워드클라우드
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family'    : 'Malgun Gothic',  # 한글 폰트 설정
                     'figure.dpi'     : '120',            # 해상도 설정
                     'figure.figsize' : [6.5, 6]})        # 가로 세로 크기 설정

font="C:\Windows\Fonts\HMFMPYUN.TTF" #폰트 경로

df_word = tagcountt.query('n >= 2')
df_word = df_word.sort_values('n', ascending=False)
df_word = df_word
dic_nouns = df_word.set_index('tags').to_dict()['n']
from wordcloud import WordCloud

import PIL
icon = PIL.Image.open('cloud.png') #다운받은 마스크 이미지 불러오기

img = PIL.Image.new('RGB', icon.size, (255, 255, 255))
img.paste(icon, icon)
img = np.array(img)
# 워드 클라우드 출력
wc = WordCloud(random_state = 1234,         # 난수 고정
               font_path = font,            # 폰트 설정
               width = 400,                 # 가로 크기
               height = 400,                # 세로 크기
               background_color = 'white',
               mask = img)
img_wordcloud = wc.generate_from_frequencies(dic_nouns)
plt.figure(figsize = (10, 10))  # 가로, 세로 크기 설정
plt.axis('off')                 # 테두리 선 없애기
plt.imshow(img_wordcloud) 

#관심수 시리즈 전처리 
import re
nweb['like']= nweb['like'].map(lambda x: re.sub('[,]', '', x)) #컴마 삭제
nweb['like']= nweb['like'].astype(int) #인트로 타입 변경

#관심수와 순위 상관관계 
nweb[['rank', 'like']].corr()

#상관관계 시각화
import plotly.express as px

fig = px.scatter(nweb, x='rank', y='like', title='순위와 관심수 산점도')
fig.update_layout(xaxis_title='Rank', yaxis_title='Like')

fig.show()
