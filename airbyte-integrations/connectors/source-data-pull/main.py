#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_data_pull import SourceDataPull

if __name__ == "__main__":
    source = SourceDataPull()
    launch(source, sys.argv[1:])
