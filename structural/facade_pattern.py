# https://stackoverflow.com/questions/5242429/what-is-the-facade-design-pattern


class CPU():
    def boot_up(self):
        print("booting up system")


class Memory():
    def load(self):
        print("loading stuff into memory")


class HardDrive():
    def read(self):
        print("reading programs from memory")


class ComputerFacade():
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.boot_up()
        self.memory.load()
        self.hard_drive.read()


computer = ComputerFacade()
computer.start()
