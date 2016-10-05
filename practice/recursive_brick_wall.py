#Given the height of a brick wall remove all bricks from the wall
# 1 brick by 1 brick wall

def brick_wall (height):
    '''
        This function will recursively call itself until height reaches 0
        :param type height: height of the brick wall 
    '''
    if height >0:
        print(height," bricks")
        height=height-1
        return brick_wall(height)
    else:
        print('Wall is destroyed')

brick_wall(20)
