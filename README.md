# wdzjNews

用xpath定位到需要获取的信息位置，然后赋值给模型类属性，最后在管道中插入数据库存储


首先：(在终端中输入操作)
$ scrapy startproject xxx

终端中提示信息如下：
New Scrapy project 'xxx', using template directory '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/scrapy/templates/project', created in:
/Users/aaa/xxx

You can start your first spider with:
cd xxx
scrapy genspider example example.com

其次：
用pycharm打开上面的项目
新建spider文件，用pycharm查看

$ cd xxx/xxx/spiders/

$ scrapy genspider xxx_spider xxx.com

终端中提示信息如下：
Created spider 'xxx_spider' using template 'basic' in module:
xxx.spiders.xxx_spider

然后：
新建main.py执行终端操作(详细可查看demo)
from scrapy import cmdline
cmdline.execute('scrapy crawl xxx_spider'.split())

四、明确目标
在 items.py (就是一般程序中的model数据源模型类)
xxx = scrapy.Field()
xxx = scrapy.Field()

五、制作爬虫
class xxxSpiderSpider(scrapy.Spider):
# 爬虫名字
name = 'xxx_spider'
# 允许域名
allowed_domains = ['movie.xxx.com']
# 入口URL 扔到调度器里面
start_urls = ['https://xxxx.com/xxx']

def parse(self, response):
    # 数据解析
    print(response.text)
六、数据解析：
数据解析重点在于如何匹配HTML中的内容，有三种方法：第一，正则表达式。第二，xpath。第三，beautifulsoup
首先，正则表达式容错率很低。其次，xpath通俗易懂，Chrome工具有直接copy xpath选项，方便快捷。最后，beautifulsoup语法也比较简便，效率比较xpath略低。
