# https://refactoring.guru/design-patterns/bridge

from abc import ABCMeta, abstractmethod


class EntertainmentDevice(metaclass=ABCMeta):
    def __init__(self):
        self.volume_level = 0

    def press_button_left(self):
        self.volume_level -= 1
        print('Volume is decreased')

    def press_button_right(self):
        self.volume_level += 1
        print('Volume is increased')

    @abstractmethod
    def press_button_up(self):
        pass

    @abstractmethod
    def press_button_down(self):
        pass


class TVDevice(EntertainmentDevice):
    def press_button_up(self):
        print("next channel")

    def press_button_down(self):
        print("previous channel")


class DVDDevice(EntertainmentDevice):
    def press_button_up(self):
        print("next track")

    def press_button_down(self):
        print("previous track")


class Remote():
    def __init__(self, device):
        self.device = device

    def press_button_left(self):
        self.device.press_button_left()

    def press_button_right(self):
        self.device.press_button_right()

    def press_button_up(self):
        self.device.press_button_up()

    def press_button_down(self):
        self.device.press_button_down()

    @abstractmethod
    def press_button_middle(self):
        pass


class TVRemote(Remote):
    def __init__(self, device):
        super(TVRemote, self).__init__(device)

    def press_button_middle(self):
        print("TV was muted")


class DVDRemote(Remote):
    def __init__(self, device):
        super(DVDRemote, self).__init__(device)

    def press_button_middle(self):
        print("DVD was paused")


device = int(input(
    "Which kind of device? 1.TV 2.DVD :"))
remote = int(input(
    "Which kind of remote? 1.TV remote 2.DVD remote :"))

if device == 1:
    device = TVDevice()
else:
    device = DVDDevice()

if remote == 1:
    remote = TVRemote(device)
else:
    remote = DVDRemote(device)

remote.press_button_left()
remote.press_button_right()
remote.press_button_up()
remote.press_button_down()
remote.press_button_middle()
