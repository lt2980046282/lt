
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):
    comic ={}

    def get_media_requests(self, item, info):
        self.comic = dict(item)
        img = self.comic['img']
        yield Request(img)

    def file_path(self, request, response=None, info=None):
        filename = f'{self.comic["comic_name"]}/{self.comic["comic_chapter_name"]}/{self.comic["i"]}.jpg'
        return filename




