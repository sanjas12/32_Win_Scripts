import pyautogui
import time
import sys

def move_mouse():
    try:
        print("Скрипт запущен. Для остановки нажмите Ctrl+C в консоли.")
        while True:
            # Получаем текущую позицию курсора
            x, y = pyautogui.position()
            
            # Смещаем курсор немного вправо и обратно
            pyautogui.moveRel(50, 0, duration=0.1)
            pyautogui.moveRel(-50, 0, duration=0.1)
            
            # Ждем 10 минут (600 секунд)
            time.sleep(600)
    except KeyboardInterrupt:
        print("\nСкрипт остановлен.")
        sys.exit()

if __name__ == "__main__":
    move_mouse()