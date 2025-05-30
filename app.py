import streamlit as st

# Title
st.title("🧮 Retirement & Legacy Planner")

# --- User Inputs ---
st.header("Enter Your Details")

curr_age = st.number_input("Current Age", min_value=0, value=40)
ret_age = st.number_input("Retirement Age", min_value=curr_age+1, value=60)
life_exp = st.number_input("Life Expectancy", min_value=ret_age+1, value=100)

monthly_exp = st.number_input("Current Monthly Expenses (₹)", value=50000)
inflation = st.slider("Expected Inflation (% per annum)", 0.0, 15.0, 4.0)
pre_ret_return = st.slider("Returns Before Retirement (% p.a.)", 0.0, 20.0, 10.0)
post_ret_return = st.slider("Returns After Retirement (% p.a.)", 0.0, 20.0, 6.0)
curr_inv = st.number_input("Current Investments (₹)", value=100000)
legacy_amt = st.number_input("Desired Inheritance (₹)", value=1000000)

# --- Calculations ---
years_to_ret = ret_age - curr_age
years_after_ret = life_exp - ret_age
annual_expense_retirement = monthly_exp * 12 * ((1 + inflation / 100) ** years_to_ret)

# Corpus required using present value of growing annuity formula
net_ret_rate = (1 + post_ret_return / 100) / (1 + inflation / 100) - 1
if net_ret_rate > 0:
    corpus_required = annual_expense_retirement * ((1 - (1 + net_ret_rate) ** -years_after_ret) / net_ret_rate)
else:
    corpus_required = annual_expense_retirement * years_after_ret  # fallback

# Add legacy
corpus_total = corpus_required + legacy_amt

# SIP Calculation
monthly_rate = (1 + pre_ret_return / 100) ** (1/12) - 1
months = years_to_ret * 12
future_value = corpus_total

# SIP Formula: FV = SIP * [((1 + r)^n - 1) / r] * (1 + r)
sip = future_value * monthly_rate / (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate))

# Lumpsum Formula: FV = PV * (1 + r)^n => PV = FV / (1 + r)^n
lumpsum = future_value / ((1 + pre_ret_return / 100) ** years_to_ret)

# --- Output Section ---
st.header("📊 Results")

st.metric("Annual Expense at Retirement (₹)", f"{annual_expense_retirement:,.0f}")
st.metric("Corpus Required at Retirement (₹)", f"{corpus_required:,.0f}")
st.metric("Total Corpus (with Legacy) (₹)", f"{corpus_total:,.0f}")
st.metric("Monthly SIP Required (₹)", f"{sip:,.0f}")
st.metric("Lumpsum Investment Today (₹)", f"{lumpsum:,.0f}")
