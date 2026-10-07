import streamlit as st
import pandas as pd

from crawler import crawl_page
from classifier import classify_resource
from analytics import create_category_chart


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Educational Resource Discovery",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📚 Intelligent Educational Resource Discovery and Analytics System")

st.write(
    "Discover, classify and analyze useful educational resources "
    "using intelligent resource discovery techniques."
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_resources():
    return pd.read_csv("resources.csv")


try:
    data = load_resources()

except Exception as error:
    st.error(f"Unable to load resources.csv: {error}")
    st.stop()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🔎 Resource Search")

search_text = st.sidebar.text_input(
    "Search educational resources"
)

categories = ["All"] + sorted(
    data["category"].dropna().unique().tolist()
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)


# --------------------------------------------------
# SEARCH AND FILTER
# --------------------------------------------------

filtered_data = data.copy()


if search_text:
    search_lower = search_text.lower()

    filtered_data = filtered_data[
        filtered_data["title"].str.lower().str.contains(
            search_lower,
            na=False
        )
        |
        filtered_data["description"].str.lower().str.contains(
            search_lower,
            na=False
        )
    ]


if selected_category != "All":
    filtered_data = filtered_data[
        filtered_data["category"] == selected_category
    ]


# --------------------------------------------------
# RESOURCE DISCOVERY
# --------------------------------------------------

st.header("🎓 Educational Resources")

if filtered_data.empty:

    st.warning("No educational resources found.")

else:

    for _, resource in filtered_data.iterrows():

        st.subheader(resource["title"])

        st.write(
            f"**Category:** {resource['category']}"
        )

        st.write(resource["description"])

        st.link_button(
            "🔗 Open Resource",
            resource["url"]
        )

        st.divider()


# --------------------------------------------------
# RESOURCE CRAWLER
# --------------------------------------------------

st.header("🌐 Educational Resource Crawler")

st.write(
    "Enter an educational webpage URL to extract its title "
    "and automatically detect its category."
)

url = st.text_input(
    "Enter Resource URL",
    placeholder="https://example.com"
)


if st.button("🚀 Crawl Resource"):

    if not url.strip():

        st.warning("Please enter a valid URL.")

    else:

        with st.spinner("Analyzing resource..."):

            result = crawl_page(url.strip())

        if result["success"]:

            st.success("Resource successfully analyzed!")

            st.subheader("Resource Information")

            st.write(
                f"**Page Title:** {result['title']}"
            )

            detected_category = classify_resource(
                result["title"],
                result["description"]
            )

            st.write(
                f"**Detected Category:** {detected_category}"
            )

            st.write("**Description / Extracted Content:**")

            st.write(
                result["description"]
            )

            st.link_button(
                "🔗 Open Crawled Resource",
                result["url"]
            )

        else:

            st.error(
                f"Unable to crawl this webpage: {result['error']}"
            )


# --------------------------------------------------
# ANALYTICS DASHBOARD
# --------------------------------------------------

st.header("📊 Analytics Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Resources",
        len(data)
    )

with col2:
    st.metric(
        "Total Categories",
        data["category"].nunique()
    )

with col3:
    st.metric(
        "Search Results",
        len(filtered_data)
    )


st.subheader("📈 Resources by Category")

chart = create_category_chart(data)

st.pyplot(chart)


st.subheader("📋 Resource Dataset")

st.dataframe(
    data,
    use_container_width=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Intelligent Educational Resource Discovery and Analytics System"
)