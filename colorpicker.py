#!/usr/bin/env python3

import os
import re
from sys import platform
import pyautogui
import pyperclip
from pynput import mouse


def grab_color(x, y):
    pixel = pyautogui.screenshot(
        region=(x, y, 1, 1))
    color = pixel.getcolors()[0][1]
    r, g, b = color
    print()
    print('Color:')
    print(f'rgb ({r}, {g}, {b})')
    hex_str = '#%02x%02x%02x' % (r, g, b)
    print(f'hex {hex_str}')
    pyperclip.copy(hex_str)
    print('Copied to clipboard.')


def on_click(x, y, button, pressed):
    if pressed:
        grab_color(x, y)


def preview_color():
    pyautogui.displayMousePosition()


def cleanup():
    for f in os.listdir('.'):
        if re.search(r'\.screenshot.*\.png', f):
            os.remove(os.path.join('.', f))


def main():
    assert platform == 'linux'
    listener = mouse.Listener(
        on_click=on_click)
    listener.start()
    print('Click to copy the current color to the clipboard.')
    preview_color()
    cleanup()


if __name__ == "__main__":
    main()
