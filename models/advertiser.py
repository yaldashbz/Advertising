from models.base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    __advertisers = dict()

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name
        Advertiser.__advertisers.update({id: self})

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def describe_me(self):
        return 'it is an Advertiser'

    @staticmethod
    def get_total_clicks():
        count = 0
        for advertiser in Advertiser.__advertisers.values():
            count += advertiser.get_clicks()
        return count

    @staticmethod
    def help():
        return 'Advertiser help'

    @staticmethod
    def get_advertiser_by_id(id):
        return Advertiser.__advertisers.get(id)
