import pyautogui
import time

def pick_color():
    print("Mexe no rato para obter a cor do pixel. Pressiona Ctrl+C para parar.")
    try:
        while True:
            x, y = pyautogui.position() # Posicao do rato
            pixel_color = pyautogui.screenshot().getpixel((x, y)) #Obter a cor do pixel
            print(f"Mouse at ({x}, {y}) - Color: {pixel_color}", end="\r")
            time.sleep(0.1) # Delay para nao sobrecarregar o CPU
    except KeyboardInterrupt:
        print("\nColor picking stopped.")
        exit()

if __name__ == "__main__":
    pick_color()
