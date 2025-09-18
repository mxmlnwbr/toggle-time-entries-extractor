# Toggl Time Entries Extractor

A simple Python utility to extract time entries from the Toggl Track API and save them as JSON files.

## Description

This tool connects to the Toggl Track API, retrieves your time entries, and saves them to a local JSON file. It's useful for data backup, analysis, or integration with other tools that can process the exported data.

## Features

- Authenticates with the Toggl Track API using your API token
- Retrieves all time entries from your Toggl account
- Saves each time entry as a JSON object in a newline-delimited file
- Simple to run with minimal configuration

## Prerequisites

- Python 3.12 or higher
- A Toggl Track account and API token

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mxmlnwbr/toggle-time-entries-extractor.git
   cd toggle-time-entries-extractor
   ```

2. Install dependencies using uv:
   ```
   uv sync
   ```

3. Create a `.env` file in the root directory with your Toggl API token:
   ```
   API_TOKEN=your_toggl_api_token
   ```

## Usage

Run the script with uv:

```
uv run python main.py
```

The script will create a `data` directory (if it doesn't exist) and save your time entries to `data/time_entries.json`.

## Getting Your Toggl API Token

1. Log in to your Toggl Track account
2. Go to your Profile settings
3. Scroll down to the API Token section
4. Copy your API token

## Output Format

The output file is a newline-delimited JSON file, where each line contains one time entry from your Toggl account.

## Dependencies

- python-dotenv: For loading environment variables
- requests: For making API calls

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
