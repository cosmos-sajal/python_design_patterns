# https://refactoring.guru/design-patterns/chain-of-responsibility


class Handler1():
    def execute(self, value):
        if value == True:
            # some logic here
            print("proceeding handler 1")
            return True
        else:
            raise Exception('can not proceed')


class Handler2():
    def execute(self, value):
        if value == True:
            # some logic here
            print("proceeding handler 2")
            return True
        else:
            raise Exception('can not proceed')


class Handler3():
    def execute(self, value):
        if value == True:
            # some logic here
            print("proceeding handler 3")
            return True
        else:
            raise Exception('can not proceed')


try:
    o = Handler1().execute(True)
    o = Handler2().execute(o)
    o = Handler3().execute(o)
except:
    print("An exception occurred, can not proceed")
