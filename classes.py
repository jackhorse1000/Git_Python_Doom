import math
import api
import time

class Obj(object):
    def __init__(self,dict):
        self.position=Position(dict['position'])
        self.type=dict['type']
        self.dict=dict
        self.id=dict['id']

moveConst = 0.15
turnConst = 0.37
distanceTolerance = 20

class Position(object):
    def __init__(self,dict):
        self.x=dict["x"]
        self.y=dict["y"]

class Player(object):
    def __init__(self,dict):
        self.position=Position(dict['position'])
        self.id=dict['id']
        self.angle=dict['angle']
        self.health = dict['health']
        self.armor = dict['armor']
        self.weapons = dict['weapons']
        self.weapon = dict['weapon']
        self.ammo = dict['ammo']

    def no_ammo(self):
        if self.ammo['Shells'] == 0 and self.ammo['Bullets'] == 0:
            return True
        else:
            return False


    def GetAngleTo(self, target):

        diffX = self.position.x - target.position.x
        diffY = self.position.y - target.position.y
        angle = math.atan2(diffY, diffX) * (180/math.pi)  # not sure

        if angle < 0:
            angle = angle + 360

        rightTurn = angle - self.angle
        leftTurn = 360 - angle + self.angle

        if leftTurn > 360:
            leftTurn = leftTurn - 360
            rightTurn = 360 - leftTurn

        val = 0.0

        if rightTurn == leftTurn:
            val = rightTurn
        elif (abs(rightTurn) < abs(leftTurn)):
            val =180 - rightTurn
        elif abs(leftTurn) < abs(rightTurn):
            val = -180 + leftTurn

        return val

    def lookingAt(self, target):
        distance = math.hypot(self.position.x - target.position.x, self.position.y - target.position.y)
        reqAngle = self.GetAngleTo(target)
        tolerance = 2

        if distance < 25:
            tolerance = 35

        if distance < 10:
            tolerance = 45

        formatedAngle = abs(self.angle - reqAngle)
        return int(formatedAngle) < tolerance

    def turnTo(self, target):
        angle = self.GetAngleTo(target)
        amount=abs(angle)*turnConst

        if angle > 0:
            api.player_Action("turn-right", amount)
        else:
            api.player_Action("turn-left", amount)

    def distance(self, target):
        return math.hypot(self.position.x - target.position.x, self.position.y - target.position.y)

    def move(self, target,ratio=0.5):
        distance = self.distance(target)*ratio
        if distance>distanceTolerance:
            api.player_Action("forward", int(distance * moveConst))
        #shoot or move


    def shoot(self, target):
        api.player_Action("shoot", 1)
        api.player_Action("shoot", 1)
        api.player_Action("shoot", 1)

    def atTarget(self,target):
        distance = self.distance(target)

        if distance < distanceTolerance:
            return True
        else:
            return False

    def turn(self,angle):
        amount = abs(angle) * turnConst

        if angle > 0:
            api.player_Action("turn-right", amount)
        else:
            api.player_Action("turn-left", amount)

    def moveDistance(self, distance):
        api.player_Action("forward", int(distance * moveConst))

    def Goto(self,target,ratio=0.5):
        self.turnTo(target)
        time.sleep(2)
        self.move(target,ratio=ratio)


    def giveThemHell(self,target):
        for x in range(4):
            time.sleep(2)
            self.turnTo(target)
            time.sleep(2)
            self.move(target)
            time.sleep(4)
            self.shoot(target)
            time.sleep(2)

    def turn_frame(self, turn):

        if turn>0:
            api.player_Action("turn-right", 5)
        else:
            api.player_Action("turn-left", 5)

    def strafe_frame(self,direction):
        if direction>0:
            api.player_Action("strafe-right",10)
        else:
            api.player_Action("strafe-left",10)

    def move_frame(self):
        api.player_Action("forward", 16)




