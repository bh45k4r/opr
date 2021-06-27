from pynamodb.models import Model


class BaseModel(Model):
    """
    This is the base class which should be inherited by all model subclasses
    """
    class Meta:
        # subclass should set these
        table_name: str = ""
        region: str = "localhost"
        host: str = "http://127.0.0.1:8000"
        aws_access_key_id: str = "fakeMyKeyId"
        aws_secret_access_key: str = "fakeSecretAccessKey"
        write_capacity_units: int = 10
        read_capacity_units: int = 10

