# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class NewgzPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='wjw',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        self.cursor = self.connect.cursor();


    def process_item(self, item, spider):
        self.cursor.execute("""insert into dbgz(datatime,newQZ,nowJC,allQZ,men,women,allbv,allzz,allpt,newCY,allCY,imgsrc) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                """, (item['datatime'],  # item里面定义的字段和表字段对应
             item['newQZ'],
             item['nowJC'],
             item['allQZ'],
             item['men'],
             item['women'],
             item['allbv'],
             item['allzz'],
             item['allpt'],
             item['newCY'],
             item['allCY'],
             item['imgsrc']))

        self.connect.commit()

        return item
