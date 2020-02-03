# -*- coding: utf-8 -*-
import scrapy
import re
import newgz.items

class NewgzpcSpider(scrapy.Spider):
    name = 'newgzpc'
    # allowed_domains = ['http://wsjkw.gd.gov.cn/xxgzbdfk/yqtb']
    start_urls = ['http://wsjkw.gd.gov.cn/xxgzbdfk/yqtb/content/post_2881900.html']

    def parse(self, response):
        print(response)
        item = newgz.items.NewgzItem()
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data2 = ''.join(response.xpath("//div[@class='content-content']/p[2]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()
        data4 = ''.join(response.xpath("//img[@class='nfw-cms-img']/@src").extract()).strip()
        # print(data4)
        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('新增确诊病例\d+', data1)[0];
        item['newQZ'] = item['newQZ'].split('病例')[1]
        item['nowJC'] = re.search('\d+名密切接触者', data1)[0];
        item['nowJC'] = item['nowJC'].split('名')[0]
        item['allQZ'] = re.search('肺炎确诊病例\d+', data1)[0];
        item['allQZ'] = item['allQZ'].split('病例')[1]

        item['men'] = re.search('男性\d+', data2)[0];
        item['men'] = item['men'].split('男性')[1];
        item['women'] = re.search('女性\d+', data2)[0];
        item['women'] = item['women'].split('女性')[1];

        item['allbv'] = re.search('危重\d+', data3)[0];
        item['allbv'] = item['allbv'].split('重')[1];
        item['allzz'] = re.search('重症\d+', data3)[0];
        item['allzz'] = item['allzz'].split('症')[1];
        item['allpt'] = re.search('普通型\d+例', data3)[0];
        item['allpt'] = item['allpt'].split('型')[1].split('例')[0];
        item['newCY'] = re.search('新增出院\d+', data3)[0];
        item['newCY'] = item['newCY'].split('出院')[1];
        item['allCY'] = re.search('累计出院\d+', data3)[0];
        item['allCY'] = item['allCY'].split('出院')[1];
        item['imgsrc'] = data4;

        print(item)
        yield item

