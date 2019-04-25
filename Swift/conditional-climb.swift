for i in 1 ... 16 {
    if isOneGem {
        collectGem()
        turnLeft()
    } else {
        moveForward()
    }
}