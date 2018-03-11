import math
import api
import time

moveConst = 0.4
turnConst = 0.33
distanceTolerance = 20

class Position(object):
    def __init__(self,dict):
        self.x=dict["x"]
        self.y=dict["y"]

class Player(object):
    def __init__(self,dict):
        self.position=Position(dict['position'])
        self.angle=dict['angle']
        self.health = ['health']
        self.armour = ['armour']
        self.weapons = ['weapons']
        self.ammo = ['ammo']

    def GetAngleTo(self, target):

        diffX = self.position.x - target.position.x
        diffY = self.position.y - target.position.y
        angle = math.Atan2(diffY, diffX) * (180/math.pi)  # not sure

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
        elif (math.abs(rightTurn) < math.abs(leftTurn)):
            val =180 - rightTurn
        elif math.abs(leftTurn) < math.abs(rightTurn):
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

        formatedAngle = math.abs(self.angle - reqAngle)
        return int(formatedAngle) < tolerance

    def turnTo(self, target):
        angle = self.GetAngleTo(target)
        amount=math.abs(angle)*turnConst

        if angle > 0:
            api.player_Action("turn-right", amount)
        else:
            api.player_Action("turn-left", amount)

    def distance(self, target):
        return math.hypot(self.position.x - target.position.x, self.position.y - target.position.y)

    def move(self, target):
        if not self.lookingAt(target):
            self.turnTo(target)
        else:
            distance = self.distance()
            #shoot or move
            api.move(distance*moveConst)

    def shoot(self, target):
        #get the best weapon find weapon and change
        self.turnTo(target)
        time.sleep(1/20)
        if self.lookingAt(target):
            api.player_Action("shoot", 1)
            api.player_Action("shoot", 1)
            api.player_Action("shoot", 1)
            api.player_Action("shoot", 1)
            api.player_Action("shoot", 1)


    def atTarget(self,target):
        distance = self.distance()

        if distance < distanceTolerance:
            return True
        else:
            return False

    def giveThemHell(self,target):
        for x in range(4):
            self.turnTo(target)
            self.move(target)
            self.shoot(target)
            time.sleep(1/15)
