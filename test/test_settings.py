from .. import settings
import os.path


def test_set_setting_obj_ok():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.conf_file != ""


def test_set_setting_obj_not_file():
    conf_file = "./include/test/file_not_exist.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.conf_file == ""


def test_read_settings_ok():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.read_settings(conf_file)


def test_read_settings_not_file():
    conf_file = "./include/test/file_not_exist.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert not setting.read_settings(conf_file)


def test_read_settings_bad_file():
    conf_file = "./include/test/__init__.py"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert not setting.read_settings(conf_file)


def test_get_settings_all():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = []
    res = setting.get_setting(setting_path_list)
    assert res == setting.setting_data


def test_get_settings_subsection1():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["subsection1"]
    res = setting.get_setting(setting_path_list)
    assert res == {'key2': 'value2', 'key3': 'value3', 'subsection2': {'key4': 'value4', 'key5': 'value5'}}


def test_get_settings_subsection2():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["subsection1", "subsection2"]
    res = setting.get_setting(setting_path_list)
    assert res == {'key4': 'value4', 'key5': 'value5'}


def test_get_settings_list():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["list1",]
    res = setting.get_setting(setting_path_list)
    assert res == ['value1', 'value2', 'value3']


def test_get_settings_subsection_not_key():
    conf_file = "./include/test/test_settings_conf.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["subsection1", "not_a_key"]
    res = setting.get_setting(setting_path_list)
    assert res is None
