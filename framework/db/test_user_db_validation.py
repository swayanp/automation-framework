import pytest
from framework.base.api_base_test import APIBaseTest
from framework.db.db_client import DBClient
from framework.testdata.dynamic.data_factory import DataFactory


@pytest.mark.db
class TestUserDBValidation(APIBaseTest):

    def test_user_inserted_into_db(self):
        db = DBClient()

        username = DataFactory.random_username()
        email = DataFactory.random_email()

        insert_query = """
        INSERT INTO users (username, email)
        VALUES (%s, %s)
        """
        db.execute_update(insert_query, (username, email))

        select_query = """
        SELECT username, email FROM users WHERE username = %s
        """
        result = db.execute_query(select_query, (username,))

        assert result[0][0] == username
        assert result[0][1] == email

        db.rollback()
        db.close()
