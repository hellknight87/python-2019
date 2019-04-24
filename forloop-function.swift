func switchOn() {
    turnleft()
    moveForward()
    oggleSwitch()
    moveForward()
    toggleSwitch()
    turnLeft()
    turnLeft()
    moveForward()
    moveForward()
}

func gemEat() {
    moveForward()
    collectGem()
    moveForward()
    collectGem()
    turnLeft()
    turnLeft()
    moveForward()
    moveForward()
    turnRight()
}

for i in 1 ... 3 {
    switchOn()
    gemEat()
    moveForward()
}