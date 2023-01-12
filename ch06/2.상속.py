"""
날짜 : 2023/01/11
이름 : 임민지
내용 : 파이썬 상속 실습하기
"""

from sub2.stockAccount import StockAccount

kb = StockAccount('KB증권', '101-12-1110', '홍길동', 50000, '삼성전자', 10, 60000)
kb.deposit(1000000)
kb.sell(5, 70000)
kb.show()