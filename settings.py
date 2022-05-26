import logging
import os.path
import yaml
import copy


class Settings:
    """
        Settings extract the settings from yml config files and store the setting
    """

    def __init__(self, conf_file):
        """init for Setting
            Args :
                conf_file (path) : Path to configuration files
        """
        self.logger = logging.getLogger(__name__)
        self.setting_data = {}
        self.conf_file = ''
        self.sub_setting_path_list = []
        self.read_settings(conf_file)

    def __str__(self):
        return str(self.setting_data)

    def __eq__(self, other):
        if not isinstance(other, Settings):
            return False
        if self.setting_data == other.setting_data:
            return True
        return False

    def read_settings(self, conf_file):
        """Extract settings from settings file
            Args :
                conf_file (str) : path to source file for read settings
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if not os.path.isfile(conf_file):
            self.logger.error("Setting file doesn't exist: {} not found!".format(conf_file))
            return False
        _raw_setting_file = open(conf_file)
        _setting_data = yaml.load(_raw_setting_file, Loader=yaml.FullLoader)
        _raw_setting_file.close()
        if type(_setting_data) is dict:
            self.setting_data = _setting_data
            self.conf_file = conf_file
            return True
        else:
            self.logger.error("Invalid setting file : {} ".format(conf_file))
        return False

    def set_sub_setting_path(self, sub_setting_path_list):
        """Set the setting_path_list attribute for settings object
            Args :
                setting_path_list (list) : liste of the sub section for this object

            Returns :
            Note : sub_setting_path_list si use for define a default path to a key
        """
        if isinstance(sub_setting_path_list, list):
            self.sub_setting_path_list = sub_setting_path_list
            return True
        return False

    def get_setting(self, setting_path_list=None):
        """Getter for settings
            Args :
                setting_path_list (list) : liste of the sub section to get

            Returns :
                dict : The return value is the parameters or the subsection (dictionary).
        """
        if setting_path_list is None:
            setting_path_list = []
        _setting_dict = self.setting_data
        if isinstance(setting_path_list, list):
            _setting_path_list = copy.deepcopy(self.sub_setting_path_list)
            _setting_path_list.extend(setting_path_list)
            for _key in _setting_path_list:
                if type(_setting_dict) is dict:
                    try:
                        _setting_dict = _setting_dict[_key]
                    except KeyError:
                        #self.logger.warning("Invalid setting path list {} , "
                        #                  "Key {} not found!".format(_setting_path_list, _key))
                        _setting_dict = None
                else:
                    #self.logger.warning("Invalid setting path list {} , "
                    #                  "Key {} not found!".format(_setting_path_list, _key))
                    _setting_dict = None
        else:
            self.logger.error("{} , is not a list !".format(setting_path_list))
            _setting_dict = None
        return _setting_dict

    def get_setting_copy(self):
        return copy.deepcopy(self)
