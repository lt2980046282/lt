import json
import os
from threading import Thread
import dlmysql

class RemoveFile(Thread):

    def __init__(self, manhua):
        self.manhua = manhua
        super(RemoveFile, self).__init__()

    def run(self):
        checkUnique(self.manhua)


def checkUnique(manhua):
    dlist = os.listdir('manhua')
    for m in manhua:
        for d in dlist:
            if d != m['comic_name']:
                with open('re.txt', 'a+') as f:
                    f.write(f'{d}\n')


def main():
    for i in range(1, 26):
        with open(f'manhua{i}.json', 'r') as f:
            m = json.loads(f.read())
        t = RemoveFile(m)
        t.start()


if __name__ == '__main__':
    main()