# cryptocurrency auto buy n sell

## 궁금한 점들
- 보유현금 중 일부만 투자하고 싶다면?
- 여러 자산에 투자하고 싶다면?
- 코드 뜯어보기

## code to run the aws server
- 터미널에서 매매 시작하기(ctrl+z 누르면 매매도 종료됨)
```python
python3 bitcoinAutotrade.py
```

- 백그라운드에서 매매 실행하기(창 꺼도 계속 실행됨)
```python
nohup python3 bitcoinAutoTrade.py > output.log &
```

- 실행 중인지 확인
```python
ps ax | grep .py
```

- 프로세스 종료(ps ax 명령어 맨 왼쪽이 PID임)
```python
kill -9 PID
```
