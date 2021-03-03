# Here is project 2

import numpy as np
import cv2

x = 200
y = 100

trial_map = np.zeros([y,x],np.uint8)
trial_map[y-1-60:y-40-1,90:110] = 255
# print(trial_map)
cv2.circle(trial_map,(160-1,y-50-1),15,(255,0,0),-1)
print(trial_map[50][160])
cv2.imshow('map', trial_map)
cv2.waitKey(0)

def find_blank_tile(array):

        # grab index of where the value of the index of the state is 0
        blank_tile = np.where(np.asarray(array) == 0)[0][0]
       
        # print(f'blank tile location is: {blank_tile}')
        
        return blank_tile

def Action_Move(zero_col, zero_row, parent_state, direction):
        
        next_pos = (zero_col + direction[0], zero_row + direction[1])
        
        # If the move is legal then swap the blank space with the next position
        if next_pos[0] < size and next_pos[0] >= 0 and next_pos[1] < size and next_pos[1] >= 0:
            
            next_pos_index = (next_pos[1] * size) + next_pos[0]
            zero_loc = (zero_row * size) + zero_col
            

            curr_state = parent_state.copy()
            
            
            temp = curr_state[zero_loc]
            curr_state[zero_loc] = curr_state[next_pos_index]
            curr_state[next_pos_index] = temp
            
            # If the current state isn't visited then append it to the visited list and add it to the queue     
                   
            if curr_state not in visited:

                visited.append(curr_state)
                parent_visited.append(parent_state)
               
                parent_q.put_nowait(curr_state)

                # Let us know when we are at the goal state and return true
                if curr_state == goal_state:
                    print("Goal has been reached")
                    print(f'Puzzle is: {curr_state}')
                    return True
        return False 
