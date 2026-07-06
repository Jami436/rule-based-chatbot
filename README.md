# Rule-Based AI Guardrail & Chatbot Engine

## Overview

A deterministic chatbot built for the DecodeLabs Internship onboarding project.

The project demonstrates a modular architecture based on the Input → Process → Output (IPO) model and introduces a guardrail layer for deterministic input validation.

---

## Features

- Rule-based chatbot
- Deterministic responses
- Input normalization
- Input validation (Guardrails)
- Graceful exit commands
- Automated unit testing
- Modular architecture

---

## Project Structure

rule-based-chatbot/
│
├── app/
├── tests/
├── main.py
└── README.md

---

## Architecture

User Input
     │
     ▼
Guardrail Layer
     │
     ▼
Normalization
     │
     ▼
Intent Matching
     │
     ▼
Response Engine

---

## Running

python main.py

---

## Testing

python -m unittest discover tests

---

## Tech Stack

- Python 3
- unittest

---

## Future Improvements

- Regex-based intent matching
- Configuration via JSON
- Logging to file
- More guardrails