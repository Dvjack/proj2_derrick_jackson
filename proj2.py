# Here is project 2

import numpy as np
import cv2

x = 200
y = 100
# generating and diplaying the trial map
def trial():
    trial_map = np.zeros([y,x],np.uint8)
    trial_map[y-1-60:y-40-1,90:110] = 255
    # print(trial_map)
    cv2.circle(trial_map,(160-1,y-50-1),15,(255,0,0),-1)
    # print(trial_map[50][160])
    # cv2.imshow('map', trial_map)
    # cv2.waitKey(0)

trial()

def get_pos():
    start_col = int(input("Starting Column: "))
    start_row = int(input("Starting Row: "))
    starting_position = [start_col,start_row]
    goal_col = int(input("Goal Column: "))
    goal_row = int(input("Goal Row: "))
    goal_position = [goal_col,goal_row]

    print(f'start: {starting_position}')
    print(f'goal: {goal_position}')

get_pos()


def Action_Move(start_col, start_row, direction):

    next_pos = (start_col + direction[0], start_row + direction[1])

    if next_pos[0] < x and next_pos[0] >= 0 and next_pos[1] < y and next_pos[1] >= 0:

        return
    
# try:
#         goal_reached = False
#         i =0
#         while not goal_reached:


#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (0,-1))
           
#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (0,1)) or goal_reached
            
#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (-1,0)) or goal_reached
            
#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (1,0)) or goal_reached

#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (-1,-1)) or goal_reached

#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (1,-1)) or goal_reached

#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (-1,1)) or goal_reached

#             goal_reached = Action_Move(blank_tile_col,blank_tile_row, parent_state, (1,1)) or goal_reached

