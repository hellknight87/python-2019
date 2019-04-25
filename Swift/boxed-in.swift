func collectGem {
    moveForward()
    if onGem {
        collectGem()
    }
}

func switchCheck {
    moveForward()
    if onClosedSwitch {
        toggleSwitch()
    }
}

for i in 1 ... 9 {
    collectGem()
    turnleft()
    switchCheck()
}