import seaborn as sns
import numpy as np
import pandas as pd
from tqdm import tqdm


df = sns.load_dataset('diamonds')
df.info()
print(df.describe())

print()
categorical_cols = df.select_dtypes(include=['category']).columns.tolist()
continuous_cols = df.select_dtypes(include=['number']).columns.tolist()
print(categorical_cols)
print(continuous_cols)

print()
# 연속현 변수들만 뽑아서 저장한다.
X_raw = df[continuous_cols].values

# 해당 변수들의 평균을 구한다.
mu = X_raw.mean(axis=0)
# 해당 변수들의 표준편차를 구한다.
std = X_raw.std(axis=0)

# 표준편차가 0이 될 경우 바꿔준다.
# 1. 1로 바꾸거나
std = np.where(std == 0, 1.0, std)
# 2. 아주 작은 값으로 바꾸거나
epsilon = 1e-8
std = np.where(std == 0, epsilon, std)

# 표준화된 X 값들을 구한다.
X_norm = (X_raw - mu) / std
print(X_norm)


# 정규방정식으로 theta 만들기
# 계산의 편의를 위해 X_norm을 DataFrame으로
X_df = pd.DataFrame(X_norm, columns=continuous_cols)

# feature와 label의 분리
X = X_df.drop(labels='price', axis=1).values
y = X_df['price'].values

# 절편항을 추가
m, n = X_norm.shape
X_b = np.c_[np.ones((m, 1)), X_norm]


# theta
theta = np.zeros(n+1)
# 학습률 : 현재 지점에서 어느정도 이돌할지
alpha = 0.01
# 반복 횟수
iterations = 1000

# 비용 계산 결과 기록
loss_history = []

# 정해진 iterations만큼 반복
for i in tqdm(range(iterations)):
    # 현재 theta에 대한 예측값을 계산하고
    y_pred = (X_b @ theta).flatten()

    # 예측값에 대하여 MSE 계산
    error = y_pred - y
    mse = np.mean(error ** 2)
    loss_history.append(mse)

    # MSE를 바탕으로 경사를 계산
    gradient = (2/m) * X_b.T @ error

    # 경사를 바탕으로 theta를 갱신
    theta = alpha * gradient

import matplotlib.pyplot as plt
print("최종 θ:", theta.flatten())
print("최종 MSE:", loss_history[-1])

plt.plot(loss_history)
plt.xlabel("Iteration", size="large")
plt.ylabel("Mean Squared Error", size="large")
plt.title("Loss Curve", size="large")
plt.show()
