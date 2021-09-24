import pyautogui

def udelejSS(nazev):
    roughPath = r"C:\Users\KDK\Desktop\screenshot_test\t"
    actualPath = roughPath+nazev
    print(actualPath)

    pyautogui.screenshot(roughPath + nazev)