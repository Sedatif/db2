import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import cmdline
from lxml import etree
import webbrowser

#cmdline.execute("scrapy crawl task1".split())
#cmdline.execute("scrapy crawl task2".split())

print("task 1")
with open('out/task1.xml', 'rb') as file:
    root = etree.parse(file)
minAmount = 100
pages = root.xpath('//page')
for page in pages:
    amount = page.xpath('count(./fragment[@type="image"])') 
    if amount < minAmount:
        minAmount = amount 
print('Minimal amount of graphic elements on page are %i\n' % minAmount)

print("task 2")
transform = etree.XSLT(etree.parse('transform.xsl'))
result = transform(etree.parse('out/task2.xml'))
result.write("out/task2.xhtml", pretty_print=True, encoding="UTF-8")
print("XHTML created.")
webbrowser.open('file://' + os.path.realpath("out/task2.xhtml"))