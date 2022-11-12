import dataclasses


@dataclasses.dataclass
class User:
    id: int
    name: str
    auth_key: str
