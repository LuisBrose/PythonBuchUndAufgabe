import time
import urllib.request as u
import random as r
import threading as t
import sys


def get_page(url: str | u.Request, out: str):
    """
    Opens the specified url and saves the result in a file
    :param url: the url to be called
    :param out: the path to the output file
    """
    response = u.urlopen(url)
    try:
        out_file = open(out, 'wb')
        out_file.write(response.read())
    except Exception as e:
        print(e)


def get_page_often(url: str | u.Request, out_folder: str, delay_interval: (int, int), iterations: int):
    """
    Opens the specified url and save the result as many times as you want in random intervals
    :param url: the url to be called
    :param out_folder: the path to the output folder
    :param delay_interval: random delays between min and max (min == max possible)
    :param iterations: how many times you want to call the page
    """
    def anon():
        for i in range(0, iterations):
            get_page(url, f"{out_folder}/{r.randint(1000, 100000)}.html")
            time.sleep(r.randint(delay_interval[0], delay_interval[1]))
        thread.join()

    thread = t.Thread(target=anon, daemon=True)
    thread.start()


if __name__ == "__main__":
    r.seed()
    _url = input("Which site do you want to download?: ")
    _delay = (int(input("Min. time between downloads: ")), int(input("Max. time between downloads: ")))
    _iterations = int(input("How many times should the site be downloaded?: "))

    get_page_often(_url, f"out", _delay, _iterations)

    while True:
        if input("Type 'q' to stop the program:") == 'q':
            sys.exit(0)

