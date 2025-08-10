## Description
Automated test that:
1. Opens the website https://events.shooters.global/
2. Clicks the "Build for free" button
3. Logs in with a predefined user
4. Waits for the white canvas in the builder to load
5. Logs out of the account

## Requirements
- Python 3.8 or newer  
- Playwright >= 1.30.0  
- pytest  
- Internet connection to access the site

> **Note:** If Python is not installed, download it from the [official website](https://www.python.org/downloads/).

## Installation

```bash
git clone https://github.com/invalidrep/test_task.git
cd test_task

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```
## Running Tests

### Run all tests
pytest -s

### Run a specific test
pytest -s tests/test_login_builder.py

## Project Structure

pages/ — Page Object Models

tests/ — Test files

conftest.py — pytest fixtures

requirements.txt — dependencies

README.md — this file