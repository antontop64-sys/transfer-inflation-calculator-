from __future__ import annotations

from datetime import datetime

import streamlit as st

from inflation_calculator import calculate_inflation_adjusted_value

CURRENT_YEAR = datetime.now().year

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
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
        color: #f8f8f8;
    }
    .subtitle {
        color: #cfcfcf;
        margin-bottom: 1.25rem;
    }
    .card {
        background: #171717;
        border: 1px solid #2a2a2a;
        border-radius: 18px;
        padding: 1.25rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }
    .result-card {
        background: linear-gradient(135deg, #103820 0%, #14532d 100%);
        border: 1px solid #1e7a43;
        border-radius: 18px;
        padding: 1.25rem;
        margin-top: 1rem;
    }
    .result-title {
        color: #d1fae5;
        font-size: 1rem;
        margin-bottom: 0.4rem;
    }
    .result-value {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 800;
    }
    .example {
        font-size: 0.95rem;
        color: #d6d6d6;
    }
    .accent {
        color: #4ade80;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">Football Transfer Inflation Calculator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Estimate how historical transfer fees compare to today\'s money using 3% annual compound inflation.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="card">', unsafe_allow_html=True)
transfer_year = st.number_input(
    "Transfer Year",
    min_value=1990,
    max_value=CURRENT_YEAR,
    value=2017,
    step=1,
)
transfer_amount = st.number_input(
    "Transfer Fee (million €)",
    min_value=0.01,
    value=50.0,
    step=0.1,
    format="%.2f",
)
calculate = st.button("Calculate", use_container_width=True, type="primary")
st.markdown('</div>', unsafe_allow_html=True)

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
        adjusted_value = calculate_inflation_adjusted_value(
            transfer_year=int(transfer_year),
            transfer_amount_million_eur=float(transfer_amount),
        )
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">Inflation-adjusted transfer value</div>
                <div class="result-value">€ {adjusted_value:,.2f} million</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="card example">
        <div class="accent">Example: Neymar</div>
        <div>Year: 2017</div>
        <div>Transfer fee: €222 million</div>
    </div>
    """,
    unsafe_allow_html=True,
)
