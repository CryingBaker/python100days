def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    elif not wall_on_right() and front_is_clear():
        turn_right()
        if front_is_clear():
            move()
    else:
        turn_right()
        if front_is_clear():
            move()