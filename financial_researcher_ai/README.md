Financial Researcher AI CrewThis project utilizes the Crew AI framework to create a team of autonomous AI agents that work together to perform in-depth financial research and analysis on any given company.The crew consists of two specialized agents:A Researcher Agent that scours the internet for the latest news, financial reports, and market data.An Analyst Agent that synthesizes the collected data into a comprehensive, easy-to-read report with an executive summary and market outlook.FeaturesAutomated Research: Automatically gathers up-to-date information about a specified company.In-Depth Analysis: Provides insightful analysis, including trends, challenges, and future outlook.Sequential Task Processing: Ensures a logical workflow where analysis is only performed after research is complete.Customizable: Easily change the target company, or modify the agents' goals and backstories in the configuration files.Extensible: Add new agents or tools to expand the crew's capabilities.Technology StackFramework: Crew AILLM: Requires an OpenAI API Key (or another compatible model)Search Tool: SerperDev for efficient, real-time search results.Language: Python 3.12+Setup and InstallationFollow these steps to get the project up and running on your local machine.1. Clone the Repositorygit clone [https://github.com/your-username/financial_researcher_ai.git](https://github.com/your-username/financial_researcher_ai.git)
cd financial_researcher_ai
2. Create a Virtual EnvironmentIt's highly recommended to use a virtual environment to manage project dependencies.# Create the virtual environment
python3 -m venv .venv

# Activate it (on macOS/Linux)
source .venv/bin/activate

# On Windows
# .venv\Scripts\activate
3. Install DependenciesThe crewai command-line tool uses uv to manage dependencies, which are listed in the pyproject.toml file.crewai install
If you prefer pip, you can install the required packages manually:pip install crewai crewai-tools python-dotenv
4. Set Up API KeysThis is the most important step. The agents need API keys to access the language model (OpenAI) and the search tool (Serper).Create a new file named .env in the root directory of your project.Add your API keys to the .env file in the following format:# .env

# Get your key from: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
OPENAI_API_KEY="sk-..."

# Get your key from: [https://serper.dev/api-key](https://serper.dev/api-key)
SERPER_API_KEY="..."
Note: The .env file is included in .gitignore to ensure your secret keys are not accidentally committed to a public repository.How to RunSet the Target Company: Open the src/financial_researcher_ai/main.py file and change the company name in the inputs dictionary.# src/financial_researcher_ai/main.py

def run():
    """
    Run the financial researcher crew
    """
    inputs = {
        'company': 'NVIDIA'  # <-- Change this to any company you want
    }
    FinancialResearcherAI().crew().kickoff(inputs=inputs)
Run the Crew: Execute the following command from your terminal (make sure your virtual environment is activated).crewai run
The agents will begin their tasks, and you will see their progress printed to the console. The final report will be displayed at the end of the process.Customizing the CrewYou can easily modify the behavior of the agents and tasks by editing the YAML configuration files:config/agents.yaml: Change the role, goal, and backstory of each agent to alter their personality and focus.config/tasks.yaml: Modify the description and expected_output for each task to change what the agents are instructed to do.LicenseThis project is licensed under the MIT License. See the LICENSE file for more details.