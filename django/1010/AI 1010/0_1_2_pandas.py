import pandas as pd

"""
DataFrame
"""
data = {
    'Name': ['Alex', 'Bred', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [55.5, 90.3, 78.9],
}

df = pd.DataFrame(data)
print(df)
print()

# Series : DataFrame의 열(Column)
name_series = df['Name']
print(name_series)
print()

# Record 접근
# index 기반 접근
print(df.iloc[1])
print(df.iloc[0,0], df.iloc[0,2])
# label 기반 접근
print(df.loc[0, 'Name'], df.loc[0, 'Score'])

# 여러 열을 추출
print(df[['Name', 'Score']])
print()

# 정보 찾아보기
df.info()
print(df.describe())
print(df.shape)
print(df.columns.tolist())
print(df.index)
print()
# 상위 일부 가져오기
print(df.head(2))


"""
집계 기능
"""
print(df['Score'].mean())
print(df['Age'].max())
print(df.sort_values(by="Score"))

"""
다양한 타입의 데이터를 활용하여 DataFrame 만들기
"""
# 목표
data = {
    'Name': ['Alex', 'Bred', 'Chad'],
    'Age': [25, 30, 35],
    'Score': [55.5, 90.3, 78.9],
}

df = pd.DataFrame(data)

# 여러 딕셔너리에서 만들기
alex = {'Name': 'Alex', 'Age': 25, 'Score': 85.5}
brad = {'Name': 'Brad', 'Age': 30, 'Score': 90.3}
chad = {'Name': 'Chad', 'Age': 35, 'Score': 78.9}
# 각 딕셔너리가 레코드라고 생각하고 리스트로
df_from_dict = pd.DataFrame([alex, brad, chad])
print(df_from_dict)

# 여러 리스트에서 만들기
alex = ['Alex', 25, 85.5]
brad = ['Brad', 30, 90.3]
chad = ['Chad', 35, 78.9]
df_from_list = pd.DataFrame(
    [alex, brad, chad], 
    columns=['Name', 'Score', 'Age']
)


# numpy array에서 만들기
import numpy as np
nums = np.array([
    [25, 85.5],
    [30, 90.3],
    [35, 78.9],
])

# 나이와 점수로 DataFrame 만들기
df_from_ndarr = pd.DataFrame(nums, columns=['Age', 'Score'])
# 0번에 이름 추가하기
names = ['Alex', 'Brad', 'Chad']
df_from_ndarr.insert(0, 'Name', names)
print(df_from_ndarr)

# 시리즈 형변환
df_from_ndarr['Score'] = df_from_ndarr['Score'].astype(int)
print(df_from_ndarr)
