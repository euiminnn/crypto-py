import pyupbit

access = "zDgJ2X0OZKk1pA7OEl4c88Mh5xCR1NTIHw0TU9TV"          # 본인 값으로 변경
secret = "gtJtPUD4TC0KvyfxGO7T8xrbbMR2tcAQMygz0eSR"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회