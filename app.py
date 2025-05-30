import streamlit as st

st.title("🧮 Retirement & Legacy Planner")

# --- Input Section ---
st.header("Enter Your Details")

curr_age = st.number_input("Current Age", min_value=0, value=40)
ret_age = st.number_input("Retirement Age", min_value=curr_age + 1, value=60)
life_exp = st.number_input("Life Expectancy", min_value=ret_age + 1, value=100)

monthly_exp = st.number_input("Current Monthly Expenses (₹)", value=50000)
inflation = st.number_input("Expected Inflation (% per annum)", value=6.0, format="%.2f")
pre_ret_return = st.number_input("Returns Before Retirement (% p.a.)", value=20.0, format="%.2f")
post_ret_return = st.number_input("Returns After Retirement (% p.a.)", value=6.0, format="%.2f")
curr_inv = st.number_input("Current Investments (₹)", value=100000)
legacy_amt = st.number_input("Desired Inheritance (₹)", value=1000000)

# --- Compute Button ---
if st.button("💡 Compute"):

    # --- Calculations ---
    years_to_ret = ret_age - curr_age
    years_after_ret = life_exp - ret_age
    annual_expense_retirement = monthly_exp * 12 * ((1 + inflation / 100) ** years_to_ret)

    # Corpus required using present value of growing annuity formula
    net_ret_rate = (1 + post_ret_return / 100) / (1 + inflation / 100) - 1
    if net_ret_rate > 0:
        corpus_required = annual_expense_retirement * ((1 - (1 + net_ret_rate) ** -years_after_ret) / net_ret_rate)
    else:
        corpus_required = annual_expense_retirement * years_after_ret

    # Add legacy
    corpus_total = corpus_required + legacy_amt

    # SIP Calculation
    monthly_rate = (1 + pre_ret_return / 100) ** (1 / 12) - 1
    months = years_to_ret * 12
    future_value = corpus_total

    if monthly_rate > 0:
        sip = future_value * monthly_rate / (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate))
    else:
        sip = future_value / months

    # Lumpsum Formula
    lumpsum = future_value / ((1 + pre_ret_return / 100) ** years_to_ret)

    # Legacy portion
    legacy_lumpsum = legacy_amt / ((1 + pre_ret_return / 100) ** years_to_ret)
    legacy_sip = legacy_amt * monthly_rate / (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate))

    # --- Display the Summary Message ---
       st.markdown("---")
    st.subheader("📋 Retirement Plan Summary")
    
    st.markdown(
        f"Your current expenses of Rs. **{monthly_exp * 12:,.0f}** will be Rs. **{annual_expense_retirement:,.0f}** "
        f"at an inflation (%) of **{inflation:.2f}** after **{years_to_ret}** years.\n\n"
        f"To meet these expenses and maintain your current standard of living, you will need to accumulate a corpus of "
        f"Rs. **{corpus_required:,.0f}**\n\n"
        f"For this, you need to invest:\n"
        f"- A **lumpsum** amount of Rs. **{lumpsum:,.0f}**\n"
        f"- Or start an **SIP** of Rs. **{sip:,.0f}** per month for the next **{years_to_ret}** years at **{pre_ret_return}%** CAGR\n\n"
        f"What's more, you can leave an inheritance of Rs. **{legacy_amt:,.0f}** by investing:\n"
        f"- An additional **lumpsum** of Rs. **{legacy_lumpsum:,.0f}**\n"
        f"- Or an **SIP** of Rs. **{legacy_sip:,.0f}** per month"
    )
