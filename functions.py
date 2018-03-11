import api
import math


def GetAngleTo(Target):

    diffX = math.abs(player.position.x - target.x)
    diffY = math.abs(player.position.y - target.y)
    angle = math.degrees(math.Atan2(diffY, diffX) ) #not sure

    if angle < 0:
        angle = angle +360

    rightTurn = angle - player.angle
    leftTurn = 360 - angle + player.angle

    if leftTurn > 360 :
        leftTurn = leftTurn -360
        rightTurn = 360 -leftTurn

    val = 0.0

    if rightTurn ==leftTurn:
        val = rightTurn
    elif (math.abs(rightTurn) < math.abs(leftTurn)):
        val = rightTurn
    elif math.abs(leftTurn) < math.abs(rightTurn):
            val = -leftTurn

    return -val



#
# func (player *Player) DistanceTo(target Position) float64 {
#     var distance = math.Hypot(player.Position.X-target.X, player.Position.Y-target.Y)
#     return distance
# }
def lookingAt(target):
    distance = math.hypot(player.x -target.x, player.y - target.y)
    reqAngle = player.GetAngleTo(target)
    tolerance = 2

    if distance < 25:
        tolerance = 35

    if distance < 10:
        tolerance = 45

    formatedAngle = math.abs(player.angle - requiredAngle)
    return int(formatedAngle)<tolerance

#
# func (player *Player) EqualCoordinates(target Position) bool {
#     var diffX = math.Abs(target.X - player.Position.X)
#     var diffY = math.Abs(target.Y - player.Position.Y)
#     return diffX < 100 && diffY < 100
# }
#
# func (player *Player) EqualCoordinatesPrecise(target Position) bool {
#     var diffX = math.Abs(target.X - player.Position.X)
#     var diffY = math.Abs(target.Y - player.Position.Y)
#     return diffX == 0 && diffY == 0
# }