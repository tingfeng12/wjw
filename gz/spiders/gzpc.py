3# -*- coding: utf-8 -*-
import scrapy
import gz.items
import re
from copy import deepcopy

class GzpcSpider(scrapy.Spider):
    name = 'gzpc'
    # allowed_domains = ['http://wsjkw.gd.gov.cn/xxgzbdfk/yqtb/']
    start_urls = ['http://wsjkw.gd.gov.cn/xxgzbdfk/yqtb/']
    # start_urls = ['http://wsjkw.gd.gov.cn/xxgzbdfk/content/post_2881379.html']

    def parse(self, response):
        print(response)
        tr_list = response.xpath("//div[@class='section list']//li")
        for tr in tr_list:
            item = gz.items.GzItem()
            item['title'] = tr.xpath(".//a/@title").extract_first()
            item['href'] = tr.xpath(".//a/@href").extract_first()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_lis,
                meta={"item": deepcopy(item)}
            )
        next_url = ''.join(response.xpath("//a[@class='next']/@href").extract())
        # print(next_url)
        if next_url:
            # print('next')
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_lis(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data2 = ''.join(response.xpath("//div[@class='content-content']/p[2]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()

        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('新增确诊病例\d+', data1);
        item['newZY'] = re.search('新增出院\d+', data1);
        item['allQZ'] = re.search('肺炎确诊病例\d+', data1);

        item['men'] = re.search('男性\d+', data2);
        item['women'] = re.search('女性\d+', data2);

        item['allbv'] = re.search('危重\d+', data3);
        item['allzz'] = re.search('重症\d+', data3);
        item['allpt'] = re.search('普通病例\d+例', data3);
        item['allCY'] = re.search('出院\d+', data3);

        print(item)
        yield item
