# Football Transfer Inflation Calculator

A Streamlit web app that estimates how much a historical football transfer fee would be worth in today's money using **3% annual compound inflation**.

## Project structure

- `app.py` – Streamlit UI and app styling.
- `inflation_calculator.py` – inflation calculation logic.
- `requirements.txt` – Python dependencies.
- `README.md` – setup and run instructions.

## Installation

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

Then open the local URL printed by Streamlit (usually `http://localhost:8501`).

## Features

- Input validation:
  - Year must be between **1990** and the **current year**.
  - Transfer amount must be greater than **0**.
- Default inflation model: **3% compound annual inflation**.
- Includes a Neymar example transfer:
  - Year: **2017**
  - Fee: **€222 million**
