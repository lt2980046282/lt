import os


def novel():
    for index in range(400):
        os.system(f'scrapy crawl manhwa -a page={index+1} -o novel{index+1}.json --nolog')
        print(index+1)


def daili():
    for index in range(1502):
        os.system(f'scrapy crawl daili -a page={index+1819} ')

novel()