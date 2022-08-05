import logging
import os.path
from src.settings import Settings
from abc import ABC, abstractmethod


class Element:
    """
        Element is global object
    """
    SETTING_PATH_ROOT = "ELEMENT"
    SETTING_DEFAULT_NAME = "DEFAULT"
    VERSION = "NC"

    def __init__(self, settings, name):
        """init for Element
            Args :
                setting (Settings, str) : setting for Element or path to the setting file
                name (str) : name of the configuration in setting file
        """
        # Init
        self.logger = logging.getLogger(__name__)
        self.local_setting = None
        self.name = None
        if name is None or name == "":
            name = "DEFAULT"

        self.str = self.__class__.__name__ + " : "
        self.setting_status = False

        self.local_setting = self._get_setting_obj_from_param(settings)
        if isinstance(self.local_setting, Settings):
            self.local_setting.set_sub_setting_path([self.SETTING_PATH_ROOT])
            if isinstance(name, str):
                if name in self.local_setting.get_setting([]).keys():
                    self.name = name
                    self.str += self.name

    def __str__(self):
        return str(self.str)

    def _get_setting_val(self, var_name):
        value = self.local_setting.get_setting([self.name, var_name])
        if value is None:
            value = self.local_setting.get_setting([self.SETTING_DEFAULT_NAME, var_name])
        return value

    def _check_settings(self):
        """load the settings value for class source
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if self.local_setting is None:
            return False
        if self.name is None:
            return False
        return True

    def get_name(self):
        """get_name get name value
            Args :
            Returns :
                name (float) : return name value
        """
        return self.name

    def get_version(self):
        """get_name get name value
            Args :
            Returns :
                name (float) : return name value
        """
        return self.VERSION

    def _gen_element_object(self, obj_var, setting=None):
        """set_source set source value
            Args :
                source (source or str) : source or sournce name in setting file
                setting :
            Returns :
                obj_type : return the element to set
        """
        if isinstance(obj_var, self.__class__):
            return obj_var
        elif isinstance(obj_var, str):
            setting = self._get_setting_obj_from_param(setting)
            if setting is None:
                setting = self.local_setting

            return self.__class__(setting, obj_var)
        self.logger.warning("Invalid argument source must be a source "
                            "object or the name of a configured source ".format(obj_var))
        return None

    @staticmethod
    def _get_setting_obj_from_param(settings):
        setting_out = None
        if settings is None:
            setting_out = None
        elif isinstance(settings, Settings):
            setting_out = settings.get_setting_copy()
        elif isinstance(settings, str):
            if os.path.isfile(os.path.abspath(settings)):
                setting_out = Settings(settings)

        return setting_out

