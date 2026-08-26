import csv
import sqlite3
import pandas as pd
import streamlit as st

st.title("Test database")

@st.cache_data
def load_and_initialize():
    conn = sqlite3.connect("example.db")
    df=pd.read_csv(r"CompaniesDSSS.csv")
    df.to_sql("my_table", conn, if_exists="replace", index=False)
    conn.close()
    return "Database Initiaized"

status_msg = load_and_initialize()

conn = sqlite3.connect("example.db", check_same_thread=False)

query = "SELECT distinct Space FROM my_table"
try:
    cursor = conn.cursor()
    cursor.execute(query)
    categories = [row[0] for row in cursor.fetchall()]
    #categories = sorted(df["Space"].dropna().unique())
    selected_categories = st.multiselect("Filter by Space:", options=categories)

    if selected_categories:
        placeholders = ", ".join(["?"]*len(selected_categories))
        query = f"SELECT * FROM my_table WHERE Space IN ({placeholders})"
        params = tuple(selected_categories)
    else:
        query = "SELECT * FROM my_table"
        params = ()

#cursor = conn.cursor()
#cursor.execute("Select * from my_table limit 5")
#print(cursor.fetchall())

#df_result= pd.read_sql_query(query, conn)
#print(query)
#print(params)
    df_filtered = pd.read_sql_query(query, conn, params=params)
    st.dataframe(df_filtered)
finally:
    conn.close()

