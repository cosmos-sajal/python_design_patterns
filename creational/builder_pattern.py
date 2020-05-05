# https://stackoverflow.com/questions/757743/what-is-the-difference-between-builder-design-pattern-and-factory-design-pattern
# https://stackoverflow.com/questions/328496/when-would-you-use-the-builder-pattern

from abc import ABCMeta, abstractmethod


class Robot(metaclass=ABCMeta):
    @abstractmethod
    def create_head(self):
        pass

    @abstractmethod
    def create_arms(self):
        pass

    @abstractmethod
    def create_torso(self):
        pass

    @abstractmethod
    def create_legs(self):
        pass


class OldRobotImplementation(Robot):
    def __init__(self):
        self.head = None
        self.legs = None
        self.arms = None
        self.torso = None

    def create_head(self):
        self.head = "Tin Head"

    def create_torso(self):
        self.torso = "Tin Torso"

    def create_arms(self):
        self.arms = "Torch Arms"

    def create_legs(self):
        self.legs = "Rollers"


class NewRobotImplementation(Robot):
    def __init__(self):
        self.head = None
        self.legs = None
        self.arms = None
        self.torso = None

    def create_head(self):
        self.head = "Titanium Head"

    def create_torso(self):
        self.torso = "Carbon fiber"

    def create_arms(self):
        self.arms = "Cutter Arms"

    def create_legs(self):
        self.legs = "Rockets"


class RobotDirectorInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_robot(self):
        pass

    @abstractmethod
    def get_robot(self):
        pass


class RobotDirector(RobotDirectorInterface):
    def __init__(self, robot_style):
        self.robot = robot_style

    def create_robot(self):
        self.robot.create_head()
        self.robot.create_torso()
        self.robot.create_arms()
        self.robot.create_legs()

    def get_robot(self):
        robot = self.robot
        print(robot.head)
        print(robot.legs)
        print(robot.torso)
        print(robot.arms)

        return self.robot


robot_director = RobotDirector(OldRobotImplementation())
robot_director.create_robot()
print("------Old Robot------")
robot_1 = robot_director.get_robot()

robot_director = RobotDirector(NewRobotImplementation())
robot_director.create_robot()
print("------New Robot------")
robot_2 = robot_director.get_robot()
