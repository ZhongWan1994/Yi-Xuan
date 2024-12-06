from bazi_spider.customer import Customer
from bazi_spider.data_parser import DataParser
from bazi_spider.data_spider import DataSpider
from bazi_spider.test import Test

if __name__ == '__main__':
    customer = Customer("淡定姐", "0", "1985", "07", "14", "12", "20", "上海", "上海", "浦东新区")
    dataSpider = DataSpider(customer)
    raw_data = dataSpider.get_bazi_raw_data()
    data_parser = DataParser(customer)
    data_parser.parse_data(raw_data)
    Test.print_simple_info(customer)

