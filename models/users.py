from pynamodb.attributes import UnicodeAttribute

from .base import BaseModel


class UsersModel(BaseModel):
    """
    Table for Users
    """
    class Meta:
        table_name: str = "users"
        region: str = BaseModel.Meta.region
        host: str = BaseModel.Meta.host
        aws_access_key_id: str = BaseModel.Meta.aws_access_key_id
        aws_secret_access_key: str = BaseModel.Meta.aws_secret_access_key
        write_capacity_units: int = BaseModel.Meta.write_capacity_units
        read_capacity_units: int = BaseModel.Meta.read_capacity_units
    """
    Identifier of the user. A user can be directly
    retrieved using the ID [O(1) operation]
    """
    user_id = UnicodeAttribute(hash_key=True)
    """
    This is the type of user. E.g. medical institution, medical supply vendor, etc.
    It would be useful for range queries:
    https://aws.amazon.com/blogs/database/using-sort-keys-to-organize-data-in-amazon-dynamodb/
    """
    user_type = UnicodeAttribute(range_key=True)
    user_password = UnicodeAttribute()
    user_fullname = UnicodeAttribute()
    user_contact = UnicodeAttribute()

