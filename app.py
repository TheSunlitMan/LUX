import logging
import os
import random

from fastapi import FastAPI, HTTPException, Query


# -------------------------
# Configuration
# -------------------------

APP_NAME = os.getenv("APP_NAME", "Latin Dictionary")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")


# -------------------------
# Logging
# -------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# -------------------------
# Application
# -------------------------

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="A small API for learning Latin vocabulary.",
)


# -------------------------
# Data
# -------------------------

WORDS = [
    {
        "id": 1,
        "latin": "amicus",
        "translation": "друг",
        "part_of_speech": "существительное",
    },
    {
        "id": 2,
        "latin": "aqua",
        "translation": "вода",
        "part_of_speech": "существительное",
    },
    {
        "id": 3,
        "latin": "vita",
        "translation": "жизнь",
        "part_of_speech": "существительное",
    },
    {
        "id": 4,
        "latin": "amare",
        "translation": "любить",
        "part_of_speech": "глагол",
    },
    {
        "id": 5,
        "latin": "bellum",
        "translation": "война",
        "part_of_speech": "существительное",
    },
]


# -------------------------
# Service endpoints
# -------------------------

@app.get("/health")
def health_check():
    """Return service health status."""
    logger.info("Health check requested")

    return {
        "status": "ok",
    }


@app.get("/version")
def get_version():
    """Return application version."""
    logger.info("Version requested")

    return {
        "name": APP_NAME,
        "version": APP_VERSION,
    }


# -------------------------
# Dictionary endpoints
# -------------------------

@app.get("/words")
def get_words():
    """Return all dictionary words."""
    logger.info("Returning %d words", len(WORDS))

    return {
        "count": len(WORDS),
        "words": WORDS,
    }


@app.get("/words/{word_id}")
def get_word(word_id: int):
    """Return a word by its ID."""
    logger.info("Searching for word with id=%d", word_id)

    for word in WORDS:
        if word["id"] == word_id:
            return word

    logger.warning("Word with id=%d was not found", word_id)

    raise HTTPException(
        status_code=404,
        detail="Word not found",
    )


@app.get("/search")
def search_words(
    q: str = Query(
        min_length=1,
        description="Search query",
    ),
):
    """Search words by Latin name or translation."""
    logger.info("Search query: %s", q)

    query = q.lower()

    results = [
        word
        for word in WORDS
        if query in word["latin"].lower()
        or query in word["translation"].lower()
    ]

    return {
        "query": q,
        "count": len(results),
        "results": results,
    }


# -------------------------
# Learning functionality
# -------------------------

@app.get("/quiz/{word_id}")
def check_translation(
    word_id: int,
    answer: str = Query(
        min_length=1,
        description="Your translation",
    ),
):
    """Check whether the supplied translation is correct."""
    logger.info("Quiz request for word_id=%d", word_id)

    word = next(
        (word for word in WORDS if word["id"] == word_id),
        None,
    )

    if word is None:
        logger.warning("Quiz requested for unknown word_id=%d", word_id)

        raise HTTPException(
            status_code=404,
            detail="Word not found",
        )

    correct = answer.strip().lower() == word["translation"].lower()

    logger.info(
        "Quiz result for word_id=%d: correct=%s",
        word_id,
        correct,
    )

    return {
        "word": word["latin"],
        "answer": answer,
        "correct": correct,
    }


@app.get("/random-word")
def get_random_word():
    """Return a random word without its translation."""
    word = random.choice(WORDS)

    logger.info("Random word selected: %s", word["latin"])

    return {
        "id": word["id"],
        "latin": word["latin"],
        "part_of_speech": word["part_of_speech"],
    }