from unittest import TestCase, skip
from src.helpers.config import Config

import os


class TestConfig(TestCase):
    def test_init_env_config_path(self):
        pass

    def test_get_verbosity_level(self):
        # Positive
        def test_level_none(self):
            levels = 'critical, error, warning, info, debug'
            self.assertEqual(Config.get_verbosity_level(level=None), levels, )

        def test_all_levels(self):
            self.assertEqual(Config.get_verbosity_level(level='console'), 10)
            self.assertEqual(Config.get_verbosity_level(level='debug'), 10)
            self.assertEqual(Config.get_verbosity_level(level='info'), 20)
            self.assertEqual(Config.get_verbosity_level(level='warning'), 30)
            self.assertEqual(Config.get_verbosity_level(level='error'), 40)
            self.assertEqual(Config.get_verbosity_level(level='critical'), 50)

        def test_text_level_capitalized(self):
            self.assertTrue(Config.get_verbosity_level(level=10, text=True).isupper())

        # Negative
        def test_wrong_level(self):
            self.assertEqual(Config.get_verbosity_level(level='wrong_str'), None)

    def test_get_windows_system_disk(self):
        def setUp(self):
            self.old_environ = os.environ.copy()
            new_environ = os.environ
            new_environ.clear()

        def tearDown(self):
            os.environ = self.old_environ

        def test_getenv(self):
            os.environ['SystemDrive'] = 'C:\\'
            self.assertEqual(Config.get_windows_system_disk(), 'C:\\')
            os.environ.clear()

        @skip('It raise because there is no win32api module\
                       and I dont know how to check it.')
        def test_not_windows(self):
            try:
                Config.get_windows_system_disk()
            except EnvironmentError:
                self.fail('Not Windows')

