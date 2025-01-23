import pyscreenshot as ImageGrab  
import pyautogui 
import numpy as np 
import keyboard

# Function to find the coordinates of a certain color
def find_color_on_screen(target_color, tolerance=2):
    # Take a screenshot of the entire screen
    screenshot = ImageGrab.grab()
    image = np.array(screenshot)

    # Loop through all pixels to find the color
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            # Check if the pixel color matches the target color within the tolerance
            if (abs(pixel[0] - target_color[0]) <= tolerance and
                abs(pixel[1] - target_color[1]) <= tolerance and
                abs(pixel[2] - target_color[2]) <= tolerance):
                return x, y  # Return the first match
    return None

def main():
    # Define the target color in RGB format
    target_color = (0, 0, 0) 
    
    
    ## while A key is not pressed do:
    while True:
        if keyboard.is_pressed('a'):
            print("A key pressed. Executing code...")
            while not keyboard.is_pressed('space'):
                position = find_color_on_screen(target_color)
                if position:
                    x, y = position
                    print(f"Color found at: ({x}, {y})")
                    pyautogui.moveTo(x, y) 
                    pyautogui.click()
            print("B key pressed. Stopping execution.")
            break
    
if __name__ == "__main__":
    main()