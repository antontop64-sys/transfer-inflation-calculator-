from __future__ import annotations

from datetime import datetime

import streamlit as st

from inflation_calculator import InflationMode, calculate_inflation_adjusted_value

CURRENT_YEAR = datetime.now().year

TOP_TRANSFERS = [
    {
        "player": "Neymar",
        "year": 2017,
        "fee": 222.0,
        "from_club": "Barcelona",
        "to_club": "PSG",
    },
    {
        "player": "Kylian Mbappe",
        "year": 2018,
        "fee": 180.0,
        "from_club": "Monaco",
        "to_club": "PSG",
    },
    {
        "player": "Philippe Coutinho",
        "year": 2018,
        "fee": 135.0,
        "from_club": "Liverpool",
        "to_club": "Barcelona",
    },
    {
        "player": "Joao Felix",
        "year": 2019,
        "fee": 126.0,
        "from_club": "Benfica",
        "to_club": "Atletico Madrid",
    },
    {
        "player": "Enzo Fernandez",
        "year": 2023,
        "fee": 121.0,
        "from_club": "Benfica",
        "to_club": "Chelsea",
    },
    {
        "player": "Antoine Griezmann",
        "year": 2019,
        "fee": 120.0,
        "from_club": "Atletico Madrid",
        "to_club": "Barcelona",
    },
    {
        "player": "Jack Grealish",
        "year": 2021,
        "fee": 117.5,
        "from_club": "Aston Villa",
        "to_club": "Manchester City",
    },
    {
        "player": "Cristiano Ronaldo",
        "year": 2009,
        "fee": 94.0,
        "from_club": "Manchester United",
        "to_club": "Real Madrid",
    },
    {
        "player": "Gareth Bale",
        "year": 2013,
        "fee": 101.0,
        "from_club": "Tottenham",
        "to_club": "Real Madrid",
    },
]

st.set_page_config(
    page_title="Football Transfer Inflation Calculator",
    page_icon="⚽",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1b1b1b 0%, #0f0f0f 40%, #090909 100%);
        color: #f5f5f5;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: 0.4px;
        margin-bottom: 0.25rem;
        color: #f8f8f8;
    }
    .subtitle {
        color: #c8c8c8;
        margin-bottom: 1.1rem;
        line-height: 1.45;
    }
    .card {
        background: #171717;
        border: 1px solid #2a2a2a;
        border-radius: 16px;
        padding: 1.2rem;
        margin: 0.9rem 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.32);
    }
    .result-card {
        background: linear-gradient(135deg, #103820 0%, #14532d 100%);
        border: 1px solid #1f7c45;
        border-radius: 16px;
        padding: 1.2rem;
        margin-top: 1rem;
    }
    .result-title {
        color: #d1fae5;
        font-size: 1rem;
        margin-bottom: 0.35rem;
    }
    .result-value {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 800;
    }
    .muted {
        color: #cfcfcf;
        font-size: 0.92rem;
    }
    .accent {
        color: #4ade80;
        font-weight: 700;
    }
    .info-title {
        color: #bbf7d0;
        font-size: 0.96rem;
        font-weight: 700;
        margin-bottom: 0.45rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">Football Transfer Inflation Calculator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Compare historical transfer fees in today\'s euros using either <span class="accent">economic inflation</span> or <span class="accent">football market inflation</span>.</div>',
    unsafe_allow_html=True,
)

if st.button("Reset", type="secondary"):
    st.session_state.clear()
    st.rerun()

st.markdown('<div class="card">', unsafe_allow_html=True)
input_mode = st.radio("Input Mode", ["Manual input", "Choose from top transfers"], horizontal=True)
selected_player_name = None
player_name = ""
from_club = ""
to_club = ""

if input_mode == "Choose from top transfers":
    selected_player_name = st.selectbox(
        "Search player",
        [transfer["player"] for transfer in TOP_TRANSFERS],
        index=0,
        help="Type in the box to quickly search a player.",
    )
    selected_transfer = next(
        transfer for transfer in TOP_TRANSFERS if transfer["player"] == selected_player_name
    )
    player_name = selected_transfer["player"]
    transfer_year = int(selected_transfer["year"])
    transfer_amount = float(selected_transfer["fee"])
    from_club = selected_transfer["from_club"]
    to_club = selected_transfer["to_club"]

    st.markdown(
        f"""
        <div class="card">
            <div class="info-title">Selected player info</div>
            <div><span class="muted">Player:</span> {player_name}</div>
            <div><span class="muted">Transfer:</span> {from_club} → {to_club}</div>
            <div><span class="muted">Year:</span> {transfer_year}</div>
            <div><span class="muted">Fee:</span> € {transfer_amount:,.2f} million</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    player_name = st.text_input("Player Name (optional)", value="")
    transfer_year = int(
        st.number_input(
            "Transfer Year",
            min_value=1990,
            max_value=CURRENT_YEAR,
            value=2017,
            step=1,
        )
    )
    transfer_amount = float(
        st.number_input(
            "Transfer Fee (million €)",
            min_value=0.01,
            value=50.0,
            step=0.1,
            format="%.2f",
        )
    )
    from_club = st.text_input("From Club (optional)", value="")
    to_club = st.text_input("To Club (optional)", value="")

mode: InflationMode = st.radio(
    "Inflation Mode",
    ["Economic inflation", "Football market inflation"],
    horizontal=True,
)

calculate = st.button("Calculate", use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card muted">
        <span class="accent">Economic inflation</span> reflects general price level changes in the broader economy.
        <br/>
        <span class="accent">Football market inflation</span> reflects transfer-market specific growth, which can rise or fall differently from consumer prices.
    </div>
    """,
    unsafe_allow_html=True,
)

if calculate:
    errors: list[str] = []
    if transfer_year < 1990 or transfer_year > CURRENT_YEAR:
        errors.append(f"Year must be between 1990 and {CURRENT_YEAR}.")
    if transfer_amount <= 0:
        errors.append("Transfer amount must be greater than 0.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        adjusted_value, years_passed, growth_points = calculate_inflation_adjusted_value(
            transfer_year=transfer_year,
            transfer_amount_million_eur=transfer_amount,
            mode=mode,
            current_year=CURRENT_YEAR,
        )

        player_line = (
            f"<div><span class='muted'>Player:</span> {player_name}</div>" if player_name.strip() else ""
        )
        clubs_line = (
            f"<div><span class='muted'>Route:</span> {from_club} → {to_club}</div>"
            if from_club.strip() and to_club.strip()
            else ""
        )

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Inflation-adjusted transfer value (today)</div>
                <div class="result-value">€ {adjusted_value:,.2f} million</div>
                {player_line}
                <div><span class="muted">Original transfer fee:</span> € {transfer_amount:,.2f} million</div>
                <div><span class="muted">Transfer year:</span> {transfer_year}</div>
                <div><span class="muted">Years passed:</span> {years_passed}</div>
                <div><span class="muted">Selected mode:</span> {mode}</div>
                {clubs_line}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Transfer value growth over time")
        chart_data = {
            "Year": [int(point["Year"]) for point in growth_points],
            "Adjusted value (€m)": [point["Value"] for point in growth_points],
        }
        st.line_chart(chart_data, x="Year", y="Adjusted value (€m)")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("#### Top Transfers")
sort_by = st.selectbox("Sort table by", ["Fee", "Year"], index=0)
if sort_by == "Fee":
    sorted_transfers = sorted(TOP_TRANSFERS, key=lambda item: item["fee"], reverse=True)
else:
    sorted_transfers = sorted(TOP_TRANSFERS, key=lambda item: item["year"], reverse=True)

st.dataframe(
    [
        {
            "Player": transfer["player"],
            "Year": transfer["year"],
            "Fee (€m)": transfer["fee"],
            "From Club": transfer["from_club"],
            "To Club": transfer["to_club"],
        }
        for transfer in sorted_transfers
    ],
    use_container_width=True,
    hide_index=True,
)
st.markdown('</div>', unsafe_allow_html=True)
