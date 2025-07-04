import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Volatility Forecast Dashboard")

returns = pd.read_csv("returns.csv", parse_dates=['date'], index_col='date')
vol = pd.read_csv("forecast_vol.csv", parse_dates=['date'], index_col='date')
VaR = pd.read_csv("VaR_table.csv", parse_dates=['date'], index_col='date')

returns.index = pd.to_datetime(returns.index)
vol.index = pd.to_datetime(vol.index)
VaR.index = pd.to_datetime(VaR.index)

# Plot Forecasted Volatility vs Realized Return
st.subheader("Volatility Forecast vs Realized Return")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(vol.index, vol['forecast'], label="GARCH Forecast", color='blue')
ax.plot(returns.index, returns['abs_return'], label="Abs Return", color='orange', alpha=0.5)
ax.set_title("Volatility Forecast")
ax.legend()
st.pyplot(fig)

# VaR Plot
st.subheader("Value at Risk (VaR)")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(returns.index, returns['return'], label='Return', alpha=0.6)
ax2.plot(VaR.index, VaR['VaR_95'], label='VaR 95%', linestyle='--', color='red')
ax2.plot(VaR.index, VaR['VaR_99'], label='VaR 99%', linestyle='--', color='purple')
ax2.fill_between(VaR.index, VaR['VaR_99'], VaR['VaR_95'], color='red', alpha=0.1)
ax2.legend()
st.pyplot(fig2)

# Tail Risk Meter
st.subheader("Tail Risk Alert")
tail_prob = 0.1126
st.metric(label="Probability of >3σ Shock", value=f"{tail_prob*100:.2f}%")
