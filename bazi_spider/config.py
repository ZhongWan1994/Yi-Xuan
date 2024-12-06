from bazi_spider.customer import Customer


class Config(object):
    def __init__(self, customer: Customer):
        self.customer = customer
        self.proxy_bat_path = r'E:\ProgramFiles\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat'
        self.target_url = "https://pcbz.iwzwh.com/#/paipan-result/index?name=%s&sex=%s&solarTime=%s&solarTime=" \
                          "%s&solarTime=%s&solarTime=%s&solarTime=%s&address=%s&sunTime=%s&sunTime=%s&sunTime=" \
                          "%s&sunTime=%s&sunTime=%s" % (customer.name, customer.sex,
                                                        customer.year, customer.month, customer.day, customer.hour,
                                                        customer.minute,
                                                        "%s+%s+%s" %
                                                        (customer.province, customer.city, customer.area),
                                                        customer.year, customer.month, customer.day, customer.hour,
                                                        customer.minute)
