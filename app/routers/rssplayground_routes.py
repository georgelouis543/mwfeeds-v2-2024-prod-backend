from fastapi import APIRouter

from app.controllers.rssplayground_controllers.parser_controller import parse_input_rss
from app.models.rss_playground.item_params import ItemParamsModel

router = APIRouter(
    prefix="/rss-playground",
    tags=["RSS Playground"]
)


@router.post("/get-feed-preview")
async def get_rss_feed_preview(item_params: ItemParamsModel):
    preview_items = await parse_input_rss(dict(item_params))
    return preview_items
