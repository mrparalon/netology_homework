import unittest
from unittest import TestCase, skip, mock
from src.helpers.config import Config

import os



class TestConfig(TestCase):
    def test_init_env_config_path(self):
        #TODO попробовать unittest mock
        o = Config()
        WINDOWS = False
        APP_NAME = 'testapp'
        ENVIRONMENT_CONFIG_PATH = 'TEST_APP_CONFIG_PATH'
        USER_HOME_DIR = os.path.expanduser('~')
        TEST_APP_ROOT_DIR = './test'
        DEFAULT_CONFIG_PATH = ['./', ]
        a = Config.init_env_config_path()
        print(a)

class TestVerbosityLevel(TestCase):
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


class TestWindowsSystemDisk(TestCase):
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


if __name__ == "__main__":
    unittest.main()