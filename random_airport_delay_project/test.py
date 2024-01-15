# tis but a test
import keyboard
import random

# # Define the key to win
# winning_key = 'w'

# def on_key_event(e):
#     if e.event_type == keyboard.KEY_DOWN:
#         print(f'Key {e.name} was pressed')
        
#         if e.name == winning_key:
#             print('Congratulations! You found the winning key. You win!')
#             keyboard.unhook_all()

# # Register the callback function
# keyboard.hook(on_key_event)

# # Generate a random winning key
# winning_key = random.choice('abcdefghijklmnopqrstuvwxyz')

# print(f'Find and press the key: {winning_key}')

# keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit the program

a = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
print(random.choice(a))