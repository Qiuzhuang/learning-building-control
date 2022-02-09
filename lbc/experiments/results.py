import glob
import logging
import os
import pickle

import pandas as pd
import numpy as np


logging.basicConfig(level="INFO")
logger = logging.getLogger(__file__)


def main(dr):

    dirname = f"results-{dr}"
    print(dirname)
    files = glob.glob(os.path.join(dirname, "*.p"))
    files = sorted(files)
    logger.info(f" Found {len(files)} files: {files}")

    data = {}
    for f in files:
        with open(f, "rb") as x:
            _data = pickle.load(x)
            key = os.path.basename(f)
            result = {
                key: {
                    "test_loss": _data["mean_loss"],
                    "cpu_time": _data["cpu_time"]
                }
            }
            data.update(result)
            logger.info(result)

    df = pd.DataFrame(data).T
    df = df.sort_values("test_loss")
    print(df)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dr",
        type=str,
        help="DR program",
        choices=["TOU", "RTP", "PC"])
    a = parser.parse_args()

    _ = main(a.dr)


