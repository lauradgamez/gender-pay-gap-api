import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import joblib

# -------------------------------------------------------
# Page configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Gender Pay Gap Dashboard",
    page_icon="⚖️",
    layout="wide"
)

# -------------------------------------------------------
# Force light theme for all plotly charts
# -------------------------------------------------------
PLOTLY_TEMPLATE = "plotly_white"
PRIMARY_COLOR = "#c1121f"
DIVERGING_PALETTE = "RdBu_r"

# -------------------------------------------------------
# Load data
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('gender_pay_gap_dataset.csv')
    return df

@st.cache_resource
def load_encoders():
    encoders = joblib.load('saved_models/label_encoders.joblib')
    return encoders

df = load_data()
label_encoders = load_encoders()

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.title("⚖️ Gender Pay Gap Analysis")
st.markdown(
    "Exploratory and predictive analysis of the gender pay gap "
    "across 103 countries and 5 decades, based on ILOSTAT data."
)

st.divider()

# -------------------------------------------------------
# Global metrics bar
# -------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Countries analyzed",
        value=df['ref_area_label'].nunique()
    )

with col2:
    st.metric(
        label="Years covered",
        value=f"{df['time'].min()} - {df['time'].max()}"
    )

with col3:
    avg_gap = round(df['obs_value_pay_gap'].mean(), 1)
    st.metric(
        label="Average pay gap",
        value=f"{avg_gap}%"
    )

with col4:
    pct_positive = round(
        (df['obs_value_pay_gap'] > 0).sum() / len(df) * 100, 1
    )
    st.metric(
        label="Records where men earn more",
        value=f"{pct_positive}%"
    )

st.divider()

# -------------------------------------------------------
# Navigation tabs
# -------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "🌍 The Problem",
    "🔍 Patterns & Causes",
    "🤖 Simulate"
])

# -------------------------------------------------------
# TAB 1: The Problem
# -------------------------------------------------------
with tab1:
    st.subheader("The gender pay gap is a global phenomenon")
    st.markdown("Average pay gap by country across all available years and occupations.")

    # --- Chart 1: World map ---
    map_data = df.groupby(
        ['ref_area_label', 'ref_area'], as_index=False
    )['obs_value_pay_gap'].mean().round(1)

    map_data.columns = ['country', 'iso_code', 'avg_pay_gap']
    map_data['iso_code'] = map_data['iso_code'].str.upper()

    fig_map = px.choropleth(
        map_data,
        locations='iso_code',
        color='avg_pay_gap',
        hover_name='country',
        hover_data={'avg_pay_gap': ':.1f', 'iso_code': False},
        color_continuous_scale=DIVERGING_PALETTE,
        range_color=[-30, 50],
        labels={'avg_pay_gap': 'Pay gap (%)'},
        title='Average Gender Pay Gap by Country (%)',
        template=PLOTLY_TEMPLATE
    )

    fig_map.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=40, b=0),
        coloraxis_colorbar=dict(title="Pay gap (%)"),
        paper_bgcolor='white',
        geo=dict(bgcolor='white', lakecolor='lightblue')
    )

    st.plotly_chart(fig_map, use_container_width=True)

    st.caption(
        "Positive values = men earn more. "
        "Negative values = women earn more. "
        "Grey = no data available."
    )

    st.divider()

    # --- Chart 2: Historical trend ---
    st.markdown("### Has the gap improved over time?")
    st.markdown("Global average pay gap per year.")

    trend_data = df.groupby(
        'time', as_index=False
    )['obs_value_pay_gap'].mean().round(1)

    fig_trend = px.line(
        trend_data,
        x='time',
        y='obs_value_pay_gap',
        labels={
            'time': 'Year',
            'obs_value_pay_gap': 'Average pay gap (%)'
        },
        title='Global Average Gender Pay Gap Over Time',
        markers=True,
        template=PLOTLY_TEMPLATE
    )

    fig_trend.add_hline(
        y=0,
        line_dash='dash',
        line_color='gray',
        annotation_text='Parity line (0%)'
    )

    fig_trend.update_traces(line_color=PRIMARY_COLOR, marker_color=PRIMARY_COLOR)
    fig_trend.update_layout(height=400, paper_bgcolor='white')

    st.plotly_chart(fig_trend, use_container_width=True)

    st.divider()

    # --- Chart 3: Pay gap evolution by country ---
    st.markdown("### How has the gap evolved in each country?")
    st.markdown("Select one or more countries to compare their evolution over time.")

    available_countries = sorted(df['ref_area_label'].unique().tolist())

    selected_countries = st.multiselect(
        "Select countries",
        options=available_countries,
        default=['argentina', 'francia', 'estados unidos de américa']
    )

    if selected_countries:
        country_trend_data = df[
            df['ref_area_label'].isin(selected_countries)
        ].groupby(
            ['ref_area_label', 'time'], as_index=False
        )['obs_value_pay_gap'].mean().round(1)

        fig_country = px.line(
            country_trend_data,
            x='time',
            y='obs_value_pay_gap',
            color='ref_area_label',
            markers=True,
            labels={
                'time': 'Year',
                'obs_value_pay_gap': 'Average pay gap (%)',
                'ref_area_label': 'Country'
            },
            title='Gender Pay Gap Evolution by Country',
            template=PLOTLY_TEMPLATE
        )

        fig_country.add_hline(
            y=0,
            line_dash='dash',
            line_color='gray',
            annotation_text='Parity line (0%)'
        )

        fig_country.update_layout(
            height=450,
            paper_bgcolor='white',
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=-0.3,
                xanchor='center',
                x=0.5
            )
        )

        st.plotly_chart(fig_country, use_container_width=True)
    else:
        st.info("Please select at least one country to display the chart.")

# -------------------------------------------------------
# TAB 2: Patterns & Causes
# -------------------------------------------------------
with tab2:
    st.subheader("The gap has patterns across occupations and regions")

    # --- Chart 4: Pay gap by occupation ---
    st.markdown("### Which occupations have the largest gap?")
    st.markdown("Average pay gap by occupation across all countries and years.")

    occupation_data = df.groupby(
        'classif1_label', as_index=False
    )['obs_value_pay_gap'].mean().round(1)

    occupation_data = occupation_data.sort_values(
        'obs_value_pay_gap', ascending=True
    )

    fig_occ = px.bar(
        occupation_data,
        x='obs_value_pay_gap',
        y='classif1_label',
        orientation='h',
        labels={
            'obs_value_pay_gap': 'Average pay gap (%)',
            'classif1_label': 'Occupation'
        },
        title='Average Gender Pay Gap by Occupation (%)',
        color='obs_value_pay_gap',
        color_continuous_scale='Reds',
        range_color=[0, 35],
        template=PLOTLY_TEMPLATE
    )

    fig_occ.update_layout(
        height=600,
        showlegend=False,
        paper_bgcolor='white'
    )

    fig_occ.add_vline(
        x=0,
        line_dash='dash',
        line_color='gray',
        annotation_text='Parity (0%)'
    )

    st.plotly_chart(fig_occ, use_container_width=True)

    st.divider()

    # --- Chart 5: Earnings ratio vs pay gap ---
    st.markdown("### What drives the gap?")
    st.markdown(
        "Relationship between the female-to-male earnings ratio and the pay gap. "
        "Each point is one country-occupation-year record."
    )

    sample_data = df.sample(n=2000, random_state=42)

    fig_scatter_earnings = px.scatter(
        sample_data,
        x='earnings_ratio',
        y='obs_value_pay_gap',
        labels={
            'earnings_ratio': 'Earnings ratio (women / men)',
            'obs_value_pay_gap': 'Pay gap (%)'
        },
        title='Earnings Ratio vs Pay Gap',
        hover_data=['ref_area_label', 'time'],
        opacity=0.5,
        template=PLOTLY_TEMPLATE,
        color='obs_value_pay_gap',
        color_continuous_scale='Spectral_r',
        range_color=[-30, 40]
    )

    fig_scatter_earnings.add_hline(
        y=0, line_dash='dash', line_color='gray'
    )
    fig_scatter_earnings.add_vline(
        x=1, line_dash='dash', line_color='gray',
        annotation_text='Equal earnings (ratio=1)'
    )

    fig_scatter_earnings.update_layout(
        height=450,
        paper_bgcolor='white'
    )

    st.plotly_chart(fig_scatter_earnings, use_container_width=True)

    st.divider()

    # --- Chart 6: Hours ratio vs pay gap ---
    st.markdown(
        "Relationship between the female-to-male hours ratio and the pay gap."
    )

    fig_scatter_hours = px.scatter(
        sample_data,
        x='hours_ratio',
        y='obs_value_pay_gap',
        labels={
            'hours_ratio': 'Hours ratio (women / men)',
            'obs_value_pay_gap': 'Pay gap (%)'
        },
        title='Hours Ratio vs Pay Gap',
        hover_data=['ref_area_label', 'time'],
        opacity=0.5,
        template=PLOTLY_TEMPLATE,
        color='obs_value_pay_gap',
        color_continuous_scale='Spectral_r',
        range_color=[-30, 40]
    )

    fig_scatter_hours.add_hline(
        y=0, line_dash='dash', line_color='gray'
    )
    fig_scatter_hours.add_vline(
        x=1, line_dash='dash', line_color='gray',
        annotation_text='Equal hours (ratio=1)'
    )

    fig_scatter_hours.update_layout(
        height=450,
        paper_bgcolor='white'
    )

    st.plotly_chart(fig_scatter_hours, use_container_width=True)

# -------------------------------------------------------
# TAB 3: Simulate
# -------------------------------------------------------
with tab3:
    st.subheader("Simulate labor market scenarios with our XGBoost model")
    st.markdown(
        "Adjust the labor market characteristics below to simulate different scenarios. "
        "The model predicts the expected pay gap based on conditions like earnings, "
        "working hours, and employment — not based on the year alone."
    )
    st.divider()

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown("#### Input features")

        year = st.slider(
            "Reference year (contextual)",
            min_value=1969,
            max_value=2035,
            value=2030
        )
        st.caption(
            "💡 The year provides historical context but the prediction is primarily "
            "driven by the labor market variables below."
        )

        earnings_women = st.number_input(
            "Hourly earnings - Women (USD)",
            min_value=0.0,
            max_value=200.0,
            value=10.0,
            step=0.5
        )

        earnings_men = st.number_input(
            "Hourly earnings - Men (USD)",
            min_value=0.0,
            max_value=200.0,
            value=12.0,
            step=0.5
        )

        employees_women = st.number_input(
            "Female employees (thousands)",
            min_value=0.0,
            max_value=100000.0,
            value=500.0,
            step=100.0
        )

        employees_men = st.number_input(
            "Male employees (thousands)",
            min_value=0.0,
            max_value=100000.0,
            value=500.0,
            step=100.0
        )

        hours_women = st.number_input(
            "Weekly hours worked - Women",
            min_value=0.0,
            max_value=100.0,
            value=38.0,
            step=0.5
        )

        hours_men = st.number_input(
            "Weekly hours worked - Men",
            min_value=0.0,
            max_value=100.0,
            value=40.0,
            step=0.5
        )

        occupation_options = sorted(label_encoders['classif1_label'].classes_.tolist())
        occupation = st.selectbox(
            "Occupation",
            options=occupation_options
        )

        region_options = sorted(label_encoders['ref_area_label'].classes_.tolist())
        region = st.selectbox(
            "Country",
            options=region_options,
            index=region_options.index('argentina')
        )

    with col_right:
        st.markdown("#### Prediction")
        st.markdown(" ")

        if st.button("🔮 Simulate scenario", use_container_width=True):

            earnings_ratio = earnings_women / earnings_men if earnings_men > 0 else 0
            hours_ratio = hours_women / hours_men if hours_men > 0 else 0
            employment_ratio = employees_women / employees_men if employees_men > 0 else 0
            delta_earnings = earnings_men - earnings_women
            delta_hours = hours_men - hours_women

            payload = {
                "time": year,
                "ref_area": df[df['ref_area_label'] == region]['ref_area'].iloc[0],
                "ref_area_label": region,
                "classif1": df[df['classif1_label'] == occupation]['classif1'].iloc[0],
                "classif1_label": occupation,
                "obs_status_label": df[df['classif1_label'] == occupation]['obs_status_label'].iloc[0],
                "obs_value_employees_women": employees_women,
                "obs_value_employees_men": employees_men,
                "obs_value_earnings_women": earnings_women,
                "obs_value_earnings_men": earnings_men,
                "obs_value_hours_women": hours_women,
                "obs_value_hours_men": hours_men,
                "earnings_ratio": earnings_ratio,
                "hours_ratio": hours_ratio,
                "employment_ratio": employment_ratio,
                "delta_earnings": delta_earnings,
                "delta_hours": delta_hours
            }

            API_URL = "https://gender-pay-gap-api.onrender.com/predict"

            try:
                response = requests.post(API_URL, json=payload, timeout=30)

                if response.status_code == 200:
                    result = response.json()
                    predicted_gap = result.get('predicted_pay_gap', None)

                    if predicted_gap is not None:
                        st.metric(
                            label="Predicted gender pay gap",
                            value=f"{round(predicted_gap, 2)}%"
                        )

                        if predicted_gap > 10:
                            st.error(
                                f"⚠️ High gap: men earn significantly more than women "
                                f"in this context ({round(predicted_gap, 2)}%)"
                            )
                        elif predicted_gap > 0:
                            st.warning(
                                f"Men earn slightly more than women "
                                f"({round(predicted_gap, 2)}%)"
                            )
                        else:
                            st.success(
                                f"✅ In this context women earn as much or more than men "
                                f"({round(predicted_gap, 2)}%)"
                            )
                else:
                    st.error(
                        f"API error: {response.status_code}. "
                        f"Details: {response.text}"
                    )

            except requests.exceptions.Timeout:
                st.warning(
                    "⏳ The API is waking up (Render free tier goes to sleep). "
                    "Please wait 30 seconds and try again."
                )
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")

        st.divider()

        st.markdown("#### About the model")
        st.markdown(
            "- **Algorithm:** XGBoost Regressor\n"
            "- **R² score:** 0.9509\n"
            "- **Training data:** ILOSTAT (ILO)\n"
            "- **API:** FastAPI deployed on Render\n"
            "- **Features used:** year, hourly earnings, number of employees, "
            "weekly hours worked, occupation and country"
        )