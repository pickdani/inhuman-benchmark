import pyautogui # https://pyautogui.readthedocs.io/en/latest/
import webbrowser # https://docs.python.org/3/library/webbrowser.html

URL = 'https://humanbenchmark.com/tests/aim'

def setup_window():
    webbrowser.open_new(URL)

def find_target():
    pass

if __name__ == '__main__':
    setup_window()