## Synthetic.py

import numpy as np

def make_synthetic_brick(im_shape, width, height, shift_x, shift_y):
    '''
    Make really simple sythetic brick.
    '''
    brick = np.zeros(im_shape)
    brick[shift_y:shift_y+height, shift_x:shift_x+width]= 1.0
    return brick

def make_random_bricks(num_bricks = 10, im_shape = (20, 20)):
    ''' 
    Create a set of random bricks! Return list of brick images. 
    '''
    them_bricks = []
    for i in range(num_bricks):
        #Randomly pick brick params:
        width = np.random.randint(im_shape[1]//2, im_shape[1]-2)
        height = np.random.randint(im_shape[0]//4, im_shape[0]//2)
        shift_x = np.random.randint(1, im_shape[1]-width)
        shift_y = np.random.randint(1, im_shape[0]-height)
        
        brick = make_synthetic_brick(im_shape, width, height, shift_x, shift_y)
        them_bricks.append(brick)
        
    return them_bricks

def make_synthetic_ball(im_shape, center, radius):
    '''
    Make really simple sythetic ball.
    '''
    ball = np.zeros(im_shape)
    all_x, all_y = np.where(ball==0)
    circle_indices = ((all_x-center[0])**2 + (all_y-center[1])**2) <= radius**2
    ball[all_y[circle_indices], all_x[circle_indices]] = 1.0
    
    return ball

def make_random_balls(num_balls = 10, im_shape = (20, 20)):
    '''
    Create a set of random bricks! Return list of brick images. 
    '''
    balls = []
    for i in range(num_balls):
        #Randomly pick brick params:
        radius = np.random.randint(im_shape[1]//10, im_shape[1]//2)
        center_x = np.random.randint(radius, im_shape[1]-radius)
        center_y = np.random.randint(radius, im_shape[0]-radius)
        
        ball = make_synthetic_ball(im_shape, (center_y, center_x), radius)
        balls.append(ball)
        
    return balls