from pynamodb.attributes import MapAttribute, UnicodeAttribute, ListAttribute

from .base import BaseModel


class SuppliesModel(BaseModel):
    """
    Table for Supplies
    """
    class Meta:
        table_name: str = "supplies"
        region: str = BaseModel.Meta.region
        host: str = BaseModel.Meta.host
        aws_access_key_id: str = BaseModel.Meta.aws_access_key_id
        aws_secret_access_key: str = BaseModel.Meta.aws_secret_access_key
        write_capacity_units: int = BaseModel.Meta.write_capacity_units
        read_capacity_units: int = BaseModel.Meta.read_capacity_units
    """
    Identifier of the supplies. An supplies can be directly
    retrieved using the ID [O(1) operation].
    """
    supplies_id = UnicodeAttribute(hash_key=True)
    """
    This is the type of supplies. E.g. ppe, oxygen, mask, etc.
    It would be useful for range queries:
    https://aws.amazon.com/blogs/database/using-sort-keys-to-organize-data-in-amazon-dynamodb/
    """
    supplies_type = UnicodeAttribute(range_key=True)
    """
    This is whether the supplies are being offered or requested. Medical
    supply vendors would use the former and medical institution would use the
    latter
    """
    supplies_state = UnicodeAttribute()
    # When was it offered or requested
    supplies_state_date = UnicodeAttribute()
    supplies_description = UnicodeAttribute()
    # Hash key of the supplier or requester
    supplies_users_user_id = UnicodeAttribute()

