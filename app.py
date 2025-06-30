import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")
st.title("👥 Employee Attrition Dashboard")
st.markdown("This dashboard provides key insights to help HR understand attrition patterns and trends across different factors.")

@st.cache_data
def load_data():
    df = pd.read_csv("EA.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
department = st.sidebar.multiselect("Department", options=df["Department"].unique(), default=df["Department"].unique())
gender = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
overtime = st.sidebar.multiselect("OverTime", options=df["OverTime"].unique(), default=df["OverTime"].unique())

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["OverTime"].isin(overtime))
]

# Tabs for grouping visuals
tab1, tab2, tab3, tab4 = st.tabs(["📌 Overview", "📈 Performance & Satisfaction", "💰 Compensation", "📆 Tenure"])

with tab1:
    st.subheader("Employee Distribution & Demographics")

    st.markdown("**1. Count of Employees by Department**")
    fig1 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("**2. Gender Distribution**")
    fig2 = px.pie(filtered_df, names="Gender", hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("**3. Attrition by Marital Status**")
    fig3 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("**4. Education Field Breakdown**")
    fig4 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("**5. Age Distribution**")
    fig5 = px.histogram(filtered_df, x="Age", nbins=20, color="Attrition")
    st.plotly_chart(fig5, use_container_width=True)

with tab2:
    st.subheader("Job Satisfaction and Performance")

    st.markdown("**6. Job Satisfaction vs Attrition**")
    fig6 = px.box(filtered_df, x="Attrition", y="JobSatisfaction", points="all")
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("**7. Environment Satisfaction vs Attrition**")
    fig7 = px.box(filtered_df, x="Attrition", y="EnvironmentSatisfaction", points="all")
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("**8. Training Times Last Year**")
    fig8 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition", barmode="group")
    st.plotly_chart(fig8, use_container_width=True)

    st.markdown("**9. OverTime vs Attrition**")
    fig9 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
    st.plotly_chart(fig9, use_container_width=True)

    st.markdown("**10. Job Involvement**")
    fig10 = px.box(filtered_df, x="Attrition", y="JobInvolvement", points="all")
    st.plotly_chart(fig10, use_container_width=True)

with tab3:
    st.subheader("Compensation and Rewards")

    st.markdown("**11. Monthly Income Distribution**")
    fig11 = px.histogram(filtered_df, x="MonthlyIncome", nbins=30, color="Attrition")
    st.plotly_chart(fig11, use_container_width=True)

    st.markdown("**12. Percent Salary Hike**")
    fig12 = px.box(filtered_df, x="Attrition", y="PercentSalaryHike", points="all")
    st.plotly_chart(fig12, use_container_width=True)

    st.markdown("**13. Stock Option Level**")
    fig13 = px.histogram(filtered_df, x="StockOptionLevel", color="Attrition", barmode="group")
    st.plotly_chart(fig13, use_container_width=True)

    st.markdown("**14. Daily Rate Distribution**")
    fig14 = px.histogram(filtered_df, x="DailyRate", nbins=20, color="Attrition")
    st.plotly_chart(fig14, use_container_width=True)

    st.markdown("**15. Hourly Rate Distribution**")
    fig15 = px.histogram(filtered_df, x="HourlyRate", nbins=20, color="Attrition")
    st.plotly_chart(fig15, use_container_width=True)

with tab4:
    st.subheader("Tenure and Career Progression")

    st.markdown("**16. Years at Company vs Attrition**")
    fig16 = px.box(filtered_df, x="Attrition", y="YearsAtCompany", points="all")
    st.plotly_chart(fig16, use_container_width=True)

    st.markdown("**17. Years in Current Role**")
    fig17 = px.box(filtered_df, x="Attrition", y="YearsInCurrentRole", points="all")
    st.plotly_chart(fig17, use_container_width=True)

    st.markdown("**18. Years Since Last Promotion**")
    fig18 = px.box(filtered_df, x="Attrition", y="YearsSinceLastPromotion", points="all")
    st.plotly_chart(fig18, use_container_width=True)

    st.markdown("**19. Years With Current Manager**")
    fig19 = px.box(filtered_df, x="Attrition", y="YearsWithCurrManager", points="all")
    st.plotly_chart(fig19, use_container_width=True)

    st.markdown("**20. Total Working Years**")
    fig20 = px.box(filtered_df, x="Attrition", y="TotalWorkingYears", points="all")
    st.plotly_chart(fig20, use_container_width=True)
