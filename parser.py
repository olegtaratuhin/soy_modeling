# -*- coding: utf-8 -*-
"""Parser definition file.

This file contains definition of parser. Parser is used to read
command-line arguments and configure launch.

Example:
    Parser import is defined as follows:

        from parser import Parser

        parser = Parser(sys.argv)
        configuration = parseer.get_configuration

Attributes:
    Parser (class): a command line arguments parser class.
    get_configuration (Configuration): get configuration from arguments.

Todo:
    * Add Parser implementation
    * Add configuration api
    * Add configuration implementation

"""


import argparse
import textwrap


class Parser(object):
    """
    Parser to wrap commandline parsing.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent("""
            Plant's analysis tool. Can calculate plant's state during sow to blossom,
            as well as blossom to harvest. Also can provide estimates on
            oil and protein, produced by plant to certain day.
            """),
            epilog="authored by SPbSTU IAMM compbio lab")

        self.parser.add_argument('--mode',
                            metavar='-M',
                            choices=['fit', 'predict'],
                            nargs=1,
                            required=True,
                            help="""
            Mode selector, to train a model pass 'fit', to use existing model pass 'predict'
            """)
        self.parser.add_argument('--target',
                            metavar='-T',
                            choices=['crop', 'bloom', 'protein', 'oil'],
                            nargs='+',
                            required=True,
                            help="""
            Target specifier, utility will run for each argument separately if multiple are passed
            """)
        self.parser.add_argument('--labels-data',
                            metavar='-Ld',
                            nargs=1,
                            required=True,
                            help=textwrap.dedent("""\
            File with labeled data to be enriched and used by model. Expected format is csv or hdf5.
            Table must have data in following format (exact names are expected), values marked as optionals
            may not be provided, but the ones that are included in target are mandatory.\
            \
            Name - name of the plant (must be consistent); \
            Place - name of the nearest meteo station (must be included in database file); \
            Sowing data - date of sow; \
            Crop date - date of crop; \
            Bloom date - date of bloom; \
            Sow to Crop - number of days between sow and crop (corresponds to 'crop' target option) -optional; \
            Crop to Bloom - number of days between crop and bloom (corresponds to 'bloom' target option) -optional; \
            Protein - milligrams of protein (corresponds to 'protein' target option) -optional; \
            Oil - milligrams of oil (corresponds to 'oil' target option) -optional; \
            """))

        self.parser.add_argument('--meteo-data',
                            metavar='-Md',
                            nargs=1,
                            required=True,
                            help=textwrap.dedent("""\
            File with meteo data to be labeled with provided labels data. Excepted foramt is csv or hdf5.
            Table must have data in following format (exact names are expected).\
            \
            Date - date of meteo record; \
            T_min - minimum temperature; \
            T_max - maximum temperature; \
            Precipitation - precipitation during day; \
            All sky - collective radiation; \
            Clear sky - radiation of clear sky; \
            """))

    def parse_args(self, *args):
        self.parsed_arguments = self.parser.parse_args()
        return self.parsed_arguments

    def get_configuration(self):
        pass
