import pyupbit
import numpy as np
#ohlcv(Open, High, Low, Close, Volume)
df = pyupbit.get_ohlcv("KRW-BTC", count=7)

#변동폭 * k 계산, which is (고가 - 저가) * k
df['range'] = (df['high'] - df['low']) * 0.3

#target(매수가) = open(시초가) + range(어제변동폭)
#range 컬럼을 한 칸씩 밑으로 내림(.shift(1))
#어제의 변동폭을 이용해야 하기 때문
df['target'] = df['open'] + df['range'].shift(1)

#fee = 0.0032
fee = 0
df['ror'] = np.where(df['high'] > df['target'], # 고가>매수가, 즉 매수한지
                     df['close'] / df['target'] - fee, # 매수했을 때 수익률(종가/매수가)
                     1) # 매수하지 않았을 때

#누적 곱 계산(cumprod) -> 누적 수익률
df['hpr'] = df['ror'].cumprod()

#Draw Down 계산(누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

print(df)
#MaxDD
print("MDD(%): ", df['dd'].max())

#액셀로 출력
#df.to_excel("dd.xlsx")