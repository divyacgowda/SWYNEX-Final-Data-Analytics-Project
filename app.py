import base64
import time
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Titanic Survival Analytics",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "titanic_cleaned.csv"
HEADER_IMAGE_PATH = BASE_DIR / "assets" / "titanic_header.png"


# --------------------------------------------------
# 2. CUSTOM DASHBOARD DESIGN
# --------------------------------------------------

st.markdown("""
<style>
.stApp {
    background: #071426;
    color: #E5EDF8;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.6rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #0D1D33;
    border-right: 1px solid #203751;
}

[data-testid="stSidebar"] * {
    color: #E5EDF8;
}

h1, h2, h3, p, label {
    color: #E5EDF8;
}

.hero {
    background: linear-gradient(115deg, #102B49, #123E54, #172B51);
    border: 1px solid #28506A;
    border-radius: 20px;
    padding: 28px 32px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
    color: #F4F8FF;
    margin-bottom: 7px;
}

.hero-subtitle {
    color: #A8C5D8;
    font-size: 14px;
}

.hero-tag {
    display: inline-block;
    color: #5EEAD4;
    background: #123D4A;
    border: 1px solid #27616B;
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.hero-ship {
    font-size: 65px;
    text-align: center;
}

.metric-card {
    background: linear-gradient(140deg, #142C47, #102239);
    border: 1px solid #294665;
    border-radius: 16px;
    padding: 19px 20px;
    min-height: 125px;
}

.metric-label {
    color: #A6BAD0;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 13px;
}

.metric-value {
    color: #F5F8FF;
    font-size: 29px;
    font-weight: 800;
}

.metric-note {
    color: #69DCCB;
    font-size: 11px;
    margin-top: 7px;
}

.section-title {
    color: #F1F6FF;
    font-size: 19px;
    font-weight: 750;
    margin-top: 22px;
    margin-bottom: 12px;
}

.-title {
    color: #EAF2FF;
    font-size: 15px;
    font-weight: 700;
    machartrgin-bottom: 4px;
}

.chart-caption {
    color: #8FA9C5;
    font-size: 11px;
    margin-bottom: 8px;
}

.insight-box {
    background: linear-gradient(135deg, #102B43, #172746);
    border: 1px solid #31506D;
    border-radius: 16px;
    padding: 17px;
    margin-bottom: 12px;
    min-height: 105px;
}

.insight-label {
    color: #65DCCB;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 8px;
}

.insight-value {
    color: #F4F8FF;
    font-size: 17px;
    font-weight: 750;
}

.footer {
    text-align: center;
    color: #7891AA;
    font-size: 11px;
    padding-top: 28px;
    border-top: 1px solid #203751;
    margin-top: 35px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #0C1C30;
    border-color: #203751 !important;
    border-radius: 16px;
}

.stButton > button {
    background: linear-gradient(90deg, #0D9488, #0F766E);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

.stButton > button:hover {
    border: 1px solid #5EEAD4;
    color: white;
}
/* KPI Cards Entrance Animation */
@keyframes kpiFadeUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.metric-card {
    animation: kpiFadeUp 0.8s ease-out both;
}

.metric-card:nth-child(1) {
    animation-delay: 0.1s;
}

.metric-card:nth-child(2) {
    animation-delay: 0.2s;
}

.metric-card:nth-child(3) {
    animation-delay: 0.3s;
}

.metric-card:nth-child(4) {
    animation-delay: 0.4s;
}

/* Chart Card Hover Animation */
div[class*="st-key-chart-card-"] {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

div[class*="st-key-chart-card-"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 180, 255, 0.25);
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 10px 25px rgba(0, 180, 255, 0.25) !important;
    outline: 1px solid rgba(0, 180, 255, 0.5);
}

div[class*="st-key-chart-card-"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 180, 255, 0.22);
}

div[data-testid="stVerticalBlockBorderWrapper"]:has(.chart-title):hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 180, 255, 0.18);
    border-color: rgba(0, 180, 255, 0.6);
}
/* =================================
   TITANIC SIDEBAR DESIGN
================================= */

/* Sidebar background */
[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(
        180deg,
        #071A2E 0%,
        #102B49 55%,
        #0A2038 100%
    );
    border-right: 1px solid rgba(66, 153, 225, 0.25);
}

/* Sidebar heading */
[data-testid="stSidebar"] h2 {
    color: #EAF6FF !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(105, 180, 230, 0.25);
}

/* Sidebar descriptions */
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #8FA9C5 !important;
}

/* Filter labels */
[data-testid="stSidebar"] label {
    color: #DCEBFA !important;
    font-weight: 600 !important;
}

/* Dropdown boxes */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #102B49 !important;
    border: 1px solid #28506A !important;
    border-radius: 10px !important;
    transition: border-color 0.3s ease,
                box-shadow 0.3s ease;
}

/* Dropdown hover */
[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
    border-color: #39A9E8 !important;
    box-shadow: 0 0 10px rgba(57, 169, 232, 0.15);
}

/* Reset button */
[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(110deg, #12618A, #168AAD);
    color: white !important;
    border: 1px solid #36A9E1;
    border-radius: 10px;
    font-weight: 600;
    height: 42px;
    transition: all 0.3s ease;
}

/* Reset button hover */
[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(110deg, #168AAD, #219EBC);
    box-shadow: 0 5px 16px rgba(33, 158, 188, 0.3);
    transform: translateY(-2px);
}

/* Sidebar divider */
[data-testid="stSidebar"] hr {
    border-color: rgba(105, 180, 230, 0.25);
}
/* =====================================
   NAVIGATION CATEGORY CARDS
===================================== */

/* Outer card */
div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stButton"]) {
    background: linear-gradient(
        145deg,
        #102B49,
        #0A1B30
    ) !important;

    border: 1px solid #28506A !important;
    border-radius: 16px !important;
    padding: 12px !important;

    transition: all 0.3s ease;
}

/* Card hover */
div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stButton"]):hover {
    border-color: #36A9E1 !important;
    box-shadow: 0 8px 22px rgba(54, 169, 225, 0.16);
    transform: translateY(-3px);
}

/* Unselected navigation button */
div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stButton"]) [data-testid="baseButton-secondary"] {
    background: #102B49 !important;
    color: #DCEBFA !important;
    border: 1px solid #35627F !important;
    border-radius: 10px !important;
    min-height: 52px;
    font-size: 15px !important;
    font-weight: 700 !important;
    text-align: left !important;
    box-shadow: none !important;
}

/* Selected navigation button */
div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stButton"]) [data-testid="baseButton-primary"] {
    background: linear-gradient(
        110deg,
        #12618A,
        #168AAD
    ) !important;
    color: white !important;
    border: 1px solid #36A9E1 !important;
    border-radius: 10px !important;
    min-height: 52px;
    font-size: 15px !important;
    font-weight: 700 !important;
    box-shadow: 0 0 14px rgba(54, 169, 225, 0.18) !important;
}

/* Card descriptions */
div[data-testid="stVerticalBlockBorderWrapper"]:has([data-testid="stButton"]) [data-testid="stCaptionContainer"] {
    color: #A8BCD0 !important;
    font-size: 12px !important;
    padding: 4px 4px 0;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITANIC HEADER IMAGE
# --------------------------------------------------

if HEADER_IMAGE_PATH.exists():
    image_data = base64.b64encode(
        HEADER_IMAGE_PATH.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <style>
        .hero {{
            background-image:
                linear-gradient(
                    rgba(4, 15, 30, 0.45),
                    rgba(4, 15, 30, 0.60)
                ),
                url("data:image/png;base64,{image_data}") !important;
            background-size: cover !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



# --------------------------------------------------
# 3. LOAD AND PREPARE DATA
# --------------------------------------------------

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

    required_columns = [
        "PassengerId", "Survived", "Pclass", "Sex",
        "Age", "SibSp", "Parch", "Fare", "Embarked"
    ]

    missing_columns = [
        col for col in required_columns if col not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Dataset is missing these columns: {missing_columns}"
        )

    numeric_columns = [
        "Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"
    ]

    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["Sex"] = data["Sex"].astype("string").str.title()
    data["Embarked"] = data["Embarked"].astype("string").str.upper()

    data["FamilySize"] = (
        data["SibSp"] + data["Parch"] + 1
    )

    data["AgeGroup"] = pd.cut(
        data["Age"],
        bins=[-0.001, 12, 18, 35, 60, np.inf],
        labels=[
            "Child",
            "Teenager",
            "Young Adult",
            "Adult",
            "Senior"
        ],
        include_lowest=True
    )

    data["Survival Status"] = data["Survived"].map({
        0: "Did Not Survive",
        1: "Survived"
    })

    data["Passenger Class"] = data["Pclass"].map({
        1: "1st Class",
        2: "2nd Class",
        3: "3rd Class"
    })

    return data


try:
    df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error(
        "Dataset not found. Please place titanic_cleaned.csv "
        "inside the project's data folder."
    )
    st.stop()
except Exception as error:  # noqa: BLE001
    st.error(f"Unable to load the dataset: {error}")
    st.stop()


# --------------------------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.markdown("## ⚙️ Dashboard Controls")
st.sidebar.caption("Filter the passenger data")

if st.sidebar.button("↺ Reset Filters", use_container_width=True):
    for key in [
        "gender_filter",
        "class_filter",
        "age_filter",
        "port_filter"
    ]:
        st.session_state[key] = "All"

    st.rerun()

gender = st.sidebar.selectbox(
    "👤 Gender",
    ["All", "Female", "Male"],
    key="gender_filter"
)

passenger_class = st.sidebar.selectbox(
    "🎫 Passenger Class",
    ["All", "1st Class", "2nd Class", "3rd Class"],
    key="class_filter"
)

age_group = st.sidebar.selectbox(
    "🎂 Age Group",
    [
        "All", "Child", "Teenager",
        "Young Adult", "Adult", "Senior"
    ],
    key="age_filter"
)

port = st.sidebar.selectbox(
    "⚓ Embarkation Port",
    ["All", "C", "Q", "S"],
    key="port_filter"
)

st.sidebar.markdown("---")
st.sidebar.caption("SWYNEX | Data Analyst Internship")
st.sidebar.caption("Dataset: Titanic Passenger Records")


# --------------------------------------------------
# 5. APPLY FILTERS
# --------------------------------------------------

filtered = df.copy()

if gender != "All":
    filtered = filtered[filtered["Sex"] == gender]

if passenger_class != "All":
    filtered = filtered[
        filtered["Passenger Class"] == passenger_class
    ]

if age_group != "All":
    filtered = filtered[
        filtered["AgeGroup"].astype("string") == age_group
    ]

if port != "All":
    filtered = filtered[filtered["Embarked"] == port]


# --------------------------------------------------
# 6. REUSABLE DESIGN FUNCTIONS
# --------------------------------------------------

COLORS = {
    "Survived": "#2DD4BF",
    "Did Not Survive": "#F472B6",
    "Female": "#C084FC",
    "Male": "#38BDF8",
    "Primary": "#38BDF8",
    "Secondary": "#A78BFA",
    "Accent": "#F472B6"
}


def style_chart(fig, height=330):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={
            "color": "#DCE8F7",
            "family": "Segoe UI, sans-serif",
            "size": 11
        },
        margin={"l": 15, "r": 15, "t": 38, "b": 15},
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1
        }
    )

    fig.update_xaxes(
        gridcolor="rgba(148,163,184,0.12)",
        zerolinecolor="rgba(148,163,184,0.12)"
    )

    fig.update_yaxes(
        gridcolor="rgba(148,163,184,0.12)",
        zerolinecolor="rgba(148,163,184,0.12)"
    )

    return fig


def show_chart(title, fig, caption="Interactive visualization"):

    with st.container(
        border=True,
        key=f"chart-card-{title.lower().replace(' ', '-')}"
    ):

        st.markdown(
            f"""
            <div class="chart-title"
                 style="font-size:17px;
                        font-weight:700;
                        color:#EAF6FF;
                        margin-bottom:5px;">
                {title}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="chart-caption"
                 style="color:#8FA9C5;
                        font-size:11px;
                        margin-bottom:12px;">
                {caption}
            </div>
            """,
            unsafe_allow_html=True
        )

        if fig is not None:

            # Detect heatmap charts
            is_heatmap = any(
                trace.type == "heatmap"
                for trace in fig.data
            )

            # Consistent chart theme
            fig.update_layout(
                template="plotly_dark",

                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",

                font={
                    "family": "Arial, sans-serif",
                    "size": 12,
                    "color": "#DCEBFA"
                },

                # Ocean-inspired color palette
                colorway=[
                    "#36A9E1",
                    "#20C997",
                    "#F4B942",
                    "#E76F51",
                    "#8B9DFF",
                    "#A78BFA"
                ],

                # Consistent spacing
                margin={
                    "l": 25,
                    "r": 20,
                    "t": 35,
                    "b": 35
                },

                # Consistent legends
                legend={
                    "orientation": "h",
                    "yanchor": "bottom",
                    "y": 1.02,
                    "xanchor": "right",
                    "x": 1,
                    "bgcolor": "rgba(0,0,0,0)",
                    "font": {
                        "size": 11,
                        "color": "#DCEBFA"
                    },
                    "title_text": ""
                },

                # Styled hover tooltips
                hoverlabel={
                    "bgcolor": "#102B49",
                    "bordercolor": "#36A9E1",
                    "font": {
                        "color": "#EAF6FF",
                        "size": 12
                    },
                    "align": "left"
                }
            )

            # Consistent axis styling
            fig.update_xaxes(
                showgrid=False,
                zeroline=False,
                linecolor="rgba(143,169,197,0.25)",
                tickfont={"color": "#B8CCE0"}
            )

            fig.update_yaxes(
                showgrid=not is_heatmap,
                gridcolor="rgba(143,169,197,0.14)",
                zeroline=False,
                linecolor="rgba(143,169,197,0.25)",
                tickfont={"color": "#B8CCE0"}
            )
            
            

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False,
                    "displaylogo": False,
                    "responsive": True
                }
            )

        else:
            st.info("Not enough matching data to display this chart.")
            
            
            
            
def highest_rate(data, column):
    if data.empty:
        return "No data"

    rates = (
        data.groupby(column, observed=True)["Survived"]
        .mean()
        .mul(100)
        .dropna()
    )

    if rates.empty:
        return "Not available"

    best = rates.idxmax()
    return f"{best}: {rates.loc[best]:.1f}%"


# --------------------------------------------------
# 7. DASHBOARD HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div class="hero-tag">SWYNEX • DATA ANALYTICS PROJECT</div>
    <div class="hero-title">
        Titanic Survival Analytics Dashboard
    </div>
    <div class="hero-subtitle">
        Exploring passenger survival patterns through interactive data visualization
    </div>
    <div style="height: 80px;"></div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# 8. KPI CARDS
# --------------------------------------------------

total = len(filtered)
survivors = int((filtered["Survived"] == 1).sum())
deaths = int((filtered["Survived"] == 0).sum())

survival_rate = (
    survivors / total * 100
    if total > 0 else 0
)

st.markdown(
    '<div class="section-title">📊 Passenger Overview</div>',
    unsafe_allow_html=True
)

kpi_data = [
    ("TOTAL PASSENGERS", f"{total:,}", "Passengers in current selection"),
    ("TOTAL SURVIVORS", f"{survivors:,}", "Passengers who survived"),
    ("TOTAL DEATHS", f"{deaths:,}", "Passengers who did not survive"),
    ("SURVIVAL RATE", f"{survival_rate:.2f}%", "Survival percentage")
]

columns = st.columns(4)

for col, (label, value, note) in zip(columns, kpi_data):
    with col:
        if label == "SURVIVAL RATE":
            placeholder = st.empty()

            for step in range(51):
                animated_rate = survival_rate * step / 50

                placeholder.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{animated_rate:.2f}%</div>
                    <div class="metric-note">{note}</div>
                </div>
                """, unsafe_allow_html=True)

                time.sleep(0.04)

        else:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """, unsafe_allow_html=True)


# --------------------------------------------------
# 9. EMPTY FILTER RESULT HANDLING
# --------------------------------------------------

if filtered.empty:
    st.warning(
        "No passengers match the selected filters. "
        "Try changing or resetting your filters."
    )
    st.stop()
st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)


# --------------------------------------------------
# 10. CHART 1: SURVIVAL BY GENDER
# --------------------------------------------------

gender_stats = (
    filtered.groupby(["Sex", "Survival Status"], observed=True)
    .size()
    .reset_index(name="Passengers")
)

fig_gender = px.bar(
    gender_stats,
    x="Sex",
    y="Passengers",
    color="Survival Status",
    barmode="group",
    color_discrete_map=COLORS,
    text_auto=True
)

fig_gender.update_layout(
    xaxis_title="Gender",
    yaxis_title="Number of Passengers"
)


# --------------------------------------------------
# 11. CHART 2: SURVIVAL BY CLASS
# --------------------------------------------------

class_stats = (
    filtered.groupby("Passenger Class", observed=True)["Survived"]
    .mean()
    .mul(100)
    .reset_index(name="Survival Rate")
)

fig_class = px.bar(
    class_stats,
    x="Passenger Class",
    y="Survival Rate",
    color="Passenger Class",
    category_orders={
        "Passenger Class": ["1st Class", "2nd Class", "3rd Class"]
    },
    color_discrete_sequence=["#2DD4BF", "#38BDF8", "#A78BFA"],
    text_auto=".1f"
)

fig_class.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_class.update_layout(
    showlegend=False,
    yaxis_title="Survival Rate (%)",
    xaxis_title="Passenger Class",
    yaxis_range=[0, 110]
)

# --------------------------------------------------
# CLICKABLE CHART CATEGORY CARDS
# --------------------------------------------------

if "chart_section" not in st.session_state:
    st.session_state.chart_section = "📊 Survival Analysis"


row1_col1, row1_col2 = st.columns(2, gap="large")
row2_col1, row2_col2 = st.columns(2, gap="large")


with row1_col1:  # noqa: SIM117
    with st.container(border=True):
        if st.button(
            "📊 Survival Analysis",
            key="card_survival",
            type="primary" if st.session_state.chart_section == "📊 Survival Analysis" else "secondary",
            width="stretch"
        ):
            st.session_state.chart_section = "📊 Survival Analysis"
            st.rerun()

        st.caption("Survival patterns by gender and passenger class")


with row1_col2:  # noqa: SIM117
    with st.container(border=True):
        if st.button(
            "👥 Passenger Demographics",
            key="card_demographics",
            type="primary" if st.session_state.chart_section == "👥 Passenger Demographics" else "secondary",
            width="stretch"
        ):
            st.session_state.chart_section = "👥 Passenger Demographics"
            st.rerun()

        st.caption("Age distribution and fare analysis")


with row2_col1:  # noqa: SIM117
    with st.container(border=True):
        if st.button(
            "👨‍👩‍👧 Family & Travel",
            key="card_family",
            type="primary" if st.session_state.chart_section == "👨‍👩‍👧 Family & Travel" else "secondary",
            width="stretch"
        ):
            st.session_state.chart_section = "👨‍👩‍👧 Family & Travel"
            st.rerun()

        st.caption("Family size and embarkation ports")


with row2_col2:  # noqa: SIM117
    with st.container(border=True):
        if st.button(
            "🌐 Advanced Insights",
            key="card_advanced",
            type="primary" if st.session_state.chart_section == "🌐 Advanced Insights" else "secondary",
            width="stretch"
        ):
            st.session_state.chart_section = "🌐 Advanced Insights"
            st.rerun()

        st.caption("Correlation and survival heatmaps")


chart_section = st.session_state.chart_section
if chart_section == "📊 Survival Analysis":

    col1, col2 = st.columns(2, gap="large")

    with col1:
        show_chart(
            "👥 Survival by Gender",
            style_chart(fig_gender, height=300),
            "Survival comparison by gender"
        )

    with col2:
        show_chart(
            "🎫 Survival by Passenger Class",
            style_chart(fig_class, height=300),
            "Survival percentage across passenger classes"
        )


# --------------------------------------------------
# 12. CHART 3: AGE DISTRIBUTION
# --------------------------------------------------

fig_age = px.histogram(
    filtered,
    x="Age",
    color="Survival Status",
    nbins=25,
    barmode="overlay",
    opacity=0.78,
    color_discrete_map=COLORS
)

fig_age.update_layout(
    xaxis_title="Passenger Age",
    yaxis_title="Number of Passengers"
)


# --------------------------------------------------
# 13. CHART 4: FARE DISTRIBUTION
# --------------------------------------------------

fig_fare = px.histogram(
    filtered,
    x="Fare",
    color="Survival Status",
    nbins=30,
    barmode="overlay",
    opacity=0.75,
    color_discrete_map=COLORS
)

fig_fare.update_layout(
    xaxis_title="Ticket Fare",
    yaxis_title="Number of Passengers"
)

if chart_section == "👥 Passenger Demographics":

    col1, col2 = st.columns(2, gap="large")

    with col1:
        show_chart(
            "🎂 Age Distribution",
            style_chart(fig_age, height=300),
            "Passenger age distribution by survival status"
        )

    with col2:
        show_chart(
            "💰 Fare Distribution",
            style_chart(fig_fare, height=300),
            "Ticket fare distribution by survival status"
        )


# --------------------------------------------------
# 14. CHART 5: FAMILY SIZE ANALYSIS
# --------------------------------------------------

family_stats = (
    filtered.groupby("FamilySize")
    .agg(
        Passengers=("Survived", "size"),
        Survival_Rate=("Survived", "mean")
    )
    .reset_index()
)

family_stats["Survival_Rate"] *= 100

fig_family = px.bar(
    family_stats,
    x="FamilySize",
    y="Survival_Rate",
    color="Survival_Rate",
    color_continuous_scale=["#2563EB", "#2DD4BF"],
    text_auto=".1f"
)

fig_family.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_family.update_layout(
    coloraxis_showscale=False,
    xaxis_title="Family Size",
    yaxis_title="Survival Rate (%)",
    yaxis_range=[0, min(
        110,
        max(100, float(family_stats["Survival_Rate"].max()) + 10)
    )]
)


# --------------------------------------------------
# 15. CHART 6: EMBARKATION PORT
# --------------------------------------------------

port_counts = (
    filtered["Embarked"]
    .dropna()
    .value_counts()
    .rename_axis("Port")
    .reset_index(name="Passengers")
)

fig_port = px.pie(
    port_counts,
    names="Port",
    values="Passengers",
    hole=0.62,
    color="Port",
    color_discrete_map={
        "C": "#2DD4BF",
        "Q": "#A78BFA",
        "S": "#38BDF8"
    }
)

fig_port.update_traces(
    textposition="inside",
    textinfo="percent+label",
    marker={"line": {"color": "#0C1C30", "width": 3}}
)

if chart_section == "👨‍👩‍👧 Family & Travel":

    col1, col2 = st.columns(2, gap="large")

    with col1:
        show_chart(
            "👨‍👩‍👧 Family Size Analysis",
            style_chart(fig_family, height=300),
            "Family size compared with survival rate"
        )

    with col2:
        show_chart(
            "⚓ Embarkation Port Analysis",
            style_chart(fig_port, height=300),
            "Passenger distribution across embarkation ports"
        )


# --------------------------------------------------
# 16. CHART 7: CORRELATION HEATMAP
# --------------------------------------------------

numeric_columns = [
    "Survived", "Pclass", "Age",
    "SibSp", "Parch", "Fare", "FamilySize"
]

correlation = filtered[numeric_columns].corr()

fig_corr = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale=[
        "#172554", "#2563EB", "#2DD4BF"
    ],
    zmin=-1,
    zmax=1
)

fig_corr.update_layout(
    coloraxis_colorbar_title="Correlation"
)


# --------------------------------------------------
# 17. CHART 8: GENDER AND CLASS
# --------------------------------------------------

gender_class = (
    filtered.pivot_table(
        values="Survived",
        index="Sex",
        columns="Pclass",
        aggfunc="mean"
    ) * 100
)

fig_gender_class = px.imshow(
    gender_class,
    text_auto=".1f",
    aspect="auto",
    color_continuous_scale=[
        "#172554", "#2563EB", "#2DD4BF"
    ],
    zmin=0,
    zmax=100,
    labels={
        "x": "Passenger Class",
        "y": "Gender",
        "color": "Survival Rate (%)"
    }
)

fig_gender_class.update_layout(
    coloraxis_colorbar_title="Survival %"
)

if chart_section == "🌐 Advanced Insights":

    col1, col2 = st.columns(2, gap="large")

    with col1:
        show_chart(
            "🌐 Correlation Heatmap",
            style_chart(fig_corr, height=330),
            "Relationships between numerical passenger features"
        )

    with col2:
        show_chart(
            "🧑 Gender and Passenger Class",
            style_chart(fig_gender_class, height=330),
            "Survival percentage by gender and passenger class"
        )
# 18. DYNAMIC KEY INSIGHTS
# --------------------------------------------------
# 19. FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    TITANIC SURVIVAL ANALYTICS DASHBOARD
    <br>
    Built with Python • Streamlit • Pandas • Plotly
    <br>
    SWYNEX Data Analyst Internship Project
</div>
""", unsafe_allow_html=True)
