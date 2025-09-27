#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher_ai.crew import FinancialResearcherAI

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the financial researcher crew
    """

    inputs = {
        'company':'NatWest'
    }

    result = FinancialResearcherAI().crew().kickoff(inputs=inputs)
    print(result.raw)


if __name__ == "__main__":
    run()