import streamlit as st

st.set_page_config(page_title="Retirement & Legacy Planner", layout="centered")

st.title("Retirement and Legacy Planning Calculator")

# Input Section
curr_age = st.number_input("Current Age", min_value=18, max_value=100, value=25)
ret_age = st.number_input("Age of Financial Independence (Retirement Age)", min_value=curr_age+1, max_value=100, value=60)
life_exp = st.number_input("Life Expectancy", min_value=ret_age, max_value=120, value=100)

inflation = st.number_input("Expected Inflation Rate (% p.a.)", min_value=0.0, max_value=20.0, value=6.0, format="%.2f")
pre_ret_return = st.number_input("Return Before Financial Independence (% p.a.)", min_value=0.0, max_value=30.0, value=15.0, format="%.2f")
post_ret_return = st.number_input("Return After Financial Independence (% p.a.)", min_value=0.0, max_value=20.0, value=10.0, format="%.2f")
existing_return = st.number_input("Return on Existing Investments (% p.a.)", min_value=0.0, max_value=30.0, value=12.0, format="%.2f")

monthly_exp = st.number_input("Current Monthly Expenses (Rs.)", min_value=0, value=30000, step=1000)
current_inv = st.number_input("Current Investments (Rs.)", min_value=0, value=100000, step=1000)

legacy_amt = st.number_input("Inheritance to be left behind (Rs.)", min_value=0, value=10000000, step=1000)

if st.button("💡 Calculate"):

    years_to_ret = ret_age - curr_age
    years_after_ret = life_exp - ret_age

    # Project annual expenses at retirement with inflation
    annual_expense_retirement = monthl
