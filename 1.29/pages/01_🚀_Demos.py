import streamlit as st
from PIL import Image
import base64
import pandas as pd
import random
from datetime import datetime
from faker import Faker

@st.cache_data
def get_file_url(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )
    
st.set_page_config("Demos", "🚀", layout="wide")

icon("🚀")
st.title("v1.29 Feature Demos", anchor=False)

st.markdown("""
🔲 [Customizable border](#customizable-border)

⏳ [New app loading animation](#new-app-loading-animation)
""", unsafe_allow_html=True)

# st.divider()

## -------------------------------------------------------------------- ##
# Border Demo
st.markdown('<a name="customizable-border"></a>', unsafe_allow_html=True)
st.header("🔲 Customizable border", divider="rainbow")
st.markdown("You can now customize `st.container` and `st.form` by adding or removing the border")

# Initialize Faker to generate fake data
fake = Faker()

def random_date(start, end):
    return start + (end - start) * random.random()

def create_sample_data(num_rows=10):
    data = {
        # "Order ID": [f"ORD{1000+i}" for i in range(num_rows)],
        "Customer Name": [fake.name() for _ in range(num_rows)],
        "Product": [random.choice(["Laptop", "Smartphone", "Tablet", "Headphones", "Charger"]) for _ in range(num_rows)],
        "Quantity": [random.randint(1, 5) for _ in range(num_rows)],
        "Order Date": [random_date(datetime(2021, 1, 1), datetime(2023, 1, 1)).strftime("%Y-%m-%d") for _ in range(num_rows)]
    }
    return pd.DataFrame(data)
df = create_sample_data(10)

after, before = st.columns(2)

with after:
    st.subheader("New customizable borders")
    st.info("⬇️ The new `st.container` can now be configured to have a border")
   
    with st.container(border=True):
        # st.info("This text and table are inside a container with a border")
        st.dataframe(data=df, use_container_width=True)
        st.button("Refresh data", use_container_width=True, key="after1")

    st.code(
        """
        with st.container(border=True):
            st.dataframe(data=df, use_container_width=True)
            st.button("Refresh data", use_container_width=True)
        """
    )

    st.info("⬇️ The new `st.form` can now be configured to appear without a border")

    with st.form(key="my_form_2", border=False):
        st.dataframe(data=df, use_container_width=True)
        st.form_submit_button(label="Submit")
    
    st.code(
        """
        with st.form(key="my_form_2", border=False):
            st.dataframe(data=df, use_container_width=True)
            st.form_submit_button(label="Submit")
        """
    )

with before:
    st.subheader("Old non-customizable borders")
    st.info("⬇️ The legacy `st.container` does not have a border")
    with st.container():
        st.dataframe(data=df, use_container_width=True)
        st.button("Refresh data", use_container_width=True, key="before1")
        
    # Instead of st.empty(), use a markdown with empty space
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
    
    st.code(
        """
        with st.container():
            st.dataframe(data=df, use_container_width=True)
            st.button("Refresh data", use_container_width=True)
        """
    )

    st.info("⬇️ The legacy `st.form` always has a border")
    with st.form(key="my_form_1"):
        st.dataframe(data=df, use_container_width=True)
        st.form_submit_button(label="Submit")
    st.code(
        """
        with st.form(key="my_form"):
            st.info("This text and table are inside a form with a border")
            st.dataframe(data=df, use_container_width=True)
            st.form_submit_button(label="Submit")
        """
    )


## -------------------------------------------------------------------- ##
# App skeleton Demo
st.markdown('<a name="new-app-loading-animation"></a>', unsafe_allow_html=True)
st.header("⏳ New app loading animation", divider="rainbow")
st.markdown("The ':blue[Please wait...]' message has been updated to a more engaging animation")

old_skeleton_url = get_file_url("/mount/src/release-demos/1.29/pages/old_skeleton.gif")
new_skeleton_url = get_file_url("/mount/src/release-demos/1.29/pages/new_skeleton.gif")
# skeleton_url = get_file_url("/mount/src/release-demos/1.29/pages/skeleton.gif")

gif1, gif2 = st.columns(2)
with gif2:
    st.subheader("Old loading message")
    st.caption("Upon reload, the page shows :blue[Please wait...]")
    st.markdown(
        f'<img src="data:image/gif;base64,{old_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )

with gif1:
    st.subheader("New loading behavior")
    st.caption("The new update shows an app skeleton loading animation")
    st.markdown(
        f'<img src="data:image/gif;base64,{new_skeleton_url}" width=450 alt="demo gif">',
        unsafe_allow_html=True,
    )

st.divider()

# ## --------------------NEXT RELEASE v1.30------------------------------------------------ ##
# # Anchor Demo
# st.header("🔗 :red[Improved anchor button]")
# st.caption("Streamlit headers have anchors on the left side which overlaps other elements. This new change moves it to the right side of the header.")

# anchor = Image.open("/mount/src/release-demos/1.29/pages/anchor_img.png")
# # anchor = "pages/anchor_img.png"

# col1, col2 = st.columns(2)
# with col2:
#     st.subheader("Anchor on the left")
#     st.caption("Behavior before the update ⬇️")
#     st.image(anchor)
# with col1:
#     st.subheader("New and updated anchor on the right")
#     st.caption("Hover over the header to interact with the new changes ⬇️")
#     from datetime import datetime

#     with st.container():
#         st.header('Chart Timeframe Selection')
#         timeframe = st.radio(
#             "Select timeframe:",
#             ('All', 'Last 28 days', 'Quarter to date (QTD)', 'Year to date (YTD)')
#         )
#         start_date, end_date = st.date_input(
#             "Enter a date range",
#             value=(datetime(2019, 12, 1), datetime(2023, 7, 27)),
#             min_value=datetime(2000, 1, 1),
#             max_value=datetime.today()
#         )
