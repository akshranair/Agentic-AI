#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_picker.crew import StockPicker


def run():
    """
    Run the research crew
    """


    inputs = {
        'sector': 'Technology'
    }

    result = StockPicker().crew().kickoff(inputs = inputs)

    print("\n\n ** Final Decision ** \n\n")

    print(result.raw)


if __name__ == "__main__":
    run()