import unittest
from parser import Parser
import argparse

class ParserTest(unittest.TestCase):

    def test_help(self):
        parser = Parser()
        command = '-h'
        expected = """usage: main.py [-h] --mode -M --target -T [-T ...] --labels-data -Ld
               --meteo-data -Md

Plant's analysis tool. Can calculate plant's state during sow to blossom,
as well as blossom to harvest. Also can provide estimates on
oil and protein, produced by plant to certain day.

optional arguments:
  -h, --help            show this help message and exit
  --mode -M             Mode selector, to train a model pass 'fit', to use
                        existing model pass 'predict'
  --target -T [-T ...]  Target specifier, utility will run for each argument
                        separately if multiple are passed
  --labels-data -Ld     File with labeled data to be enriched and used by
                        model. Expected format is csv or hdf5. Table must have
                        data in following format (exact names are expected),
                        values marked as optionals may not be provided, but
                        the ones that are included in target are mandatory.
                        Name - name of the plant (must be consistent); Place -
                        name of the nearest meteo station (must be included in
                        database file); Sowing data - date of sow; Crop date -
                        date of crop; Bloom date - date of bloom; Sow to Crop
                        - number of days between sow and crop (corresponds to
                        'crop' target option) -optional; Crop to Bloom -
                        number of days between crop and bloom (corresponds to
                        'bloom' target option) -optional; Protein - milligrams
                        of protein (corresponds to 'protein' target option)
                        -optional; Oil - milligrams of oil (corresponds to
                        'oil' target option) -optional;
  --meteo-data -Md      File with meteo data to be labeled with provided
                        labels data. Excepted foramt is csv or hdf5. Table
                        must have data in following format (exact names are
                        expected). Date - date of meteo record; T_min -
                        minimum temperature; T_max - maximum temperature;
                        Precipitation - precipitation during day; All sky -
                        collective radiation; Clear sky - radiation of clear
                        sky;

authored by SPbSTU IAMM compbio lab"""
        actual = parser.parse_args(command)
        self.assertEquals(actual, expected)

    def test_basic(self):
        parser = Parser()
        command = '--mode fit --target protein --labels-data dataset/dates_dataset_raw.csv --meteo-data dataset/database/kuban'.split(' ')
        expected = argparse.Namespace(labels_data=['dataset/dates_dataset_raw.csv'], meteo_data=[
                             'dataset/database/kuban'], mode=['fit'], target=['protein'])
        actual = parser.parse_args(command)

        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()