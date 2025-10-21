import numpy as np

"""
기본 행렬 생성 및 연산
"""

arr = np.array([1,2,3,4,5])
print(arr)

a = np.array([[1,2],[3,4]])
# print(a)
b = np.array([[4,3], [2,1]])
# print(b)
# print(a @ b)

# 다차원 배열 생성
arr_2d = np.array([[10,20,30],[40,50,60]])
print(arr_2d)

# 단위 행렬 다니엘형..?
x = np.eye(3)
print(x)

# 행렬의 원소를 인덱스를 바탕으로 변경하기
x[0,2] = 47     # 0행의 2열을 47로 변경
print(x)


"""
무작위 행렬 만들기
"""
arr_ran = np.random.randint(low=50, high=101, size=5)
print(arr_ran)

# 정규 분포 추출
std_ran = np.random.randn(3,3)
print(std_ran)


"""
연산 / 형변환
"""
id_3 = np.eye(3)
std_ran = np.random.randn(3,3)
# 다양한 차원에 대한 곱 / 내적(벡터 x 벡터)
z = np.dot(id_3, std_ran)
print(std_ran)
print(z)

# 각 원소의 형변환
id_bool = id_3.astype(bool)
id_bool = id_3.astype(int)
print(id_bool)

# 상수 곱 (스칼라 배)
x_float = id_3 * 1.1
print(x_float)


"""
벡터 연습 (numpy 활용법 추가)
"""
# 기본 벡터 생성
v = np.array([1,2,3])

# v를 반복 복제
v_repeated = np.tile(v, (3,1))
print(v_repeated)

# 다차원 행렬을 평탄화
v_flattened = v_repeated.flatten()
print(v_flattened)

# 균등한 간격을 가지는 일정 크기의 벡터를 생성
thetas = np.linspace(0, 2 * np.pi, 120)
# print(thetas)

# 각 원소에 삼각함수 적용
sin_thetas = np.sin(thetas)
print(sin_thetas)

"""
시각화 해보기
"""
import matplotlib.pyplot as plt
plt.plot(thetas, sin_thetas)
plt.title('sin curve')
plt.xlabel('theta (radians)')
plt.ylabel('sin(theta)')
plt.show()