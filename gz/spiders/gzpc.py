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
            time = ''.join(item['title'])
            time = ''.join(re.search('\d+月\d+日',time)[0])
            print(time)
            if time > '2月2日':
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_lis202,
                    meta={"item": deepcopy(item)}
                )
            elif time >= '1月29日':
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_lis129,
                    meta={"item": deepcopy(item)}
                )
            elif time >= '1月28日':
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_lis128,
                    meta={"item": deepcopy(item)}
                )
            elif time >= '1月26日':
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_lis126,
                    meta={"item": deepcopy(item)}
                )
            elif time >= '1月23日':
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_lis123,
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

    def parse_lis129(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data2 = ''.join(response.xpath("//div[@class='content-content']/p[2]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()

        item['allJC'] = '';
        item['imgsrc'] = '';
        item['newZZ'] = '';
        item['newVZ'] = '';
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

    def parse_lis202(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data2 = ''.join(response.xpath("//div[@class='content-content']/p[2]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()
        data4 = ''.join(response.xpath("//img[@class='nfw-cms-img']/@src").extract()).strip()
        # print(data4)
        item['newZZ'] = '';
        item['newVZ'] = '';
        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('新增确诊病例\d+', data1)[0];
        item['newQZ'] = item['newQZ'].split('病例')[1]
        item['allJC'] = re.search('\d+名密切接触者', data1)[0];
        item['allJC'] = item['allJC'].split('名')[0]
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

    def parse_lis128(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()
        data4 = ''.join(response.xpath("//div[@class='content-content']/p[4]/text()").extract()).strip()
        data5 = ''.join(response.xpath("//div[@class='content-content']/p[5]/text()").extract()).strip()

        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('新增确诊病例\d+', data1);
        item['newZZ'] = re.search('新增重症病例\d+', data1);
        item['newZY'] = re.search('新增出院病例\d+', data1);

        item['men'] = re.search('男性\d+', data4);
        item['women'] = re.search('女性\d+', data4);

        item['allQZ'] = re.search('肺炎确诊病例\d+', data3);
        item['allbv'] = re.search('危重病例\d+', data3);
        item['allzz'] = re.search('重症病例\d+', data3);
        item['allCY'] = re.search('出院病例\d+', data3);
        item['allJC'] = re.search('密切接触者\d+', data3);

        print(item)
        yield item

    def parse_lis126(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data2 = ''.join(response.xpath("//div[@class='content-content']/p[2]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()
        data4 = ''.join(response.xpath("//div[@class='content-content']/p[4]/text()").extract()).strip()

        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('新增确诊病例\d+', data1);
        item['newZZ'] = re.search('重症病例\d+', data1);
        item['newVZ'] = re.search('危重病例\d+', data1);

        item['men'] = re.search('男性\d+', data3);
        item['women'] = re.search('女性\d+', data3);

        item['allQZ'] = re.search('肺炎确诊病例\d+', data2);
        item['allbv'] = re.search('危重病例\d+', data2);
        item['allzz'] = re.search('重症病例\d+', data2);
        item['allCY'] = re.search('出院病例\d+', data2);

        item['allJC'] = re.search('密切接触者\d+', data4);

        print(item)
        yield item
    def parse_lis123(self, response):
        print(response)
        item = response.meta['item']
        data1 = ''.join(response.xpath("//div[@class='content-content']/p[1]/text()").extract()).strip()
        data3 = ''.join(response.xpath("//div[@class='content-content']/p[3]/text()").extract()).strip()
        data5 = ''.join(response.xpath("//div[@class='content-content']/p[5]/text()").extract()).strip()
        data6 = ''.join(response.xpath("//div[@class='content-content']/p[6]/text()").extract()).strip()

        item['datatime'] = re.search('\d.*月\d+日', data1);
        item['newQZ'] = re.search('肺炎新增确诊病例\d+', data1);

        item['men'] = re.search('男性\d+', data6);
        item['women'] = re.search('女性\d+', data6);

        item['allQZ'] = re.search('肺炎确诊病例\d+', data3);
        item['allbv'] = re.search('危重病例\d+', data3);
        item['allzz'] = re.search('重症病例\d+', data3);
        item['allCY'] = re.search('出院病例\d+', data3);

        item['allJC'] = re.search('密切接触者\d+', data5);

        print(item)
        yield item