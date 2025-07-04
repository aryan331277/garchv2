📈 Hybrid Volatility Forecasting with GARCH + EVT + VaR
A modular, real-time volatility forecasting engine designed for risk-sensitive trading, VaR estimation, and tail event detection.

Developed using GARCH modeling, Extreme Value Theory (EVT), and Kupiec backtesting, with a full Streamlit dashboard for deployment and interpretation.

🧠 Motivation
Financial volatility is rarely Gaussian — especially in crises. Traditional GARCH models fail to capture fat tails, regime shifts, and tail risk. This project builds a practical hybrid engine to forecast volatility and account for rare, high-impact events.

🚀 What It Does
Component	Function
GARCH Engine	Models volatility clustering with GARCH(1,1) and t-distribution
EVT Tail Modeling	Fits Generalized Pareto Distribution (GPD) on GARCH residuals
VaR Backtester	Computes 1-day VaR at 95% and 99%, tests violations
Kupiec Test	Statistically verifies violation rate vs confidence level
Streamlit Dashboard	Interactive plot of vol forecasts, tail risk, and VaR overlays

📊 Results Summary
Metric	Value
Tail probability (>3σ)	11.26%
95% VaR violation rate	2.07%
99% VaR violation rate	0.24%
Kupiec LR (95%)	28.99
Kupiec LR (99%)	10.63

The model is conservative — it overestimates tail risk slightly, which is often preferred in institutional risk management.

