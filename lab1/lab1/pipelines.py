from lxml import etree
from itemadapter import ItemAdapter

class Lab1Pipeline:
    def __init__(self):
        self.root: etree.Element = None

    def open_spider(self, spider):
        self.root = etree.Element(spider.name)

    def close_spider(self, spider):
        with open('out/%s.xml' % spider.name, 'wb') as file:
            file.write(etree.tostring(self.root, encoding="UTF-8", pretty_print=True, xml_declaration=True))
    
    def process_item(self, item, spider):
        if spider.name == "task1":
            page = etree.SubElement(self.root, 'page', url=item['url'])
            for text in item['text_elements']:
                etree.SubElement(page, 'fragment', type='text').text = text
            for img_src in item['image_elements']:
                etree.SubElement(page, 'fragment', type='image').text = img_src
        else:
            product = etree.Element("product")
            desc = etree.Element("description")
            desc.text = item["description"]
            pr = etree.Element("price")
            pr.text = item["price"]
            preview = etree.Element("preview")
            preview.text = item["preview"]
            product.append(desc)
            product.append(pr)
            product.append(preview)
            self.root.append(product)
        return item