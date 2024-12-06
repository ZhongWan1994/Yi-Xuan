import json

from bazi_spider.customer import Customer


class DataParser(object):
    def __init__(self, customer: Customer):
        self.customer = customer

    @staticmethod
    def trans2json(raw_data):
        json_str = raw_data
        data = json.loads(json_str)
        for key, value in data.items():
            if isinstance(value, str) and value.startswith('\\u'):
                data[key] = value.replace('\\u', '')
        return data

    def parse_data(self, raw_data):
        js_data = self.trans2json(raw_data)

        self.customer.year_start_gua = {"TG": js_data["tdbz"]["0"], "DZ": js_data["tdbz"]["1"]}
        self.customer.month_start_gua = {"TG": js_data["tdbz"]["2"], "DZ": js_data["tdbz"]["3"]}
        self.customer.day_start_gua = {"TG": js_data["tdbz"]["6"], "DZ": js_data["tdbz"]["7"]}
        self.customer.hour_start_gua = {"TG": js_data["tdbz"]["4"], "DZ": js_data["tdbz"]["5"]}

        self.customer.year_pillar = {"TG": js_data["bz"]["0"], "DZ": js_data["bz"]["1"]}
        self.customer.month_pillar = {"TG": js_data["bz"]["2"], "DZ": js_data["bz"]["3"]}
        self.customer.day_pillar = {"TG": js_data["bz"]["6"], "DZ": js_data["bz"]["7"]}
        self.customer.hour_pillar = {"TG": js_data["bz"]["4"], "DZ": js_data["bz"]["5"]}
        self.customer.flow_year_pillar = {"TG": None, "DZ": None}
        self.customer.big_luck_pillar = {"TG": None, "DZ": None}
        self.customer.bazi_str = js_data["bz"]["8"]

        self.customer.year_hidden_gan = js_data["cg"][0]
        self.customer.month_hidden_gan = js_data["cg"][1]
        self.customer.day_hidden_gan = js_data["cg"][2]
        self.customer.hour_hidden_gan = js_data["cg"][3]
        self.customer.flow_year_hidden_gan = []
        self.customer.big_luck_hidden_gan = []

        self.customer.year_vice_star = js_data["cgss"][0]
        self.customer.month_vice_star = js_data["cgss"][1]
        self.customer.day_vice_star = js_data["cgss"][2]
        self.customer.hour_vice_star = js_data["cgss"][3]
        self.customer.flow_year_vice_star = []
        self.customer.big_luck_vice_star = []

        self.customer.year_star_yun = js_data["xy"][0]
        self.customer.month_star_yun = js_data["xy"][1]
        self.customer.day_star_yun = js_data["xy"][2]
        self.customer.hour_star_yun = js_data["xy"][3]
        self.customer.flow_year_star_yun = None
        self.customer.big_luck_star_yun = None

        self.customer.year_self_loc = js_data["zz"][0]
        self.customer.month_self_loc = js_data["zz"][1]
        self.customer.day_self_loc = js_data["zz"][2]
        self.customer.hour_self_loc = js_data["zz"][3]
        self.customer.flow_year_self_loc = None
        self.customer.big_luck_self_loc = None

        self.customer.year_entity_disappear = js_data["kw"][0]
        self.customer.month_entity_disappear = js_data["kw"][1]
        self.customer.day_entity_disappear = js_data["kw"][2]
        self.customer.hour_entity_disappear = js_data["kw"][3]
        self.customer.flow_year_entity_disappear = None
        self.customer.big_luck_entity_disappear = None

        self.customer.year_include_sounds = js_data["ny"][0]
        self.customer.month_include_sounds = js_data["ny"][1]
        self.customer.day_include_sounds = js_data["ny"][2]
        self.customer.hour_include_sounds = js_data["ny"][3]
        self.customer.flow_year_include_sounds = None
        self.customer.big_luck_include_sounds = None

        self.customer.year_main_star = js_data["ss"][0]
        self.customer.month_main_star = js_data["ss"][1]
        self.customer.day_main_star = js_data["ss"][2]
        self.customer.hour_main_star = js_data["ss"][3]
        self.customer.flow_year_main_star = None
        self.customer.big_luck_main_star = None

        self.customer.year_spirits = js_data["szshensha"][0]
        self.customer.month_spirits = js_data["szshensha"][1]
        self.customer.day_spirits = js_data["szshensha"][2]
        self.customer.hour_spirits = js_data["szshensha"][3]
        self.customer.flow_year_spirits = []
        self.customer.big_luck_spirits = []

        self.customer.xiaoyun_seq = js_data["xiaoyun"]
        self.customer.dayun_seq = js_data["dayun"]

        return self.customer
