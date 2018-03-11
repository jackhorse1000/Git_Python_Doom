import math
import api
import time

moveConst = 0.3
turnConst = 0.33
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
        self.health = ['health']
        self.armour = ['armour']
        self.weapons = ['weapons']
        self.ammo = ['ammo']

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

    def move(self, target):
        distance = self.distance(target)
        if distance>distanceTolerance:
            api.player_Action("forward", int(distance * moveConst))
        #shoot or move


    def shoot(self, target):
        api.player_Action("shoot", 1)


    def atTarget(self,target):
        distance = self.distance(target)

        if distance < distanceTolerance:
            return True
        else:
            return False

    def giveThemHell(self,target):
        for x in range(4):
            time.sleep(2)
            self.turnTo(target)
            time.sleep(2)
            self.move(target)
            time.sleep(4)
            self.shoot(target)
            time.sleep(2)
