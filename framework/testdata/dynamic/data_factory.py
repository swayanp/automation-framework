from faker import Faker
import uuid


class DataFactory:
    faker = Faker()

    @staticmethod
    def random_username():
        return f"user_{uuid.uuid4().hex[:6]}"

    @staticmethod
    def random_email():
        return DataFactory.faker.email()

    @staticmethod
    def random_password():
        return DataFactory.faker.password()
