# encoding=utf-8
import os
from threading import Thread
# 批量压缩工具


class WinrarTools(Thread):
    def __init__(self, path, limit_size, file_name, mode):
        # 路径、分卷大小、文件名称、模式
        self.path, self.limit_size, self.file_name, self.mode = path, limit_size, file_name, mode
        super(WinrarTools, self).__init__()

    def run(self):
        if 'c' in self.mode:
            compress(self.path, self.limit_size, self.file_name, self.mode)
        elif self.mode == 'd':
            decompress(self.path)


def compress(path, limit_size, file_name, mode):
    if 'cmp' in mode:
        # 带密码分卷压缩
        os.system(f'rar a -p980727  -v{limit_size}m {file_name}.rar {path}')
    elif 'cm' == mode:
        # 不带密码分卷压缩
        os.system(f'rar a -v{limit_size}m {file_name}.rar {path}')


def decompress(path, mode):
    if 'cmp' in mode:
        # 带密码解压缩
        os.system(f'rar x {path}')
    elif 'cm' == mode:
        # 不带密码解压缩
        os.system(f'rar x {path}')


def main():
    filenames = os.listdir()
    for filename in filenames:
        if os.path.isdir(f'{filename}'):
            print(filename)
            t = WinrarTools(f'/{filename}/a', 100, f'{filename}', 'cmp')
            t.start()
        else:
            continue


if __name__ == '__main__':
    main()