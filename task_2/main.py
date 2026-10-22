from api import Cat, Api
import faker
from random import randint, choice



if __name__ == "__main__":
    api = Api()
    fake_data = faker.Faker()
    features = ["eat a lot", "sleep a lot", "poops a lot"]
    cats = [Cat(fake_data.name(), randint(1, 15), [choice(features)]) for _ in range(10)]

    # Call one time to fill DB
    # for cat in cats:
    #     api.add_cat(cat)

    print(api.get_all_cats())
    print(api.get_cat_info("Monica Sloan"))

    api.update_cat_age("Monica Sloan", 3)
    api.add_cat_feature("Monica Sloan", "bark")

    api.remove_cat("Nicholas Cook")