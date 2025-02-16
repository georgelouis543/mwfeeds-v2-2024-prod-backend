from fastapi import HTTPException
from lxml import etree

from app.controllers.rssplayground_controllers.fetch_source_controller import fetch_rss_feed


async def parse_input_rss(item_params: dict) -> list:
    feed_url = item_params.get("feed_url")
    if not feed_url:
        raise HTTPException(status_code=400, detail="Bad Request")

    xml_response = await fetch_rss_feed(feed_url)
    if not xml_response:
        return []

    try:
        xml_parser = etree.XMLParser()
        tree = etree.fromstring(xml_response, xml_parser)

        parsed_data = []
        items = tree.xpath(item_params["item_xpath"])

        for item in items:

            temp_dict = {}

            try:
                temp_dict["title"] = item.xpath(item_params["title_xpath"])[0]
            except:
                temp_dict["title"] = ""

            try:
                temp_dict["description"] = item.xpath(item_params["description_xpath"])[0]
            except:
                temp_dict["description"] = ""

            try:
                temp_dict["date"] = item.xpath(item_params["date_xpath"])[0]
            except:
                temp_dict["date"] = ""

            try:
                temp_dict["source_name"] = item.xpath(item_params["source_name_xpath"])[0]
            except:
                temp_dict["source_name"] = ""

            try:
                temp_dict["source_url"] = item.xpath(item_params["source_url_xpath"])[0]
            except:
                temp_dict["source_url"] = ""

            try:
                temp_dict["item_url"] = item.xpath(item_params["item_url_xpath"])[0]
            except:
                temp_dict["item_url"] = ""

            try:
                temp_dict["image_url"] = item.xpath(item_params["image_url_xpath"])[0]
            except:
                temp_dict["image_url"] = item_params.get("default_image_url",
                                                         "https://www.meltwaternews.com/ext/blr/george/MeltwaterLogo"
                                                         "MWFeeds.png")

            parsed_data.append(temp_dict)

        return parsed_data

    except Exception as e:
        print(f"Exception {e} occurred")
        return []
