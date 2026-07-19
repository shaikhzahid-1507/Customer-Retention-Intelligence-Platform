import streamlit as st

def calculate_retention_score(probability):

    return round((1 - probability) * 100)


def calculate_revenue_at_risk(monthly_charge, probability):

    annual_revenue = monthly_charge * 12
    revenue_at_risk = annual_revenue * probability

    return annual_revenue, revenue_at_risk


def show_kpi_cards(prediction, probability, monthly_charge): 
    retention_score = calculate_retention_score(probability)
    _, revenue_at_risk = calculate_revenue_at_risk(monthly_charge, probability)

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if prediction == 0:
            st.metric(
                "👤 Customer Status",
                "Staying"
            )
        else:
            st.metric(
                "👤 Customer Status",
                "Churning"
            )

    with col2:

        if probability < 0.40:
            risk = "Low"

        elif probability < 0.70:
            risk = "Medium"

        else:
            risk = "High"

        st.metric(
            "⚠ Risk Level",
            risk
        )

    with col3:

        st.metric(
            "💰 Revenue At Risk",
            f"₹{revenue_at_risk:,.0f}"
        )

    with col4:

        st.metric(
            "⭐ Retention Score",
            f"{retention_score}/100"
        )

        
def show_revenue_analytics(
    monthly_charge,
    tenure,
    probability
):

    annual_revenue = monthly_charge * 12
    revenue_at_risk = annual_revenue * probability
    customer_ltv = monthly_charge * tenure

    st.subheader("💰 Revenue Analytics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Monthly Revenue",
            f"₹{monthly_charge:,.2f}"
        )

    with col2:
        st.metric(
            "Annual Revenue",
            f"₹{annual_revenue:,.2f}"
        )

    with col3:
        st.metric(
            "Revenue at Risk",
            f"₹{revenue_at_risk:,.2f}"
        )

    with col4:
        st.metric(
            "Customer LTV",
            f"₹{customer_ltv:,.2f}"
        )
    
    
