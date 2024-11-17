import geo.utils as utils

a, b = 3, 4
c = utils.pythagoras(a, b)  # 피타고라스 함수로 빗변 계산
print('c = ', c)

r = 10
area = utils.circle(r)  # 원의 면적 계산
print('area =', area)
