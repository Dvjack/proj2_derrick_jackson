# Here is project 2

import numpy as np
import cv2
import queue as q
import os

obstacle = np.uint8(255)

x = 200
y = 100
# generating and diplaying the trial map
def get_trial():
    trial_map = np.zeros([y,x],np.uint8)
    trial_map[y-1-60:y-40-1,90:110] = 255
    # print(trial_map)
    cv2.circle(trial_map,(160-1,y-50-1),15,255,-1)
    # print(trial_map[50][160])
    # cv2.imshow('map', trial_map)
    # cv2.waitKey(0)
    return trial_map

trial_map = get_trial()
print(trial_map)

def get_pos():
    start_col = int(input("Starting Column: "))
    start_row = int(input("Starting Row: "))
    starting_position = [start_col,start_row]
    
    goal_col = int(input("Goal Column: "))
    goal_row = int(input("Goal Row: "))
    goal_position = [goal_col,goal_row]

    # print(f'start: {starting_position}')
    # print(f'goal: {goal_position}')
    return starting_position, goal_position

pos = get_pos()
start = pos[0]
goal = pos[1]
print(f'start: {start}')
print(f'goal: {goal}')

parent_visited = [0]
visited = [start]
parent_q = q.Queue()
parent_q.put_nowait(start)


def Action_Move(start_col, start_row, parent_pos, direction):

    next_pos = (start_col + direction[0], start_row + direction[1])

    

    if next_pos[1] < x and next_pos[1] >= 0 and next_pos[0] < y and next_pos[0] >= 0 and trial_map[next_pos[0], next_pos[1]] != obstacle and next_pos not in visited:

        trial_map[next_pos[0], next_pos[1]] = 150
        cv2.imshow('bfs map', trial_map)
        cv2.waitKey(0)

        visited.append(next_pos)
        parent_visited.append(parent_pos)
        parent_q.put_nowait(next_pos)

        if next_pos[0] == goal[0] and next_pos[1] == goal[1]:
            print("Goal has been reached")
            print(f'End is: {next_pos}')
            return True
    return False


my_list = []
    
try:
        goal_reached = False
        i =0
        while not goal_reached:

            print(f'I is:{i}')
            print(list(parent_q.queue))
            parent_pos = parent_q.get_nowait()
            my_list.append(parent_pos)

            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (0,-1))
           
            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (0,1)) or goal_reached
            
            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (-1,0)) or goal_reached
            
            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (1,0)) or goal_reached

            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (-1,-1)) or goal_reached

            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (1,-1)) or goal_reached

            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (-1,1)) or goal_reached

            goal_reached = Action_Move(parent_pos[0],parent_pos[1], parent_pos, (1,1)) or goal_reached

            if parent_q.empty():
                print("No Solution")

                break
            i += 1
except KeyboardInterrupt:
    exit()

my_path = []
j = 0
current_pos = tuple(goal)
# print(f'Visited is: {visited}')
# print(f'parent visited: {parent_visited}')
while current_pos != 0:
    # print(f'J is {j}')
    winning_index = visited.index(current_pos)
    # print(f'win:{winning_index}')
    # print(parent_visited[winning_index])
    my_path.append(current_pos)
    current_pos = parent_visited[winning_index]

    j += 1

my_path.reverse()
print(f'optimized: {my_path}')
