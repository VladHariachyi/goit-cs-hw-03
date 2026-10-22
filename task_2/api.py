from dataclasses import dataclass, asdict

from db_connection import db

@dataclass
class Cat:
    name: str
    age: int
    features: list[str]


class Api:
    def add_cat(self, cat: Cat) -> None:
        db.all_cats.insert_one(asdict(cat))

    def get_all_cats(self) -> list[Cat]:
        return list(db.all_cats.find({}))

    def get_cat_info(self, cat_name: str) -> Cat | None:
        return db.all_cats.find_one({ "name": cat_name })

    def update_cat_age(self, cat_name: str, age: int) -> None:
        db.all_cats.update_one({ "name": cat_name }, { "$set": { "age": age } })

    def add_cat_feature(self, cat_name: str, feature: str) -> None:
        db.all_cats.update_one({ "name": cat_name }, { "$push": { "features": feature } })

    def remove_cat(self, cat_name: str) -> None:
        db.all_cats.delete_one({ "name": cat_name })

    def remove_all_cats(self) -> None:
        db.all_cats.delete_many({})


