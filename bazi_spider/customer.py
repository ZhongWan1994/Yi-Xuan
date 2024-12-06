class Customer(object):
    def __init__(self, name, sex, year, month, day, hour, minute, province="北京", city="北京", area="东城区"):
        self.cid = "00000"
        self.name = name
        self.sex = sex

        # 出生年月日时
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

        # 起卦时间四柱
        self.year_start_gua = None
        self.month_start_gua = None
        self.day_start_gua = None
        self.hour_start_gua = None

        # 属地
        self.province = province
        self.city = city
        self.area = area

        # 四柱、大运流年
        self.year_pillar = {"TG": None, "DZ": None}
        self.month_pillar = {"TG": None, "DZ": None}
        self.day_pillar = {"TG": None, "DZ": None}
        self.hour_pillar = {"TG": None, "DZ": None}
        self.flow_year_pillar = {"TG": None, "DZ": None}
        self.big_luck_pillar = {"TG": None, "DZ": None}
        self.bazi_str = ""

        # 藏干
        self.year_hidden_gan = []
        self.month_hidden_gan = []
        self.day_hidden_gan = []
        self.hour_hidden_gan = []
        self.flow_year_hidden_gan = []
        self.big_luck_hidden_gan = []

        # 副星
        self.year_vice_star = []
        self.month_vice_star = []
        self.day_vice_star = []
        self.hour_vice_star = []
        self.flow_year_vice_star = []
        self.big_luck_vice_star = []

        # 星运
        self.year_star_yun = None
        self.month_star_yun = None
        self.day_star_yun = None
        self.hour_star_yun = None
        self.flow_year_star_yun = None
        self.big_luck_star_yun = None

        # 自坐
        self.year_self_loc = None
        self.month_self_loc = None
        self.day_self_loc = None
        self.hour_self_loc = None
        self.flow_year_self_loc = None
        self.big_luck_self_loc = None

        # 空亡
        self.year_entity_disappear = None
        self.month_entity_disappear = None
        self.day_entity_disappear = None
        self.hour_entity_disappear = None
        self.flow_year_entity_disappear = None
        self.big_luck_entity_disappear = None

        # 纳音
        self.year_include_sounds = None
        self.month_include_sounds = None
        self.day_include_sounds = None
        self.hour_include_sounds = None
        self.flow_year_include_sounds = None
        self.big_luck_include_sounds = None

        # 主星
        self.year_main_star = None
        self.month_main_star = None
        self.day_main_star = None
        self.hour_main_star = None
        self.flow_year_main_star = None
        self.big_luck_main_star = None

        # 神煞
        self.year_spirits = []
        self.month_spirits = []
        self.day_spirits = []
        self.hour_spirits = []
        self.flow_year_spirits = []
        self.big_luck_spirits = []

        # 基本序列
        self.xiaoyun_seq = []
        self.dayun_seq = []
