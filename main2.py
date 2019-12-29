leftTopTop = False
leftTopLeft = False
rightTopTop = False
rightTopRight = False
rightBotRight = False
rightBotBot = False
leftBotBot = False
leftBotLeft = False

for b in listMapy:
    if b.terrain == 0:
        if b.x < maciek.x - offpos[0] + 2 < b.x + b.size and b.y < maciek.y - offpos[1] + 2 < b.y + b.size:
            leftTopTop = True

        if b.x < maciek.x - offpos[0] - 2 < b.x + b.size and b.y < maciek.y - offpos[1] - 2 < b.y + b.size:
            leftTopLeft = True

        if b.x < maciek.x + maciek.size * 2 - offpos[0] - 2 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - \
                offpos[1] + 2 < b.y + b.size:
            rightTopTop = True

        if b.x < maciek.x + maciek.size * 2 - offpos[0] + 2 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - \
                offpos[1] - 2 < b.y + b.size:
            rightTopRight = True

        if b.x < maciek.x + maciek.size * 2 - offpos[0] + 2 < b.x + b.size and b.y < maciek.y - offpos[
            1] + 2 < b.y + b.size:
            rightBotRight = True

        if b.x < maciek.x + maciek.size * 2 - offpos[0] - 2 < b.x + b.size and b.y < maciek.y - offpos[
            1] - 2 < b.y + b.size:
            rightBotBot = True

        if b.x < b.x < maciek.x - offpos[0] - 2 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[
            1] + 2 < b.y + b.size:
            leftBotLeft = True

        if b.x < maciek.x - offpos[0] + 2 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[
            1] - 2 < b.y + b.size:
            leftBotBot = True

maciek.leftblock = 1
maciek.upblock = 1
maciek.rightblock = 1
maciek.downblock = 1
if leftTopTop and leftTopLeft:
    maciek.leftblock = 0
    maciek.upblock = 0
elif rightTopTop and rightTopRight:
    maciek.upblock = 0
    maciek.rightblock = 0
elif rightBotBot and rightBotRight:
    maciek.rightblock = 0
    maciek.downblock = 0
elif leftBotBot and leftBotLeft:
    maciek.downblock = 0
    maciek.leftblock = 0
elif leftTopTop or rightTopTop:
    maciek.upblock = 0
elif rightTopRight or rightBotRight:
    maciek.rightblock = 0
elif rightBotBot or leftBotBot:
    maciek.downblock = 0
elif leftBotLeft or leftTopLeft:
    maciek.leftblock = 0