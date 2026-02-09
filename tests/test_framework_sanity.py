from framework.base.base_test import BaseTest


class TestFrameworkSanity(BaseTest):

    def test_base_url_loaded(self):
        assert self.base_url is not None
        self.logger.info("Framework sanity test passed")
