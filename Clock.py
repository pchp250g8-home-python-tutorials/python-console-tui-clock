import time
import datetime
import curses

stdscr = curses.initscr()
curses.curs_set(0)
stdscr.clear()
stdscr.keypad(True)
stdscr.nodelay(True)
keycode = 0
while keycode <= 0:
    keycode = stdscr.getch()
    strtime = str(datetime.datetime.now().time())[0:8]
    stdscr.addstr(1,1,"Time:" + strtime)
    stdscr.refresh()
    time.sleep(1.0)
curses.endwin()