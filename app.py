import streamlit as st

st.set_page_config(
page_title="Office Wi-Fi Security Assessment",
page_icon="🔐",
layout="wide"
)

st.title("🔐 Office Wi-Fi Security Assessment")

st.write(
"A demonstration dashboard for assessing "
"wireless network security configurations."
)

st.info(
"Demo mode: These are simulated results, "
"not findings from a real office network."
)

st.sidebar.header("Assessment Settings")

network_name = st.sidebar.text_input(
"Office Network Name",
value="Office Wi-Fi"
)

security_type = st.sidebar.selectbox(
"Encryption",
["WPA3", "WPA2-AES", "WEP", "Open Network"]
)

password_policy = st.sidebar.selectbox(
"Password Policy",
["Strong password", "Weak password", "Unknown"]
)

st.subheader("Assessment Summary")

col1, col2, col3 = st.columns(3)

with col1:
st.metric("Network", network_name)

with col2:
st.metric("Encryption", security_type)

with col3:
st.metric("Password Policy", password_policy)

st.subheader("Demo Findings")

if security_type == "WPA3":
st.success(
"WPA3 selected: generally strong encryption."
)
elif security_type == "WPA2-AES":
st.info(
"WPA2-AES selected: review configuration and updates."
)
else:
st.warning(
"Potential security concern: investigate this configuration."
)

if password_policy == "Weak password":
st.warning(
"Recommendation: use a long, unique Wi-Fi password."
)
elif password_policy == "Unknown":
st.info(
"Recommendation: verify the password policy."
)

st.subheader("Recommended Security Practices")

st.markdown(
"- Use WPA3 or properly configured WPA2-AES.\n"
"- Disable WPS where appropriate.\n"
"- Change default router administrator credentials.\n"
"- Update router firmware.\n"
"- Use a guest network for visitors.\n"
"- Review connected devices regularly."
)

st.caption(
"Educational capstone demonstration. "
"No real network scanning is performed."
)