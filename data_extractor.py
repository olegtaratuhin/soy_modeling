import random

import numpy as np

from labels_translator import *
from utils import Mask


def mask_features(features, mask=None):
    """
    Mask certain features based on mask parameters and allowed labels.
    Default mask is transparent. Used in auto optimization
    of feature set.

    :param features - list of data in certain observation
    :param mask - string of bits, '1' - for pass through and '0' - for block.

    :return list of masked features
    """

    if mask is None:
        mask = Mask()

    masked_features = list()

    for i, bit in enumerate(mask):
        if bit:
            masked_features.append(features[i])

    return masked_features


def extract(filename, mask=None):
    """
    Get data from file, split into features, mask them and
    format it for the training.
    Features are selected based on mask. Default mask is transparent.

    @return labels, data in tuple
    """

    data = list()
    labels = list()
    target = list()

    path = "./dataset/"
    with open(path + filename) as f:
        for line in f.readlines():
            if len(labels) == 0:
                if mask is None:
                    mask, labels = default_mask()

                continue
            observation = line.split(",")
            masked = mask_features(observation, mask)

            if (masked[0] == 'NA'):
                continue

            target.append(float(observation[get_target_index()]))
            features = [float(el) for el in masked]
            data.append(np.array(features))

    return labels, data, target


def default_mask():
    """
    Generate a default mask based on article and common statistical sense.

    :return mask and labels for them
    """
    allowed = [
        ConstantsTranslator.AVG_DLEN_SPR20,
        ConstantsTranslator.AVG_TEMP_SOWSPR,
        ConstantsTranslator.TIME_SOWSPR,
        ConstantsTranslator.AVG_RAIN_SOW10
        ]
    labels = get_labels_with_index(allowed)
    return Mask.generate_from_indexes(allowed), labels


def random_mask():
    """
    Generate a random mask with indexes and parameters
    from groups defined in ConstantsTranslator groups
    :return mask and labels for them
    """
    allowed = []

    allowed.extend(random.sample(ConstantsTranslator.GROUP_DLEN_SPRBLOS, 1))
    allowed.extend(random.sample(ConstantsTranslator.GROUP_RAIN_SPR, 1))
    allowed.extend(random.sample(ConstantsTranslator.GROUP_TEMP_SOW, 1))
    allowed.append(ConstantsTranslator.TIME_SOWSPR)

    labels = get_labels_with_index(allowed)

    return Mask.generate_from_indexes(allowed), labels


def get_target_index():
    return ConstantsTranslator.TIME_SOWBLOS
