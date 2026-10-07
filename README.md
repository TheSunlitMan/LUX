# LUX — Latin Dictionary API

LUX is a small REST API for learning Latin vocabulary.

The project is built with FastAPI and provides endpoints for viewing, searching and testing Latin words.

## Features

* Get all dictionary words
* Get a word by ID
* Search words by Latin or Russian translation
* Check translation with a quiz
* Get a random word
* Health and version endpoints
* Automated tests with pytest
* CI with GitHub Actions

## Requirements

* Python 3.12+
* pip

## Installation

Clone the repository and create a virtual environment:

```bash
python3 -m venv lux
source lux/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API endpoints

| Method | Endpoint                     | Description                  |
| ------ | ---------------------------- | ---------------------------- |
| GET    | `/health`                    | Service health check         |
| GET    | `/version`                   | Application name and version |
| GET    | `/words`                     | Get all words                |
| GET    | `/words/{word_id}`           | Get a word by ID             |
| GET    | `/search?q=...`              | Search the dictionary        |
| GET    | `/quiz/{word_id}?answer=...` | Check a translation          |
| GET    | `/random-word`               | Get a random word            |

## Examples

Get all words:

```text
GET /words
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

## Logging and diagnostics

The application writes information about API requests to the application log.

The `/health` endpoint can be used to check whether the service is running:

```text
GET /health
```

The `/version` endpoint returns the current application name and version:

```text
GET /version
```

## Testing

Run all automated tests with:

```bash
python -m pytest -v
```

The project includes tests for:

* health check
* application version
* retrieving words
* retrieving a word by ID
* handling an unknown word
* dictionary search
* correct quiz answers
* incorrect quiz answers

## Continuous Integration

GitHub Actions automatically runs the test suite for pushes to `main` and pull requests targeting `main`.

After successful tests, the tested application files are uploaded as a GitHub Actions artifact.

## Author

**Kirill Ialkovskii**

*HSE University · Applied Neural Networks*

📧 `kaialkovskii@edu.hse.ru`