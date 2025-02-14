#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_exchange_rates_api import SourceExchangeRatesApi

if __name__ == "__main__":
    source = SourceExchangeRatesApi()
    launch(source, sys.argv[1:])
