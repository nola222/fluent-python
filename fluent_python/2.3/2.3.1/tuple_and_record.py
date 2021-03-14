# -*- coding: utf-8 -*-
# Nola

# 把元组用作记录


def record_with_tuple():
    lax_cordinates = (-118.40687, 33.94251)  # 美国洛杉矶国际机场经纬度
    city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 88014)  # 东京2003年的人口总数变化率及面积
    traveler_ids = [("USA", "321645564"), ("BRA", "462122101"), ("ECS", "134652222")]
    for passport in sorted(traveler_ids):
        print("%s/%s" %passport)

    for country, _ in sorted(traveler_ids):
        print(country)


if __name__ == '__main__':
    record_with_tuple()

