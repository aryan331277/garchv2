
🚀 What It Does
Component	Function
GARCH Engine	Models volatility clustering with GARCH(1,1) and t-distribution
EVT Tail Modeling	Fits Generalized Pareto Distribution (GPD) on GARCH residuals
VaR Backtester	Computes 1-day VaR at 95% and 99%, tests violations
Kupiec Test	Statistically verifies violation rate vs confidence level
Streamlit Dashboard	Interactive plot of vol forecasts, tail risk, and VaR overlays


The model is conservative — it overestimates tail risk slightly, which is often preferred in institutional risk management.

