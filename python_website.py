import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px  # Requires Plotly installation
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time


st.set_page_config(
    page_title="DataFlow Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }

    .sub-header {
        font-size: 1.5rem;
        color: #4a4a4a;
        text-align: center;
        margin-bottom: 3rem;
    }

    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    [data-testid="stSidebar"] .stSelectbox,
    [data-testid="stSidebar"] .stRadio,
    [data-testid="stSidebar"] .stCheckbox {
        color: white;
    }

    [data-testid="stSidebar"] label {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>DataFlow</h1>", unsafe_allow_html=True)
    st.markdown("---")

    page = st.selectbox(
        "Navigate",
        ["🏠 Home", "📈 Analytics", "🔍 Data Explorer", "🤖 AI Insights", "📊 Reports"]
    )

    st.markdown("---")
    st.markdown("### 🎛️ Settings")

    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    notifications = st.checkbox("Enable Notifications", value=True)

    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("📧 hello@dataflow.com")
    st.markdown("📱 +1 (555) 123-4567")

if page == "🏠 Home":
    st.markdown('<h1 class="main-header">DataFlow Analytics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform your data into actionable insights</p>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            '<div class="metric-container"><h3>1,234</h3><p>Active Users</p></div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="metric-container"><h3>98.5%</h3><p>Uptime</p></div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="metric-container"><h3>45TB</h3><p>Data Processed</p></div>',
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            '<div class="metric-container"><h3>24/7</h3><p>Support</p></div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown("## 🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Real-time Analytics</h3>
            <p>Monitor your data streams in real-time with advanced visualization tools and instant alerts.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h3>🤖 AI-Powered Insights</h3>
            <p>Leverage machine learning algorithms to discover hidden patterns and predict future trends.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Custom Dashboards</h3>
            <p>Create personalized dashboards with drag-and-drop widgets tailored to your specific needs.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="feature-card">
            <h3>🔒 Enterprise Security</h3>
            <p>Bank-level security with end-to-end encryption and compliance with industry standards.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## 🎯 Try Our Demo")

    demo_type = st.selectbox("Select Demo Type", ["Sales Performance", "User Engagement", "Revenue Trends"])

    if demo_type == "Sales Performance":
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        sales_data = pd.DataFrame({
            'Date': dates,
            'Sales': np.random.normal(10000, 2000, len(dates)).cumsum(),
            'Region': np.random.choice(['North', 'South', 'East', 'West'], len(dates))
        })

        fig = px.line(sales_data, x='Date', y='Sales', color='Region',
                     title="Sales Performance by Region")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

elif page == "📈 Analytics":
    st.markdown("# 📈 Analytics Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())

    if start_date > end_date:
        st.error("Error: End date must be after start date.")
        st.stop()

    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Revenue': np.random.normal(50000, 10000, len(dates)),
        'Users': np.random.normal(1000, 200, len(dates)),
        'Conversion': np.clip(np.random.normal(0.05, 0.01, len(dates)), 0.01, 0.10)
    })

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Revenue", f"${data['Revenue'].sum():,.0f}",
                 delta=f"{((data['Revenue'].tail(7).mean() - data['Revenue'].head(7).mean()) / data['Revenue'].head(7).mean() * 100):+.1f}%")

    with col2:
        st.metric("Total Users", f"{data['Users'].sum():,.0f}",
                 delta=f"{((data['Users'].tail(7).mean() - data['Users'].head(7).mean()) / data['Users'].head(7).mean() * 100):+.1f}%")

    with col3:
        st.metric("Avg Conversion", f"{data['Conversion'].mean():.2%}",
                 delta=f"{((data['Conversion'].tail(7).mean() - data['Conversion'].head(7).mean()) / data['Conversion'].head(7).mean() * 100):+.1f}%")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.line(data, x='Date', y='Revenue', title="Revenue Trend")
        fig1.update_layout(height=300)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(data.tail(7), x='Date', y='Users', title="Daily Active Users (Last 7 Days)")
        fig2.update_layout(height=300)
        st.plotly_chart(fig2, use_container_width=True)

elif page == "🔍 Data Explorer":
    st.markdown("# 🔍 Data Explorer")

    uploaded_file = st.file_uploader("Upload your data (CSV, Excel)", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success(f"Loaded {len(df)} rows and {len(df.columns)} columns")

            st.markdown("## 📋 Data Preview")
            st.dataframe(df.head(10))

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## 📊 Data Summary")
                st.dataframe(df.describe(include='all').fillna(''))

            with col2:
                st.markdown("## 🔍 Column Info")
                info_df = pd.DataFrame({
                    'Column': df.columns,
                    'Type': df.dtypes,
                    'Non-Null Count': df.count(),
                    'Null Count': df.isnull().sum()
                })
                st.dataframe(info_df)

            st.markdown("## 📈 Quick Visualization")

            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            all_columns = df.columns.tolist()

            if len(numeric_columns) >= 1:
                col1, col2 = st.columns(2)

                with col1:
                    x_axis = st.selectbox("X-axis", all_columns)

                with col2:
                    y_axis = st.selectbox("Y-axis", numeric_columns if x_axis != y_axis else [col for col in numeric_columns if col != x_axis])

                color_col = st.selectbox("Color (optional)", ['None'] + all_columns)
                color_col = None if color_col == 'None' else color_col

                chart_type = st.selectbox("Chart Type", ["Scatter", "Line", "Bar", "Histogram"])

                try:
                    if chart_type == "Scatter":
                        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_col)
                    elif chart_type == "Line":
                        fig = px.line(df, x=x_axis, y=y_axis, color=color_col)
                    elif chart_type == "Bar":
                        fig = px.bar(df, x=x_axis, y=y_axis, color=color_col)
                    else:
                        fig = px.histogram(df, x=x_axis, nbins=20, color=color_col)

                    st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"Error creating chart: {str(e)}")
            else:
                st.warning("Need at least one numeric column for visualization")

        except Exception as e:
            st.error(f"Error loading file: {str(e)}")

    else:
        st.markdown("## 🎯 Sample Data Demo")

        sample_data = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'D', 'E'],
            'Sales': [100, 150, 200, 120, 180],
            'Profit': [20, 30, 45, 25, 40],
            'Category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing']
        })

        st.dataframe(sample_data)

        fig = px.bar(sample_data, x='Product', y='Sales', color='Category',
                    title="Sample Sales Data")
        st.plotly_chart(fig, use_container_width=True)

elif page == "🤖 AI Insights":
    st.markdown("# 🤖 AI Insights")

    st.markdown("## 🎯 Predictive Analytics")

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing data with AI..."):
            time.sleep(2)

            st.success("Analysis Complete!")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📈 Predicted Trends")

                future_dates = pd.date_range(start=datetime.now(), periods=30, freq='D')
                forecast_data = pd.DataFrame({
                    'Date': future_dates,
                    'Predicted_Sales': np.random.normal(75000, 5000, 30).cumsum(),
                    'Confidence_Upper': np.random.normal(85000, 3000, 30).cumsum(),
                    'Confidence_Lower': np.random.normal(65000, 3000, 30).cumsum()
                })

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=forecast_data['Date'], y=forecast_data['Predicted_Sales'],
                                       mode='lines', name='Predicted Sales'))
                fig.add_trace(go.Scatter(x=forecast_data['Date'], y=forecast_data['Confidence_Upper'],
                                       mode='lines', name='Upper Confidence', line=dict(dash='dash')))
                fig.add_trace(go.Scatter(x=forecast_data['Date'], y=forecast_data['Confidence_Lower'],
                                       mode='lines', name='Lower Confidence', line=dict(dash='dash')))
                fig.update_layout(title="30-Day Sales Forecast")
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("### 🔍 Key Insights")

                insights = [
                    "📊 Sales are expected to increase by 12% next month",
                    "🎯 Customer retention rate is above industry average",
                    "⚠️ Product category 'Electronics' showing declining trend",
                    "🚀 Mobile traffic increased by 45% this quarter",
                    "💡 Recommendation: Focus marketing on high-value segments"
                ]

                for insight in insights:
                    st.markdown(f"- {insight}")

                st.markdown("### 🎯 Recommendations")

                recommendations = [
                    "Increase inventory for high-demand products",
                    "Optimize pricing strategy for electronics category",
                    "Expand mobile app features",
                    "Launch targeted email campaigns",
                    "Consider partnership opportunities"
                ]

                for i, rec in enumerate(recommendations, 1):
                    st.markdown(f"{i}. {rec}")

elif page == "📊 Reports":
    st.markdown("# 📊 Reports")

    report_type = st.selectbox("Select Report Type",
                              ["Executive Summary", "Sales Report", "User Analytics", "Performance Metrics"])

    if report_type == "Executive Summary":
        st.markdown("## 📋 Executive Summary")
        st.markdown("*Report generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "*")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Monthly Revenue", "$2.4M", delta="12.5%")

        with col2:
            st.metric("Active Customers", "15,234", delta="8.2%")

        with col3:
            st.metric("Customer Satisfaction", "4.7/5", delta="0.3")

        st.markdown("### 🎯 Key Highlights")
        st.markdown("""
        - Revenue grew by 12.5% compared to last month
        - Customer acquisition cost decreased by 15%
        - New product launch exceeded expectations by 130%
        - Mobile app downloads increased by 67%
        - Customer support response time improved by 25%
        """)

        st.markdown("### 📝 Action Items")
        st.markdown("""
        1. **Expand successful product lines** - Allocate additional resources to top-performing products
        2. **Optimize mobile experience** - Invest in mobile app improvements based on user feedback
        3. **Scale customer support** - Hire additional support staff to maintain service quality
        4. **International expansion** - Explore opportunities in European markets
        5. **Partnership development** - Establish strategic partnerships with complementary brands
        """)

    st.markdown("---")

    if st.button("📥 Export Report"):
        st.success("Report exported successfully! Check your downloads folder.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>© 2024 DataFlow Analytics. Built with ❤️ using Streamlit</p>
    <p>🚀 Powered by Python | 📊 Data-Driven Decisions | 🔒 Secure & Reliable</p>
</div>
""", unsafe_allow_html=True)