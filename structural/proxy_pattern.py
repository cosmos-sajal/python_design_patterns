# https://refactoring.guru/design-patterns/proxy

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class RealSubject(Subject):
    def execute(self):
        print("executing the actual function, maybe accessing DB")


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def execute(self):
        if self.is_accessible():
            self._real_subject.execute()
            self.log_access()

    def is_accessible(self):
        print("checking accessibility")
        return True

    def log_access(self):
        print("logging access")


proxy = Proxy(RealSubject())
proxy.execute()
