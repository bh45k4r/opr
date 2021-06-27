from pynamodb.attributes import MapAttribute, UnicodeAttribute, ListAttribute

from .base import BaseModel


class ArticleCard(MapAttribute):
    """
    This represents each card (display block) in the article page
    """
    card_title = UnicodeAttribute()
    card_text = UnicodeAttribute()


class ArticleBody(MapAttribute):
    """
    This is the article body which is a list of article cards
    """
    article_cards = ListAttribute(of=ArticleCard)


class ArticlesModel(BaseModel):
    """
    Table for Articles
    """
    class Meta:
        table_name: str = "articles"
        region: str = BaseModel.Meta.region
        host: str = BaseModel.Meta.host
        aws_access_key_id: str = BaseModel.Meta.aws_access_key_id
        aws_secret_access_key: str = BaseModel.Meta.aws_secret_access_key
        write_capacity_units: int = BaseModel.Meta.write_capacity_units
        read_capacity_units: int = BaseModel.Meta.read_capacity_units
    """
    Identifier of the article. An article can be directly
    retrieved using the ID [O(1) operation].
    """
    article_id = UnicodeAttribute(hash_key=True)
    article_title = UnicodeAttribute()
    """
    Body of the article. This cannot exceed 400KB in size.
    """
    article_body = ArticleBody(null=True)
    """
    URL for externally stored article body.
    """
    article_body_url = UnicodeAttribute(null=True)

