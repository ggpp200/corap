# -*- coding: utf-8 -*-
"""_Pandas 한번에 제대로 배우기.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zjTHolVTcYPG3iZKyP9G0elmBtpZThsE

# Pandas 한번에 제대로 배우기

---
"""

import numpy as np

import pandas as pd
pd.__version__
# 버전확인



"""## Pandas 객체

### Series 객체
"""

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
s
# 시리즈는 한줄짜리 데이터 집합

s.values
# 값만 볼때 사용

s.index
# 인덱스 범위 출력, 현재는 range로 0~4까지 표현

s[1]
# 인덱스로 접근

s[1:4]
# 슬라이싱도 가능

s = pd.Series([0.  , 0.25, 0.5 , 0.75, 1.0], index = ['a', 'b', 'c', 'd', 'e'])
s
# 인덱스 지정 가능

'b' in s
# 파이선의 in 함수 사용가능

s =pd.Series([0.  , 0.25, 0.5 , 0.75, 1.0], index = ['2', '4', '6', '8', '10'])
s

s[2:]

s.unique()
# 유니크한 값만 출력

s.value_counts()
# 각 밸류 갯수 세기

s.isin([0.25, 0.75])
# 특정 숫자가 안에 있는게 확인되면 True

pop_dict = {'서울특별시' : 9720846,
            '부산광역시': 3404423,
            '인천광역시': 2947217,
            '대구광역시': 2427954,
            '대전광역시': 147105,
            '광주광역시': 1455048}
population = pd.Series(pop_dict)
population
# 정보를 dictionary로 만들기

population['서울특별시']
# 인덱싱

population['서울특별시': '인천광역시']
# 인덱싱2

"""### DataFrame 객체

데이터 프레임은 2차원 배열이라고 생각하면 됨
"""

pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}])
# 데이터프레임 예제(이때, 각 C와 D에 누락값 NaN으로 표기)

pd.DataFrame(np.random.rand(5, 5), columns = ['A', 'B', 'C', 'D', 'E'], index = [1, 2, 3, 4, 5])
# colums와 index 수정

male_dict = {'서울특별시' : 4732275,
            '부산광역시': 1668618,
            '인천광역시': 1476813,
            '대구광역시': 1198815,
            '대전광역시': 734441,
            '광주광역시': 720060}
male = pd.Series(male_dict)
male
# 남자 인구수 정의 및 출력

female_dict = {'서울특별시' : 4988571,
            '부산광역시': 1735805,
            '인천광역시': 1470404,
            '대구광역시': 1229139,
            '대전광역시': 736599,
            '광주광역시': 734988}
female = pd.Series(female_dict)
female
# 여자 인구수 정의 및 출력

korea_df = pd.DataFrame({'인구수':population,
                        '남자인구수':male,
                        '여자인구수': female})
korea_df
# 3개의 Series 를 DataFrame으로 나타내기

korea_df.index
# 인덱스 내역 보기



korea_df.columns
# columns 내역보기

korea_df['서울특별시':'인천광역시']
#df슬라이싱

"""### Index 객체

Index           일반적인 index로 Numpy 배열의 축

int64index      정수 값을 위한 index

Multiindex      단일 축에 여러 단계 색인을 표현하는 계층적 idnex 객체

Datetimeindex   Numpy의 datetime64 타입으로 타임스탬프 저장

Periodindex     기간 데이터를 위한 index
"""

idx = pd.Index([2,4,6,8,10])
idx
# 인덱스 Series객체 생성

idx[1:2:2]
#슬라이싱 연습1



idx[::-1]
# 슬라이싱(역)

idx[-1::]
#슬라이싱 연습(마지막 글자)

idx[::2]

print(idx)
print(idx.size)
print(idx.shape)
print(idx.ndim)
print(idx.dtype)
# 인덱스 출력
# 인덱스 사이즈
# 인덱스 1차원 shape
# ndim은 배열의 차수이므로 1차원 이므로 1
# 데이터 타입 인트

"""#### Index 연산

append                색인 객체를 추가한 새로운 색인 반환

difference            색인의 차집합 반환

intersection          색인의 교집합 반환

union                 색인의 합집합 반환(중복 삭제)


isin                  색인이 존재하는지 여부를 불리언 배열로 반환

delete                색인이 삭제된 새로운 색인 반환

drop                  값이 삭제된 새로운 색인 반환

insert                색인이 추가된 새로운 색인 반환

is_monotonic          색인이 단조성을 가지면 True

is_unique             중복되는 색인이 없다면 True

unique                색인에서 중복되는 요소를 제거하고 유일한 값만 반환
"""

idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])

print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1 - idx2)
# 추가, 차집합, 차집합



print(idx1.intersection(idx2))
print(idx1 & idx2)
print(idx.union(idx2))
# 교집합, 교집합, 합집합



print(idx1 | idx2)
print(idx1.delete(0))
print(idx1.drop(1))
print(idx1 ^ idx2)
# 합집합, 삭제, 삭제, 여집합

"""---

## 인덱싱(Indexing)
"""

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd', 'e'])
s

s['b']

'b' in s

s.keys()

list(s.items())

s['f'] = 1.25
s

s['a':'d']

s[0:4]

s[(s > 0.4) & (s < 0.8)]

s[['a', 'c', 'e']]

"""### Series 인덱싱"""

s = pd.Series(['a', 'b', 'c', 'd', 'e'], index = [1, 3, 5, 7, 9])

s[1]
# 직접 지정한 인덱스사용

s[2:4]

s.iloc[1]
# 직접 지정한 인덱스 말고 원래 숫자인 정수값으로 접근

s.iloc[2:4]

s.reindex(range(10))
# reindex는 새로운 인덱스 구축, 이때 없는 값은 NaN 표기됨

s.reindex(range(10), method = 'bfill')
# bfill은 before fill로 전값으로 채움



"""### DataFrame 인덱싱

"""



































"""### 다중 인덱싱(Multi Indexing)

* 1차원의 Series와 2차원의 DataFrame 객체를 넘어 3차원, 4차원 이상의 고차원 데이터 처리
* 단일 인덱스 내에 여러 인덱스를 포함하는 다중 인덱싱

#### 다중 인덱스 Series
"""

































"""#### 다중 인덱스 생성"""



















"""#### 인덱싱 및 슬라이싱"""





















"""#### 다중 인덱스 재정렬"""























"""## 데이터 연산"""





















"""### 연산자 범용 함수

#### add()
"""











"""#### sub() / subtract()"""













"""#### mul() / multply()



"""













"""#### truediv() /  div() / divide() / floordiv()"""



















"""#### mod()"""









"""#### pow()"""













"""### 정렬(Sort)"""

















"""### 순위(Ranking)

"""









"""### 고성능 연산"""









































"""## 데이터 결합

### Concat() / Append()
"""

































"""### 병합과 조인"""

























































"""## 데이터 집계와 그룹 연산

#### 집계 연산(Aggregation)
"""





































"""### GroupBy 연산"""













































"""### 피벗 테이블(Pivot Table)

"""













"""### 범주형(Categorical) 데이터

"""















































"""## 문자열 연산

#### 문자열 연산자
"""









"""#### 기타 연산자

"""









"""#### 정규표현식

"""





"""## 시계열 처리"""









"""#### 시계열 데이터 구조

"""





















"""### 시계열 기본"""



















































"""### 주기와 오프셋

"""













"""### 시프트(Shift)"""













"""### 시간대 처리

* 국제표준시(Coordinated Universal Time, UTC)를 기준으로 떨어진 거리만큼 오프셋으로 시간대 처리
* 전 세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리인 `pytz` 사용
"""

















































"""### 기간과 기간 연산"""



















































"""### 리샘플링(Resampling)

* 리샘플링(Resampling): 시계열의 빈도 변환
* 다운샘플링(Down sampling): 상위 빈도 데이터를 하위 빈도 데이터로 집계
* 업샘플링(Up sampling): 하위 빈도 데이터를 상위 빈도 데이터로 집계
"""





































"""### 무빙 윈도우(Moving Window)"""























"""## 데이터 읽기 및 저장

### 텍스트 파일 읽기/쓰기
"""

























































"""### 이진 데이터 파일 읽기/쓰기"""





























"""## 데이터 정제

### 누락값 처리

* 대부분의 실제 데이터들은 정제되지 않고 누락값들이 존재
* 서로 다른 데이터들은 다른 형태의 결측을 가짐
* 결측 데이터는 `null`, `NaN`, `NA`로 표기

#### None: 파이썬 누락 데이터
"""





"""#### NaN: 누락된 수치 데이터"""





















"""#### Null 값 처리

"""







































"""### 중복 제거"""







"""### 값 치환"""









"""## 참고문헌

* Pandas 사이트: https://pandas.pydata.org/
* Jake VanderPlas, "Python Data Science Handbook", O'Reilly
* Wes Mckinney, "Python for Data Analysis", O'Reilly
"""