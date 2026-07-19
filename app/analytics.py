import streamlit as st
import plotly.express as px


def show_dashboard(df):

    st.header("📊 Executive Analytics")

    total_predictions = len(df)

    high_risk = len(df[df["probability"] >= 0.75])

    avg_probability = df["probability"].mean() * 100

    revenue_risk = df["revenue_at_risk"].sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Predictions", total_predictions)

    c2.metric("High Risk Customers", high_risk)

    c3.metric(
        "Average Churn Probability",
        f"{avg_probability:.2f}%"
    )

    c4.metric(
        "Revenue at Risk",
        f"₹{revenue_risk:,.2f}"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            df,
            names="prediction",
            title="Prediction Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.bar(
            df,
            x="contract",
            title="Contract Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        fig = px.bar(
            df,
            x="internet_service",
            title="Internet Service Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col4:

        fig = px.bar(
            df,
            x="customer_id",
            y="revenue_at_risk",
            title="Revenue at Risk"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )