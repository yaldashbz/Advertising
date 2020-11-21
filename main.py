from models.ad import Ad
from models.advertiser import Advertiser
from models.base_model import BaseAdvertising

if __name__ == '__main__':
    base_advertising = BaseAdvertising()

    advertiser_1 = Advertiser(1, 'name1')
    advertiser_2 = Advertiser(2, 'name2')

    ad_1 = Ad(1, 'title1', 'img_url1', 'link', advertiser_1)
    ad_2 = Ad(2, 'title1', 'img_url1', 'link', advertiser_2)

    print(base_advertising.describe_me(),
          ad_2.describe_me(),
          advertiser_1.describe_me(),
          sep='\n')

    ad_1.inc_views()
    ad_1.inc_views()
    ad_1.inc_views()
    ad_1.inc_views()
    ad_2.inc_views()
    ad_1.inc_clicks()
    ad_1.inc_clicks()
    ad_2.inc_clicks()

    print(advertiser_2.get_name())
    advertiser_2.set_name('new name')
    print(advertiser_2.get_name(),
          ad_1.get_clicks(),
          advertiser_2.get_clicks(),
          Advertiser.get_total_clicks(),
          Advertiser.help(),
          sep='\n')
