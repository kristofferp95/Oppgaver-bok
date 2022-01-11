import time

class Time: 
    def __init__(self, time1 = time.time(), hours = 0, minute = 0, second = 0):
        self.__hours = hours
        self.__minute = minute
        self.__second = second 
        self.__time1 = time1

    def getHours(self): 
        return self.__hours

    def getMinutes(self): 
        return self.__minute
    
    def getSecond(self): 
        return self.__second

    def getTime(self):
        return self.__time1

    def setTime(self, time): 
        self.__hours = int(time / 60 / 60 % 24)
        self.__minute = int(time / 60 % 60)
        self.__second = int(time % 60)

def main(): 
    k = time.time()
    print(f'Current time is {int(k / 60 / 60 % 24)}:{int(k / 60 % 60)}:{int(k % 60)}')
    elapsed = int(input(f'Enter the elapsed time: '))
    currentTime = Time()
    currentTime.setTime(elapsed)
    print(f'The hour:minute:second for elapse time is {currentTime.getHours()}:{currentTime.getMinutes()}:{currentTime.getSecond()}')

main()
