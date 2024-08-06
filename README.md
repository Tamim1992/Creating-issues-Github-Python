# Automating GitHub Issue Creation Using Python

## Overview
This project leverages Python to automate the process of creating issues in a GitHub repository. It fetches data from an existing GitHub repository and, if necessary, from REDCap using its API. The data from REDCap is then used to create new issues in the GitHub repository.

## Features
- Fetches open issues from a specified GitHub repository.
- Retrieves data from REDCap if no issues are found on GitHub.
- Automatically creates new issues in GitHub based on REDCap data.
- Ensures that duplicate issues are not created by checking existing issues.

## Instructions

### Prerequisites
- Python 3.x installed. For installation instructions, visit [Python Installation Guide](https://www.python.org/downloads/).
- `pip` package installer. For installation instructions, visit [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/).

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Demo.git
    cd Demo
    ```

2. Install the required Python packages:
    ```bash
    pip install requests
    ```

### Configuration
1. Update the `GITHUB_OWNER`, `GITHUB_REPO`, and `GITHUB_TOKEN` variables in the script with your GitHub repository details and personal access token.

2. Provide the REDCap API token in the `get_redcap_data` function payload.

### Usage
1. Run the script:
    ```bash
    python script.py
    ```

2. The script will:
   - Fetch open issues from the specified GitHub repository.
   - If no open issues are found, it will fetch data from REDCap.
   - Create new issues in the GitHub repository based on the REDCap data.
   - Avoid creating duplicate issues by checking existing issues.
