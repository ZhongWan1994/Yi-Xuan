from time import sleep

from bazi_spider.config import Config
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DataSpider(object):
    def __init__(self, customer):
        self.config = Config(customer)

    def init(self):
        server = Server(self.config.proxy_bat_path)
        server.start()
        proxy = server.create_proxy()

        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--proxy-server={}'.format(proxy.proxy))
        browser = webdriver.Chrome(options=chrome_options)
        return browser, proxy

    @staticmethod
    def has_kw_for_bazi(url):
        if "getbasebz" in url:
            return True
        else:
            return False

    def get_bazi_raw_data(self):
        browser, proxy = self.init()
        proxy.new_har(self.config.customer.name, options={"captureContent": True, "captureContent": True})
        browser.get(self.config.target_url)
        sleep(3)
        result = proxy.har
        raw_bazi_data = ""

        for item in result["log"]["entries"]:
            if "request" in item.keys():
                if "url" in item["request"].keys():
                    if "getbasebz" in item["request"]["url"]:
                        raw_bazi_data = item["response"]["content"]["text"]
        return raw_bazi_data
