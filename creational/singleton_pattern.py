# https://stackoverflow.com/questions/3192095/where-exactly-the-singleton-pattern-is-used-in-real-application
# https://dzone.com/articles/design-patterns-singleton
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
# https://code.google.com/archive/p/google-singleton-detector/wikis/WhySingletonsAreControversial.wiki
# https://www.vojtechruzicka.com/singleton-pattern-pitfalls/
# https://www.youtube.com/watch?v=-FRm3VPhseI


class Singleton():
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    def get_instance(self):
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance


s = Singleton()
print(s)
print(s.get_instance())
print(s.get_instance())
