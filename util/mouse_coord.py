# -*- coding: utf-8 -*-
import time
import pyautogui
import tkinter as tk


def detete_mouse(mode):

    if mode == 'shell':
        print('\nPress Ctrl-C to quit ...\n')
        try:
            while True:
                x, y = pyautogui.position()
                text = f'X: {x}'.center(8, ' ') + f'Y: {y}'.center(8, ' ')
                print('\r>>> %s' % text, end='')
                time.sleep(0.1)
        except:
            print('\n\nBye ~\n')
            time.sleep(1)

    elif mode == 'window':
        def window_setting():
            root = tk.Tk()
            root.title('Mouse Coord')
            # root.overrideredirect(1)
            root.geometry("200x30+1688+950")
            root.wm_attributes("-alpha", 0.6)
            root.wm_attributes("-toolwindow", True)
            root.wm_attributes("-topmost", True)
            return root
        root = window_setting()
        var = tk.StringVar()
        label = tk.Label(root, textvariable=var)
        def get_position():
            x, y = pyautogui.position()
            text = f'X: {x}'.center(8, ' ') + f'Y: {y}'.center(8, ' ')
            var.set(text)
            label.pack()
            root.after(100, get_position)
        root.after(0, get_position)
        root.mainloop()        


if __name__ == "__main__":

    detete_mouse('window')
