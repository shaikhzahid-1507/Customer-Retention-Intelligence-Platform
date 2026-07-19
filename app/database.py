import sqlite3
from datetime import datetime
import pandas as pd

DATABASE_NAME = "customer_predictions.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_id TEXT,

        prediction TEXT,

        probability REAL,

        confidence REAL,

        monthly_charge REAL,

        tenure INTEGER,

        revenue_at_risk REAL,

        contract TEXT,

        internet_service TEXT,

        created_at TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_prediction(
    customer_id,
    prediction,
    probability,
    confidence,
    monthly_charge,
    tenure,
    revenue_at_risk,
    contract,
    internet_service
):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (
            customer_id,
            prediction,
            probability,
            confidence,
            monthly_charge,
            tenure,
            revenue_at_risk,
            contract,
            internet_service,
            created_at
        )

        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (
            customer_id,
            prediction,
            probability,
            confidence,
            monthly_charge,
            tenure,
            revenue_at_risk,
            contract,
            internet_service,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()

    conn.close()

def get_all_predictions():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_predictions_dataframe():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT
        customer_id AS 'Customer ID',
        prediction AS 'Prediction',
        ROUND(probability * 100, 2) || '%' AS 'Probability',
        ROUND(confidence * 100, 2) || '%' AS 'Confidence',
        monthly_charge AS 'Monthly Charge',
        revenue_at_risk AS 'Revenue At Risk',
        contract AS 'Contract',
        internet_service AS 'Internet Service',
        created_at AS 'Prediction Time'
    FROM predictions
    ORDER BY id DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df
def get_dashboard_data():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT
        customer_id,
        prediction,
        probability,
        confidence,
        monthly_charge,
        revenue_at_risk,
        contract,
        internet_service,
        created_at
    FROM predictions
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df
def get_dashboard_data():

    conn = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT
        customer_id,
        prediction,
        probability,
        confidence,
        monthly_charge,
        revenue_at_risk,
        contract,
        internet_service,
        created_at
    FROM predictions
    ORDER BY id DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df