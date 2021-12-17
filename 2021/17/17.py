#target area: x=96..125, y=-144..-98
seen = set()
glob_max_y = 0
for xvel_ in range(-200,200,1):
    for yvel_ in range(-200,200,1):
        x = 0
        y = 0
        xvel = xvel_
        yvel = yvel_
        max_y = 0
        while True:
            x += xvel
            y += yvel
            if y > max_y:
                max_y = y
            if xvel > 0:
                xvel -= 1
            elif x < 0:
                xvel += 1
            yvel -= 1
            if x >= 96 and x <= 125:
                if y >= -144 and y <= -98:
                    seen.add((xvel_,yvel_))
                    if max_y > glob_max_y:
                        glob_max_y = max_y
            if y < -144:
                break
print(glob_max_y)
print(len(seen))
