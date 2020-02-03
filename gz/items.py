# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    href = scrapy.Field()  # 链接地址
    datatime = scrapy.Field()  # 时间
    newQZ = scrapy.Field()  # 新增确诊
    newZZ = scrapy.Field()  # 新增重症
    newVZ = scrapy.Field()  # 新增危重
    newZY = scrapy.Field()  # 新增治愈
    allQZ = scrapy.Field()  # 累计确诊
    allJC = scrapy.Field()  # 密切接触者

    men = scrapy.Field()    # 男性
    women = scrapy.Field()  # 女性
    allbv = scrapy.Field()  # 危重
    allzz = scrapy.Field()  # 重症
    allpt = scrapy.Field()  # 普通病例
    allCY = scrapy.Field()  # 累计治愈
    imgsrc = scrapy.Field()  # 图片地址
