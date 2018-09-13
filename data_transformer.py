# This file contains methods to transform initial data to
# approximate data semantics described in article
import pandas as pd
from labels_translator import ConstantsTranslator as translator

class Data_transformer(object):
    """
    Data transformer class applies data transformation on
    pandas table columns based on labels they have
    """

    # Maximum temperature estimation
    T_c_max = 30

    # Minimum temperature estimation
    T_c_min = 5

    # Average photoperiod estimation
    g_c = 12

    # Heaviside function
    H = lambda x: 1 if x >= T_c_max else 0

    @classmethod
    def set_t_max(cls, avg_t_max):
        T_c_max = avg_t_max

    @classmethod
    def set_t_min(cls, avg_t_min):
        T_c_min = avg_t_min

    @classmethod
    def set_g(cls, day_length):
        g_c = day_length

    @classmethod
    def _transform_avg_dlen(cls, table):
        pass

    @classmethod
    def _transform_time(cls, table):
        pass

    @classmethod
    def _transform_avg_rain(cls, table):
        pass

    @classmethod
    def _transform_t(cls, table):
        pass
