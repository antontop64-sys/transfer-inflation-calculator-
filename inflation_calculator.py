from __future__ import annotations

from datetime import datetime


def calculate_inflation_adjusted_value(
    transfer_year: int,
    transfer_amount_million_eur: float,
    annual_inflation_rate: float = 0.03,
    current_year: int | None = None,
) -> float:
    """Return the inflation-adjusted transfer value in million EUR.

    Uses compound inflation:
        adjusted = amount * (1 + rate) ** years_elapsed
    """
    year_now = current_year or datetime.now().year
    years_elapsed = year_now - transfer_year
    return transfer_amount_million_eur * (1 + annual_inflation_rate) ** years_elapsed
