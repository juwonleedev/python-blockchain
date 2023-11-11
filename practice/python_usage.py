def f(x):
    return 2*x + 1

## 포유류 객체를 선언
class mammals(object):
    ## 포유류의 형태적 특징
    def __init__(self):
        self.number_of_legs = 4 # 다리가 4개 
        self.number_of_mouth = 1 # 입이 1개
        self.number_of_ears = 2 # 귀가 2개
    
    ## 포유류의 습성: 잔다
    def sleep(self, sleeping_time):
        time.sleep(sleeping_time)

    # 포유류의 특성: 소화시킨다
    def digest(self, food):
        food = food / 2 #음식을 반으로 나누다

# 포유류 객체를 활용하여 강아지를 선언
dog = mammals()
print ("dog legs: ", dog.number_of_legs)
dog.number_of_legs = 3
print("dog legs: ", dog.number_of_legs)