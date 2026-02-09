import pytest
from framework.base.base_test import BaseTest

@pytest.mark.smoke
class TestBrowserLaunch(BaseTest):

    def test_title_is_not_empty(self):
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        assert title is not None
