from models.base_model import BaseAdvertising
from models.advertiser import Advertiser


class Ad(BaseAdvertising):
    __adds = dict()

    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__img_url = img_url
        self.__link = link
        self.__advertiser_id = advertiser.get_id()
        Ad.__adds.update({id: self})

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_img_url(self):
        return self.__img_url

    def set_img_url(self, img_url):
        self.__img_url = img_url

    def get_link(self):
        return self.__link

    def set_link(self, link):
        self.__link = link

    def describe_me(self):
        return 'it is an Ad'

    def inc_clicks(self):
        super().inc_clicks()
        advertiser = Advertiser.get_advertiser_by_id(self.__advertiser_id)
        advertiser.inc_clicks()
