from __future__ import annotations

from datetime import datetime
from typing import Literal

InflationMode = Literal["Economic inflation", "Football market inflation"]

# Yearly rates used for compounding from transfer year -> current year.
# Values are decimal percentages (e.g. 0.028 = 2.8%).
ECONOMIC_INFLATION_RATES: dict[int, float] = {
    1990: 0.051,
    1991: 0.047,
    1992: 0.034,
    1993: 0.030,
    1994: 0.029,
    1995: 0.027,
    1996: 0.024,
    1997: 0.019,
    1998: 0.014,
    1999: 0.012,
    2000: 0.021,
    2001: 0.024,
    2002: 0.022,
    2003: 0.020,
    2004: 0.021,
    2005: 0.022,
    2006: 0.023,
    2007: 0.024,
    2008: 0.034,
    2009: 0.009,
    2010: 0.016,
    2011: 0.027,
    2012: 0.025,
    2013: 0.013,
    2014: 0.007,
    2015: 0.001,
    2016: 0.002,
    2017: 0.015,
    2018: 0.018,
    2019: 0.014,
    2020: 0.003,
    2021: 0.026,
    2022: 0.082,
    2023: 0.054,
    2024: 0.028,
    2025: 0.024,
    2026: 0.023,
}

FOOTBALL_MARKET_INFLATION_RATES: dict[int, float] = {
    1990: 0.060,
    1991: 0.055,
    1992: 0.050,
    1993: 0.042,
    1994: 0.040,
    1995: 0.045,
    1996: 0.043,
    1997: 0.048,
    1998: 0.052,
    1999: 0.055,
    2000: 0.062,
    2001: 0.058,
    2002: 0.045,
    2003: 0.070,
    2004: 0.075,
    2005: 0.082,
    2006: 0.085,
    2007: 0.090,
    2008: 0.052,
    2009: -0.015,
    2010: 0.030,
    2011: 0.045,
    2012: 0.038,
    2013: 0.050,
    2014: 0.072,
    2015: 0.080,
    2016: 0.090,
    2017: 0.120,
    2018: 0.032,
    2019: 0.025,
    2020: -0.060,
    2021: 0.020,
    2022: 0.060,
    2023: 0.055,
    2024: 0.050,
    2025: 0.045,
    2026: 0.040,
}


def get_inflation_rates(mode: InflationMode) -> dict[int, float]:
    if mode == "Economic inflation":
        return ECONOMIC_INFLATION_RATES
    return FOOTBALL_MARKET_INFLATION_RATES


def calculate_inflation_adjusted_value(
    transfer_year: int,
    transfer_amount_million_eur: float,
    mode: InflationMode,
    current_year: int | None = None,
) -> tuple[float, int, list[dict[str, float]]]:
    """Calculate year-by-year compounded inflation adjustment.

    Returns:
        adjusted_value: Final value in million EUR.
        years_passed: Number of elapsed years.
        growth_points: Yearly values for charting.
    """
    year_now = current_year or datetime.now().year
    rates = get_inflation_rates(mode)

    if transfer_year > year_now:
        raise ValueError("Transfer year cannot be in the future.")

    missing_years = [year for year in range(transfer_year, year_now) if year not in rates]
    if missing_years:
        raise ValueError(
            "Missing yearly inflation data for: "
            + ", ".join(str(year) for year in missing_years)
        )

    value = transfer_amount_million_eur
    growth_points: list[dict[str, float]] = [{"Year": float(transfer_year), "Value": value}]

    for year in range(transfer_year, year_now):
        value *= 1 + rates[year]
        growth_points.append({"Year": float(year + 1), "Value": value})

    return value, year_now - transfer_year, growth_points
