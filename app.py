import streamlit as st
import requests

st.set_page_config(page_title="News Explorer", page_icon="📰")

st.title("📰 News Headlines Explorer")

api_key = st.sidebar.text_input(
    "Enter NewsAPI Key",
    type="password"
)

country = st.sidebar.selectbox(
    "Country",
    ["us", "in", "gb", "au"]
)

category = st.sidebar.selectbox(
    "Category",
    [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology"
    ]
)

num_articles = st.sidebar.slider(
    "Number of Articles",
    5,
    20,
    10
)

if st.button("Fetch News"):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country={country}&"
        f"category={category}&"
        f"pageSize={num_articles}&"
        f"apiKey={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":

        for article in data["articles"]:

            st.subheader(article["title"])

            if article["urlToImage"]:
                st.image(article["urlToImage"])

            st.write(article["description"])

            st.link_button(
                "Read Full Article",
                article["url"]
            )

            st.divider()

    else:
        st.error("Invalid API Key")

        sort_by = st.selectbox(
    "Sort By",
    ["publishedAt", "relevancy", "popularity"]
)

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={keyword}&"
    f"sortBy={sort_by}&"
    f"pageSize={num_articles}&"
    f"apiKey={api_key}"
)

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Search News", "About"]
)

if page == "Home":
    st.title("News Explorer")

elif page == "Search News":
    st.title("Search News")

elif page == "About":
    st.write("Built using Streamlit and NewsAPI")

    st.metric(
    "Articles Found",
    len(data["articles"])
)

st.set_page_config(
    page_title="News Explorer",
    page_icon="📰",
    layout="wide"
)

col1, col2 = st.columns([1,2])

with col1:
    st.image(article["urlToImage"])

with col2:
    st.subheader(article["title"])

    api_key = st.secrets["NEWS_API_KEY"]