## 포유류 객체를 선언
class mammals(object):
    ## 포유류의 형태적 특징
    def __init__(self):
        self.number_of_legs = 4 # 다리가 4개 
        self.number_of_mouth = 1 # 입이 1개
        self.number_of_ears = 2 # 귀가 2개
        self.gender = "MALE" # 남성 (혹은 "FEMALE")

    ## 포유류의 습성 : 잔다
    def sleep (self, sleeping time):
        time.sleep(sleeping_time) ## sleeping_time 만큼 움직이지 않고 잔다

    ## 포유류의 습성 : 먹는다
    def eat (self, food):
        digest(food)
    
    ## 포유류의 습성: 소화시킨다
    def digest(self, food):
        food = food / 2 # 음식을 반으로 나눈다!!

    ## 포유류의 습성: 배변한다
    def dump (self, food):
        food = 0 # 음식이 다 나가고 0이 된다!!

     
## 포유류 객체를 활용하여 강아지를 선언
dog = mammals()
    
## 포유류 객체를 활용하여 고양이를 선언
cat = mammals()
    
## 포유류 객체를 활용하여 소를 선언
cow = mammals()

## 강아지의 다리 개수 확인하기
print(dog.number_of_legs)

## 강아지의 다리 3개로 변화
dog.number_of_legs = 3

## 강아지의 다리 개수 확인하기
print(dog.number_of_legs)

