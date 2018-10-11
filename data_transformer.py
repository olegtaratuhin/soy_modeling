# This file contains methods to transform initial data to
# approximate data semantics described in article
import pandas as pd


class Data_transformer_abstract(object):
    """
    Abstract data transformer class as a template to be overridden.

    To implement custom version of predictors one must override
    transform_t_max, transform_t_min, transform_avg_dlen and provide
    your own realisation.
    """

    @classmethod
    def transform_avg_dlen(cls, table_daily, row):
        """
        Transform average day length.

        Example usage: pd.apply(function=transform_avg_dlen, axis=1,
         result_type='expand')
        """
        pass

    @classmethod
    def transform_t_min(cls, table_daily, row):
        """
        Transform min temperature values.

        Example usage: pd.apply(function=transform_t_min, axis=1,
         result_type='expand')
        """
        pass

    @classmethod
    def transform_t_max(cls, table_daily, row):
        """
        Transform max temperature values.

        Example usage: pd.apply(function=transform_t_min, axis=1,
         result_type='expand')
        """
        pass


class Data_transformer(Data_transformer_abstract):
    """
    Data transformer subclass overriding abstract data transformer.

    implementation is dona according to the publication.
    """

    # Maximum temperature estimation
    T_c_max = 23

    # Minimum temperature estimation
    T_c_min = 12

    # Average photoperiod estimation
    g_c = 13

    # Heaviside function
    H = lambda x: 1 if x >= 0 else 0

    @classmethod
    def set_t_max(cls, avg_t_max):
        """Setter for avg_t_max threshold parameter."""
        cls.T_c_max = avg_t_max

    @classmethod
    def set_t_min(cls, avg_t_min):
        """Setter for avg_t_min threshold parameter."""
        cls.T_c_min = avg_t_min

    @classmethod
    def set_g(cls, day_length):
        """Setter for day_length thresold parameter."""
        cls.g_c = day_length

    @classmethod
    def transform_avg_dlen(cls, arr):
        """Transform average day length."""
        return sum([cls.H(t - cls.g_c) * (t - cls.g_c) for t in arr]) / 80


    @classmethod
    def transform_t_min(cls, arr):
        """Transform min temperature values."""
        return sum([cls.H(t - cls.T_c_min) * (t - cls.T_c_min) for t in arr]) / 80

    @classmethod
    def transform_t_max(cls, arr):
        """Transform max temperature values."""
        return sum([cls.H(t - cls.T_c_max) * (t - cls.T_c_max) for t in arr]) / 80
