def turn_right(fuckit):
    turn_left()
    turn_left()
    turn_left()
    fuckit += 1
    return fuckit

fuckit = 0
while not at_goal():
    if fuckit<5:
        if wall_on_right() and front_is_clear():
            move()
        elif wall_on_right() and not front_is_clear():
            turn_left()
            fuckit = 0
        elif not wall_on_right() and front_is_clear():
            fuckit = turn_right(fuckit)
            if front_is_clear():
                move()
        else:
            fuckit = turn_right(fuckit)
            if front_is_clear():
                if not at_goal():
                    move()
    while fuckit > 4:
         if front_is_clear() and not at_goal():
            move()
            fuckit = 0
         else:
            fuckit = turn_right(fuckit)
    