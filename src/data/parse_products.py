from uuid import uuid4

from requests_html import HTMLSession

from src.database.base import db
from src.database.models import Product


URL = "https://rozetka.com.ua/ua/igrovie-mishi/c4673278/producer=logitech/"


def get_products(url: str = URL):
    session = HTMLSession()
    response = session.get(url)

    products = response.html.xpath('//rz-indexed-link[@class="product-link goods-tile__heading"]/a[@_ngcontent-rz-client-c4240794426 and @data-test="filter-link"]/@href')
    for product in products:
        save_product(product)

    db.session.commit()

def save_product(url: str):
    session = HTMLSession()
    response = session.get(url)
    
    name = response.html.xpath('//p[@_ngcontent-rz-client-c3166959541 and @class="title__font"]/text()')[0]
    price = response.html.xpath('//p[contains(@class, "product-price__big")]/text()')[0].replace(u"\xa0", "")
    img_url = response.html.xpath('//img[@_ngcontent-rz-client-c2880331661]/@src')[0]
    description = response.html.xpath('//div[@id="description" or contains(@class, "product-about")]//text()')
    description = ''.join(description)

    product = Product(
        id=uuid4().hex,
        name=name,
        description=description,
        img_url=img_url,
        price=price
    )

    db.session.add(product)
    print(f"Товар '{name}' успішно збережено")