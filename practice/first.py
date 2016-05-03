#Given the height of a brick wall remove all bricks from the wall
# 1 brick by 1 brick wall

def brick_wall (height):
    '''This function will recursively call itself until height reaches 0'''
    while height is not -1 :
        print "Bricks",height
        height=height - 1
        return brick_wall(height)
    return
    
print("Hello World")
brick_wall(10)

    

