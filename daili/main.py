import os
import time
from threading import Thread


class RunDaili(Thread):
    name = ''

    def __init__(self, name):
        self.name = name
        super(RunDaili, self).__init__()

    def run(self):
        rundl(self.name)


def rundl(l):
    os.system(f'py {l}.py')


def main():
    # 'success_daili',
    ls = ['dlmysql', 'daili', 'fail_daili']
    for index, l in enumerate(ls):
        t = RunDaili(l)
        try:
            t.start()
        except:
            pass


if __name__ == '__main__':
    main()
