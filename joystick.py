import pygame
import subprocess

# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() < 1:
    print("No joystick found.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Joystick initialized:", joystick.get_name())

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "zero_state"])
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "zero_state"])
            if event.button == 2:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "straight_up"])
            if event.button == 3:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "pick_object_pose"])
            if event.button == 4:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "lift_object_pose"])
            if event.button == 5:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "opposite_pose"])
            if event.button == 1:  # Assuming button '0' corresponds to 'X'
                # Run the command
                subprocess.run(["python3", "/home/raju/Documents/run/sender_v2.py", "--new_text", "place_object_pose"])
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
