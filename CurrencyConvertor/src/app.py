import streamlit as st
from utils import get_currencies
from main import convert_currency
from get_data import get_data


def c1_to_c2() :
    with st.spinner() :
        converted_value = convert_currency(
            st.session_state.currency1, st.session_state.v1, st.session_state.currency2, get_data()
        )
        st.session_state.v2 = converted_value

def c2_to_c1() :
    with st.spinner() :
        converted_value = convert_currency(
            st.session_state.currency2, st.session_state.v2, st.session_state.currency1, get_data()
        )
        st.session_state.v1 = converted_value


st.title("Currency Convertor 💰")

col1, col2, col3 = st.columns([1, 2, 4])

currency1 = col1.selectbox("currency", get_currencies(), key="currency1")
currency2 = col1.selectbox("currency2", get_currencies(), key="currency2", label_visibility="hidden")

col2.number_input(
    f"{currency1}",
    key="v1",
    on_change=c1_to_c2,
)

col2.number_input(
    f"{currency2}",
    key="v2",
    on_change=c2_to_c1,
)