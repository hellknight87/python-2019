func route1() {
    turnRight()
    moveForward()
    moveForward()
}

func route2() {
    moveForward()
    collectGem()
    turnLeft()
    turnLeft()
    moveForward()
}

for i in 1 ... 3 {
    moveForward()
    if isOnGem {
        collectGem()
        route1()
        turnLeft()
        route2()
        route1()
        turnRight()
    } else ifOnCloseSwitch {
        toggleSwitch()
        turnLeft()
        route2()
        turnLeft()
    }
}