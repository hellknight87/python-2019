func collectOrToggle() {
    if isOnGem {
        collectGem()
    } else if isOnClosedSwitch {
        toggleSwitch()
    }
}

func solveRow() {
    moveForward()
    moveForward()
    collectOrToggle()
    moveForward()
    moveForward()
    collectOrToggle()
}

solveRow()
turnLeft()
moveForward()
moveForward()
turnLeft()
solveRow()
turnRight()
moveForward()
turnRight()
solveRow()