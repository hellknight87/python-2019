func gemEat() {
    collectGem()
    if isBlocked {
        turnLeft()
    }
}

func switchOpen() {
    if isOnClosedSwitched {
        toggleSwitch()
        if isBlocked {
            turnRight()
        }
    }
}

func solveBlock() {
    if isBlocked {
        turnLeft()
    } else if isBlocked {
        turnRight()
    }
}

for i in 1 ... 12 {
    moveForward()
    if isOnGem {
        gemEat()
    } else if isOnClosedSwitched {
        switchOpen()
    } else if isBlocked {
        solveBlock()
    }
}