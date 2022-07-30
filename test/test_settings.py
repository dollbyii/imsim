from src import settings
import os.path


def test_set_setting_obj_ok():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.conf_file != ""


def test_set_setting_obj_not_file():
    conf_file = "./imsim_conf_unitest2.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.conf_file == ""


def test_read_settings_ok():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert setting.read_settings(conf_file)


def test_read_settings_not_file():
    conf_file = "./imsim_conf_unitest2.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert not setting.read_settings(conf_file)


def test_read_settings_bad_file():
    conf_file = "./include/test/test_settings.py"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    assert not setting.read_settings(conf_file)


def test_get_settings_all():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = []
    res = setting.get_setting(setting_path_list)
    assert res == setting.setting_data


def test_get_settings_subsection1():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["OBSERVATORY"]
    res = setting.get_setting(setting_path_list)
    assert res == {'DEFAULT': {'atmosphere_transmission': 0.5,'elevation': 65,'lunar_age': 0,
                               'photometric_band': 'V','seeing': 3.0},'myobservatory':
        {'atmosphere_transmission': 0.5,'elevation': 65,'seeing': 1.0,'sky_brightness': 21.0}}


def test_get_settings_subsection2():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["OBSERVATORY", "DEFAULT"]
    res = setting.get_setting(setting_path_list)
    assert res == {'atmosphere_transmission': 0.5, 'elevation': 65, 'lunar_age': 0, 'photometric_band': 'V',
                   'seeing': 3.0}


def test_get_settings_list():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["IMSIM", "test", "FILTER"]
    res = setting.get_setting(setting_path_list)
    assert res == ['C', 'V']


def test_get_settings_subsection_not_key():
    conf_file = "./imsim_conf_unitest.yml"
    conf_file = os.path.abspath(conf_file)
    setting = settings.Settings(conf_file)
    setting_path_list = ["subsection1", "not_a_key"]
    res = setting.get_setting(setting_path_list)
    assert res is None
