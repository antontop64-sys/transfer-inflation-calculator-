# Football Transfer Inflation Calculator

A Streamlit web app that estimates how historical football transfer fees compare to today's value in euros.

## Project structure

- `app.py` – Streamlit UI, input modes, result cards, chart, and top transfers table.
- `inflation_calculator.py` – year-by-year inflation calculation logic and inflation datasets.
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

- Two input modes:
  - **Manual input**
  - **Choose from top transfers** with searchable player dropdown
- Auto-filled player details in top transfer mode:
  - player name, transfer year, transfer fee, from club, to club
- Two inflation modes:
  - **Economic inflation**
  - **Football market inflation**
- Year-by-year compounding using dictionary-based yearly rate data (no fixed single annual rate)
- Styled result card showing:
  - player (if available)
  - original fee
  - transfer year
  - years passed
  - selected inflation mode
  - adjusted value today
  - transfer route (if available)
- Selected player info card
- Reset button
- Top transfers table with sorting by fee or year
- Value growth chart based on the selected inflation mode
