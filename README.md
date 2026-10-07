# LUX — Latin Dictionary API

LUX is a small educational service for learning Latin vocabulary.

The project combines a **FastAPI REST API** with an **interactive Streamlit web interface**. It provides dictionary search, random vocabulary practice and a translation quiz.

## Features

* Get all dictionary words
* Get a word by ID
* Search words by Latin word or Russian translation
* Check translations with a quiz
* Get a random word
* Interactive Streamlit web interface
* Interactive vocabulary quiz without manual word ID input
* Health and version endpoints
* Application logging
* Automated tests with pytest
* Continuous Integration with GitHub Actions

## Project structure

```text
LUX/
├── app.py
├── streamlit_app.py
├── test_app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Requirements

* Python 3.12+
* pip

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/TheSunlitMan/LUX.git
cd LUX

python3 -m venv lux
source lux/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

### FastAPI

Start the API server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Streamlit

Open another terminal, activate the same virtual environment and run:

```bash
source lux/bin/activate
streamlit run streamlit_app.py
```

The Streamlit interface will be available at the address shown by Streamlit, usually:

```text
http://localhost:8501
```

The Streamlit interface provides:

* dictionary search;
* complete dictionary view;
* random Latin word with Russian translation;
* interactive translation quiz.

The FastAPI server must be running before using the Streamlit interface because the web interface communicates with the API.

## API endpoints

| Method | Endpoint                     | Description                  |
| ------ | ---------------------------- | ---------------------------- |
| GET    | `/health`                    | Service health check         |
| GET    | `/version`                   | Application name and version |
| GET    | `/words`                     | Get all dictionary words     |
| GET    | `/words/{word_id}`           | Get a word by ID             |
| GET    | `/search?q=...`              | Search the dictionary        |
| GET    | `/quiz/{word_id}?answer=...` | Check a translation          |
| GET    | `/random-word`               | Get a random word            |

## API examples

Get all words:

```text
GET /words
```

Get a word by ID:

```text
GET /words/1
```

Search for a word:

```text
GET /search?q=aqua
```

Check a translation:

```text
GET /quiz/1?answer=друг
```

Get a random word:

```text
GET /random-word
```

Example response:

```json
{
  "id": 1,
  "latin": "amicus",
  "translation": "друг",
  "part_of_speech": "существительное"
}
```

## Environment variables

The application supports the following environment variables:

* `APP_NAME` — application name
* `APP_VERSION` — application version

If they are not specified, default values are used.

Example:

```text
APP_NAME=Latin Dictionary
APP_VERSION=0.1.0
```

A template is provided in `.env.example`.

The `.env` file is ignored by Git and should not be committed if it contains local configuration or secrets.

## Logging and diagnostics

The application writes information about API requests to the application log.

The `/health` endpoint can be used to check whether the service is running:

```text
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

The `/version` endpoint returns the current application name and version:

```text
GET /version
```

Example response:

```json
{
  "name": "Latin Dictionary",
  "version": "0.1.0"
}
```

These endpoints can be used for basic service diagnostics.

## Testing

Run all automated tests with:

```bash
python -m pytest -v
```

The test suite covers:

* health check;
* application version;
* retrieving all words;
* retrieving a word by ID;
* handling an unknown word;
* dictionary search;
* correct quiz answers;
* incorrect quiz answers;
* random word response.

## Continuous Integration

GitHub Actions automatically runs the test suite for:

* pushes to `main`;
* pull requests targeting `main`.

The CI pipeline:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs dependencies from `requirements.txt`.
4. Runs the automated test suite.
5. Uploads the tested application as a GitHub Actions artifact.

The artifact contains the main application files, including the FastAPI API and Streamlit interface.

## Development workflow

The project is developed using Git feature branches and pull requests.

Each significant feature or improvement is developed in a separate branch, tested locally and merged into `main` through a pull request.

## Author

**Kirill Ialkovskii**

*HSE University · Applied Neural Networks*

📧 `kaialkovskii@edu.hse.ru`
