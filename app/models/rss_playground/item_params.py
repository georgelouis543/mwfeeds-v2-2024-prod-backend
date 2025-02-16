from pydantic import BaseModel


class ItemParamsModel(BaseModel):
    feed_url: str = ""
    item_xpath: str = "/rss/channel/item"
    title_xpath: str = ".//title/text()"
    description_xpath: str = "//description/text()"
    date_xpath: str = ".//pubDate/text()"
    item_url_xpath: str = ".//link/text()"
    source_name_xpath: str = ".//source/text()"
    default_source_name: str = "Example Source"
    source_url_xpath: str = ".//source/@url"
    default_source_url: str = "https://www.example.com"
    image_url_xpath: str = "https://www.example.com/image1.png"
    owner: str = "example@meltwater.com"
    feature_type: str = "sharepoint"
    default_image_url: str = "https://www.example.com/image1.png"