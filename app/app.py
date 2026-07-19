import streamlit as st
from pdf_generator import generate_pdf
import plotly.express as px
from database import (
    create_database,
    save_prediction,
    get_predictions_dataframe,
    get_dashboard_data
)
import dashboard
import inspect
from charts import create_gauge_chart
from pathlib import Path
from model_handler import (
    load_model,
    load_scaler,
    load_encoder,
    load_feature_columns,
    predict_customer
)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="...",
    page_icon="📊",
    layout="wide"
)  
def load_css():
    css_file = Path(__file__).parent / "style.css"

    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
create_database()
# -------------------------------
# Load ML Components
# -------------------------------
model = load_model()
scaler = load_scaler()
encoder = load_encoder()
feature_columns = load_feature_columns()

# -------------------------------
# Header
# -------------------------------
st.markdown("""
<div class="hero-section">

<h1>📊 Customer Retention Intelligence Platform</h1>

<p>
AI-powered customer churn prediction using Machine Learning,
Business Intelligence and Executive Analytics.
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------------
# Customer Information Section
# -------------------------------
st.header("📝 Customer Information")

with st.form("customer_form"):

    # ====================================
    # Basic Customer Information
    # ====================================

    customer_id = st.text_input(
        "Customer ID",
        placeholder="Enter Customer ID"
    )

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

    with col2:
        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

    # ====================================
    # Service Information
    # ====================================

    st.subheader("📡 Service Information")

    col1, col2 = st.columns(2)

    with col1:

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No phone service", "No", "Yes"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

    with col2:

        online_security = st.selectbox(
            "Online Security",
            ["No internet service", "No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No internet service", "No", "Yes"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["No internet service", "No", "Yes"]
        )

    # ====================================
    # Subscription Information
    # ====================================

    st.subheader("📄 Subscription Information")

    col1, col2 = st.columns(2)

    with col1:

        tech_support = st.selectbox(
            "Tech Support",
            ["No internet service", "No", "Yes"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No internet service", "No", "Yes"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No internet service", "No", "Yes"]
        )

    with col2:

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    # ====================================
    # Billing Information
    # ====================================

    st.subheader("💰 Billing Information")

    col1, col2 = st.columns(2)

    with col1:

        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0,
            max_value=72,
            value=12
        )

    with col2:

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=50.0
        )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )

    submitted = st.form_submit_button("🔮 Predict Churn")


# ===================================================
# Prediction
# ===================================================

if submitted:

    customer_data = {

        # Customer Information
        "customerID": customer_id,
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,

        # Service Information
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,

        # Subscription Information
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,

        # Billing Information
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges

    }

    prediction, probability = predict_customer(
        model=model,
        scaler=scaler,
        feature_columns=feature_columns,
        customer_data=customer_data
    )

    # =====================================================
    # Prediction Results
    # =====================================================

    st.divider()

    st.header("📈 Prediction Results")
    dashboard.show_kpi_cards(
        prediction,
        probability,
        monthly_charges
    )

    st.divider()

    col1, col2 = st.columns(2)

    # ------------------------
    # Customer Status
    # ------------------------

    with col1:

        if prediction == 1:
            st.error("🔴 Customer is likely to Churn")
        else:
            st.success("🟢 Customer is likely to Stay")

    # ------------------------
    # Risk Level
    # ------------------------

    with col2:

        if probability >= 0.75:
            st.error("🔴 High Risk")

        elif probability >= 0.50:
            st.warning("🟠 Medium Risk")

        else:
            st.success("🟢 Low Risk")

    st.divider()

    # ------------------------
    # KPI Metrics
    # ------------------------

    metric1, metric2 = st.columns(2)

    metric1.metric(
        "📊 Churn Probability",
        f"{probability * 100:.2f}%"
    )

    confidence = (1 - probability) if prediction == 0 else probability
    revenue_at_risk = monthly_charges * probability
    save_prediction(

    customer_id=customer_id,

    prediction="Churn" if prediction == 1 else "Stay",

    probability=probability,

    confidence=confidence,

    monthly_charge=monthly_charges,

    tenure=tenure,

    revenue_at_risk=revenue_at_risk,

    contract=contract,

    internet_service=internet_service

)
    metric2.metric(
        "🎯 Confidence",
        f"{confidence * 100:.2f}%"
    )

    gauge = create_gauge_chart(probability)

    st.plotly_chart(
    gauge,
    use_container_width=True
)
    st.divider() 
    dashboard.show_revenue_analytics(
        monthly_charge=monthly_charges,
        tenure=tenure,
        probability=probability
    )


    # =====================================================
    # Customer Summary
    # =====================================================

    st.divider()
    st.subheader("📋 Customer Summary")

    summary = {
        "Gender": gender,
        "Senior Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Internet Service": internet_service,
        "Contract": contract,
        "Tenure (Months)": tenure,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }

    st.table(summary)

    st.divider()
    st.subheader("💡 Business Recommendations")

    if prediction == 1:
        st.warning("""
### Immediate Retention Strategy

- 📞 Contact the customer within 24 hours
- 🎁 Offer a loyalty discount
- 📅 Recommend switching to a yearly contract
- 🛠️ Provide free technical support
- 💰 Offer a personalized retention plan
""")
    else:
        st.success("""
### Customer Growth Strategy

- ⭐ Offer premium internet plans
- 📺 Recommend streaming bundles
- 💳 Suggest annual subscription
- 🎉 Reward customer loyalty
- 📈 Cross-sell additional services
""")

    with st.expander("🔍 View Technical Prediction Details"):
        st.write(f"Prediction : {prediction}")
        st.write(f"Probability : {probability:.4f}")
        st.write(f"Confidence : {confidence:.4f}")

    st.divider()

    st.markdown("""
    <div style="text-align:center;color:#94A3B8;padding:20px;">

    <b>Customer Retention Intelligence Platform</b><br>

    Built with ❤️ using

    Python • Streamlit • Scikit-Learn • SQLite • Plotly • ReportLab

    <br><br>

    Developed by <b>Zahid Shaikh</b>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.subheader("📄 Download Report")

    pdf_filename = f"{customer_id}_Prediction_Report.pdf"

    generate_pdf(
        filename=pdf_filename,
        customer_data=customer_data,
        prediction=prediction,
        probability=probability,
        confidence=confidence,
        revenue_at_risk=revenue_at_risk,
        monthly_charge=monthly_charges,
        total_charges=total_charges
    )

    with open(pdf_filename, "rb") as pdf_file:
        st.download_button(
            label="📄 Download Customer Report",
            data=pdf_file,
            file_name=pdf_filename,
            mime="application/pdf"
        )

    st.divider()
st.header("📜 Prediction History")
# ==========================================================
# Business Charts
# ==========================================================

st.divider()

st.subheader("📊 Business Insights")

dashboard_df = get_dashboard_data()

if not dashboard_df.empty:

    col1, col2 = st.columns(2)

    with col1:

        prediction_counts = (
            dashboard_df["prediction"]
            .value_counts()
            .reset_index()
        )

        prediction_counts.columns = [
            "Prediction",
            "Count"
        ]

        fig = px.pie(
            prediction_counts,
            names="Prediction",
            values="Count",
            title="Prediction Distribution",
            hole=0.45,
            color="Prediction",
            color_discrete_map={
                "Stay": "#22C55E",
                "Churn": "#EF4444"
            }
        )

        fig.update_layout(
            height=450,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        contract_counts = (
            dashboard_df["contract"]
            .value_counts()
            .reset_index()
        )

        contract_counts.columns = [
            "Contract",
            "Count"
        ]

        fig = px.bar(
            contract_counts,
            x="Contract",
            y="Count",
            title="Contract Distribution",
            text_auto=True
        )

        fig.update_layout(
            height=450,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.divider()

col3, col4 = st.columns(2)

with col3:

    internet_counts = (
        dashboard_df["internet_service"]
        .value_counts()
        .reset_index()
    )

    internet_counts.columns = [
        "Internet Service",
        "Count"
    ]

    fig = px.bar(
        internet_counts,
        x="Internet Service",
        y="Count",
        title="Internet Service Distribution",
        text_auto=True,
        color="Internet Service"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    revenue_df = dashboard_df.sort_values(
        by="revenue_at_risk",
        ascending=False
    )

    fig = px.bar(
        revenue_df,
        x="customer_id",
        y="revenue_at_risk",
        title="Revenue at Risk by Customer",
        text_auto=".2f",
        color="revenue_at_risk",
        color_continuous_scale="Reds"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        xaxis_title="Customer ID",
        yaxis_title="Revenue at Risk"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.divider()

trend_df = dashboard_df.copy()

trend_df["created_at"] = (
    trend_df["created_at"]
    .astype(str)
    .str[:10]
)

trend_df = (
    trend_df.groupby("created_at")
    .size()
    .reset_index(name="Predictions")
)

fig = px.line(
    trend_df,
    x="created_at",
    y="Predictions",
    markers=True,
    title="Daily Prediction Trend"
)

fig.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# ==========================================================
# Executive Analytics Dashboard
# ==========================================================

st.divider()

st.header("📊 Executive Analytics")

dashboard_df = get_dashboard_data()

if not dashboard_df.empty:

    total_predictions = len(dashboard_df)

    churn_customers = len(
        dashboard_df[
            dashboard_df["prediction"] == "Churn"
        ]
    )

    staying_customers = len(
        dashboard_df[
            dashboard_df["prediction"] == "Stay"
        ]
    )

    average_probability = (
        dashboard_df["probability"].mean() * 100
    )

    revenue_at_risk = (
        dashboard_df["revenue_at_risk"].sum()
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "📋 Total Predictions",
        total_predictions
    )

    c2.metric(
        "🔴 Churn",
        churn_customers
    )

    c3.metric(
        "🟢 Stay",
        staying_customers
    )

    c4.metric(
        "📈 Avg Probability",
        f"{average_probability:.2f}%"
    )

    c5.metric(
        "💰 Revenue Risk",
        f"₹{revenue_at_risk:,.0f}"
    )

else:

    st.info("No prediction history available.")

history_df = get_predictions_dataframe()

if history_df.empty:

    st.info("No predictions available yet.")

else:

    search = st.text_input(
        "🔍 Search Customer ID"
    )

    if search:

        history_df = history_df[
            history_df["Customer ID"]
            .astype(str)
            .str.contains(search, case=False)
        ]

    prediction_filter = st.selectbox(
        "Prediction Filter",
        ["All", "Stay", "Churn"]
    )

    if prediction_filter != "All":

        history_df = history_df[
            history_df["Prediction"] == prediction_filter
        ]

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )
