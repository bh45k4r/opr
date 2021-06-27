from pynamodb.attributes import UnicodeAttribute, ListAttribute

from .base import BaseModel


class QuestionnairesModel(BaseModel):
    """
    Table for Questionnaires
    """
    class Meta:
        table_name: str = "questionnaires"
        region: str = BaseModel.Meta.region
        host: str = BaseModel.Meta.host
        aws_access_key_id: str = BaseModel.Meta.aws_access_key_id
        aws_secret_access_key: str = BaseModel.Meta.aws_secret_access_key
        write_capacity_units: int = BaseModel.Meta.write_capacity_units
        read_capacity_units: int = BaseModel.Meta.read_capacity_units
    """
    Identifier of the questionnaire. A questionnaire can be directly
    retrieved using the ID [O(1) operation]
    """
    questionnaire_id = UnicodeAttribute(hash_key=True)
    """
    This is the type of questionnaire. E.g. medical institution, medical supply vendor, etc.
    It would be useful for range queries:
    https://aws.amazon.com/blogs/database/using-sort-keys-to-organize-data-in-amazon-dynamodb/
    """
    questionnaire_type = UnicodeAttribute(range_key=True)
    questionnaire_title = UnicodeAttribute()
    questionnaire_card_title = UnicodeAttribute()
    questionnaire_card_subtitle = UnicodeAttribute()
    questionnaire_card_text = ListAttribute(of=UnicodeAttribute)

