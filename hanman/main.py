import os


class main:
    for index in range(32):
        os.system(f'scrapy crawl manhwa -a page={index+1} -o manhua{index+1}.json --nolog')
