import pyautogui
import time

def auto_click(interval, button, stop_position):
    while True:
        current_position = pyautogui.position()
        if current_position == stop_position:
            print("Auto-klikovanje je zaustavljeno.")
            break
        pyautogui.click(button=button)
        time.sleep(interval)

interval = 0.00001  
button = 'left'
stop_position = (0, 0)
print(f"start")
time.sleep(5) 
auto_click(interval, button, stop_position)
