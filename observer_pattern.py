from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def unRegister(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(googlePrice, applePrice, ibmPrice):
        pass


class StockObserver(Observer):
    observerCounter = 0

    def __init__(self, stockGrabber):
        StockObserver.observerCounter += 1
        self.observerId = StockObserver.observerCounter
        stockGrabber.register(self)

    def update(self, googlePrice, applePrice, ibmPrice):
        print("observer id -" + str(self.observerId))
        print("the prices are:" + str(googlePrice) +
               " " + str(applePrice) + " " + str(ibmPrice))


class StockGrabber(Subject):
    def __init__(self):
        self.googlePrice = 0.0
        self.applePrice = 0.0
        self.ibmPrice = 0.0
        self.observers = []

    def register(self, o):
        self.observers.append(o)

    def unRegister(self, o):
        self.observers.remove(o)

    def notify(self):
        for observer in self.observers:
            observer.update(self.googlePrice, self.applePrice, self.ibmPrice)

    def setGooglePrice(self, price):
        self.googlePrice = price
        self.notify()

    def setApplePrice(self, price):
        self.applePrice = price
        self.notify()

    def setIBMPrice(self, price):
        self.ibmPrice = price
        self.notify()



stockGrabber = StockGrabber()
observer1 = StockObserver(stockGrabber)
observer2 = StockObserver(stockGrabber)

stockGrabber.setGooglePrice(100.0)
stockGrabber.setApplePrice(200.0)
stockGrabber.setIBMPrice(300.0)
