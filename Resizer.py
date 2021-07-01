import pyautogui as pg

#print(pg.getAllTitles())


windows = pg.getWindowsWithTitle("Google – Brave")

for window in windows:
    window.resizeTo(480,480)

