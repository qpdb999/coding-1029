
'''
파이썬 모듈과 라이브러리

    오늘 배운 내용

모듈과 라이브러리는 다른 곳에 작성된 기능을
가져와서 프로그램에서 사용할 수 있도록 해 준다.

예를 들어 수학 계산, 난수 생성, 날짜와 시간 확인 등의
기능을 직접 만들지 않고도 사용할 수 있다.

파이썬에서는 import를 사용해 모듈을 가져올 수 있다.



    모듈과 라이브러리의 정의


1) 모듈(Module)
파이썬 코드가 작성된 하나의 파일이다.
함수, 변수, 클래스 등을 포함할 수 있다.

예: math, random, datetime

2) 라이브러리(Library)
특정 기능을 편리하게 사용할 수 있도록
여러 코드와 기능을 모아 놓은 것이다.

3) import
모듈이나 라이브러리의 기능을 가져와 사용할 때 쓰는 명령어이다.

4) from ... import ...
모듈에서 필요한 기능을 직접 가져오는 방법이다.

5) as
모듈이나 가져온 기능에 별칭을 지정할 때 사용한다.



    math 모듈 사용하기


import math

number = 16

print("숫자:", number)
print("제곱근:", math.sqrt(number))
print("올림:", math.ceil(3.2))
print("내림:", math.floor(3.8))
print("원주율:", math.pi)



    random 모듈 사용하기


import random

number = random.randint(1, 10)

print("랜덤 숫자:", number)

menu = ["김밥", "돈가스", "비빔밥", "라면"]

choice = random.choice(menu)

print("오늘의 메뉴:", choice)



    from ... import ... 사용하기


from math import sqrt, pi

print("25의 제곱근:", sqrt(25))
print("원주율:", pi)



    as로 별칭 지정하기


import random as rd

number = rd.randint(1, 100)

print("무작위 숫자:", number)



    datetime 모듈 사용하기

import datetime

now = datetime.datetime.now()

print("현재 날짜와 시간:", now)
print("현재 연도:", now.year)
print("현재 월:", now.month)
print("현재 일:", now.day)



    모듈을 직접 만들어 사용하기


모듈은 파이썬 파일 하나로 직접 만들 수도 있다.

예를 들어 아래 내용을 calculator.py 파일에 저장한다.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

같은 폴더에 있는 다른 파이썬 파일에서 다음처럼 사용할 수 있다.

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))

실행 결과:
15
5

주의: 실제로 실행하려면 calculator.py 파일을 별도로 만들어야 한다.



    코드 분석

import math
- math 모듈을 가져온다.

math.sqrt(16)
- math 모듈의 sqrt() 기능을 사용해 제곱근을 구한다.
- 결과는 4.0이다.

math.ceil(3.2)
- 3.2보다 크거나 같은 가장 작은 정수를 구한다.
- 결과는 4이다.

math.floor(3.8)
- 3.8보다 작거나 같은 가장 큰 정수를 구한다.
- 결과는 3이다.

random.randint(1, 10)
- 1부터 10까지의 정수 중 하나를 무작위로 선택한다.
- 1과 10도 결과에 포함된다.

random.choice(menu)
- menu 리스트에 있는 항목 중 하나를 무작위로 선택한다.

from math import sqrt, pi
- math 모듈에서 sqrt와 pi만 가져온다.
- 이후 math.sqrt() 대신 sqrt()로 사용할 수 있다.

import random as rd
- random 모듈에 rd라는 별칭을 붙인다.
- rd.randint()처럼 사용할 수 있다.

datetime.datetime.now()
- 현재 날짜와 시간을 가져온다.



    복습하면서 알게 된 점


1) 모듈은 파이썬 코드가 작성된 파일이며,
   함수와 변수 등을 포함할 수 있다.

2) import를 사용하면 다른 모듈의 기능을 가져와 사용할 수 있다.

3) math 모듈을 이용하면 제곱근, 올림, 내림 등의 계산을 할 수 있다.

4) random 모듈을 이용하면 무작위 숫자나 항목을 선택할 수 있다.

5) from ... import ...를 사용하면 필요한 기능만 가져올 수 있다.

6) as를 사용하면 모듈에 짧은 별칭을 지정할 수 있다.

7) 직접 만든 파이썬 파일도 모듈로 사용할 수 있다.


========================================
📌 11. AI 활용 복습 문제
========================================

1) 파이썬에서 모듈을 가져올 때 사용하는 명령어는?
1. print   2. import   3. input   4. return

정답: 2번 (import)


2) 제곱근이나 원주율 등의 수학 기능을 제공하는 모듈은?
1. random   2. datetime   3. math   4. os

정답: 3번 (math)


3) 1부터 10까지의 정수 중 무작위 숫자를 선택하는 코드는?
1. random.sqrt(1, 10)
2. random.randint(1, 10)
3. math.randint(1, 10)
4. datetime.choice(1, 10)

정답: 2번 (random.randint(1, 10))


4) 리스트에서 무작위 항목 하나를 선택하는 기능은?
1. random.choice()
2. math.floor()
3. datetime.now()
4. random.sqrt()

정답: 1번 (random.choice())


5) import random as rd의 의미는?
1. random 모듈을 삭제한다.
2. random 모듈을 rd라는 별칭으로 사용한다.
3. rd라는 파일을 만든다.
4. random 모듈을 실행하지 않는다.

정답: 2번 (random 모듈을 rd라는 별칭으로 사용한다.)


6) from math import sqrt를 사용하면 어떻게 쓸 수 있을까?
1. math.sqrt(25)만 가능하다.
2. sqrt(25)처럼 사용할 수 있다.
3. sqrt 기능을 삭제한다.
4. math 모듈이 자동으로 설치된다.

정답: 2번 (sqrt(25)처럼 사용할 수 있다.)


7) 현재 날짜와 시간을 확인할 때 사용할 수 있는 기능은?
1. random.randint()
2. math.pi
3. datetime.datetime.now()
4. math.floor()

정답: 3번 (datetime.datetime.now())


8) 직접 만든 calculator.py를 같은 폴더의 다른 파이썬 파일에서
모듈로 사용하려면 어떤 명령어를 사용할 수 있을까?
1. import calculator
2. print calculator
3. input calculator
4. return calculator

정답: 1번 (import calculator)
'''
