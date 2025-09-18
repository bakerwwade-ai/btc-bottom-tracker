import streamlit as st
import requests
from datetime import datetime

st.title("Bitcoin Bottom-Odds Tracker")

# Run button to fetch data and compute placeholder odds
if st.button("Run Now"):
    st.write("Running daily check...")
    # Fetch current BTC price from CoinGecko
    price = None
    try:
        resp = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin", "vs_currencies": "usd"},
            timeout=10,
        )
        resp.raise_for_status()
        price = resp.json().get("bitcoin", {}).get("usd")
    except Exception:
        price = None

    if price is not None:
        st.success(f"Current BTC price: ${price:,.2f}")
    else:
        st.warning("Could not fetch BTC price.")

    # Placeholder for probability, rating, and confidence
    st.write("Bottom odds: 2% (placeholder)")
    st.write("Rating: WAIT")
    st.write("Confidence: 70%")
else:
    st.info("Press the button to run today's check.")
