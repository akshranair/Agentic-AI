# FinancialResearcherAi Crew

This project utilizes the Crew AI framework to create a team of autonomous AI agents that work together to perform in-depth financial research and analysis on any given company.

1. The crew consists of two specialized agents:

2. A Researcher Agent that scours the internet for the latest news, financial reports, and market data.

3. An Analyst Agent that synthesizes the collected data into a comprehensive, easy-to-read report with an executive summary and market outlook.

## Features

* **Automated Research**: Automatically gathers up-to-date information about a specified company.
* **In-Depth Analysis**: Provides insightful analysis, including trends, challenges, and future outlook.
* **Sequential Task Processing**: Ensures a logical workflow where analysis is only performed after research is complete.
* **Customizable**: Easily change the target company, or modify the agents' goals and backstories in the configuration files.
* **Extensible**: Add new agents or tools to expand the crew's capabilities.

## Technology Stack

* **Framework**: Crew AI
* **LLM**: Requires an OpenAI API Key (or another compatible model)
* **Search Tool**: SerperDev for efficient, real-time search results.
* **Language**: Python 3.12+



## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/financial_researcher_ai/config/agents.yaml` to define your agents
- Modify `src/financial_researcher_ai/config/tasks.yaml` to define your tasks
- Modify `src/financial_researcher_ai/crew.py` to add your own logic, tools and specific args
- Modify `src/financial_researcher_ai/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the financial_researcher-ai Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The financial_researcher-ai Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the FinancialResearcherAi Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
