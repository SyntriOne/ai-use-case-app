
import streamlit as st
import pandas as pd

def recommend_ai_tools(business_type, pain_point):
    recommendations = []

    if business_type.lower() == "retail":
        if "support" in pain_point.lower():
            recommendations.append(("ChatGPT-powered chatbot", "For answering FAQs on your site 24/7"))
            recommendations.append(("Tidio or Intercom", "To automate and track customer messages"))
        if "inventory" in pain_point.lower():
            recommendations.append(("Google Sheets + AI plugin", "For stock forecasting and order tracking"))
            recommendations.append(("Zapier", "To automate inventory reorder alerts"))

    if business_type.lower() == "service":
        if "appointments" in pain_point.lower():
            recommendations.append(("Calendly + AI assistant", "To auto-schedule meetings with clients"))
            recommendations.append(("Zapier", "To automate follow-ups after bookings"))
        if "emails" in pain_point.lower():
            recommendations.append(("Lavender AI", "To generate and optimize client emails"))
            recommendations.append(("ChatGPT", "To help respond to common questions"))

    if business_type.lower() == "professional":
        if "documents" in pain_point.lower():
            recommendations.append(("Docparser", "To extract data from PDFs and forms"))
            recommendations.append(("Otter.ai", "To transcribe client meetings or calls"))
        if "reporting" in pain_point.lower():
            recommendations.append(("Power BI or Google Looker Studio", "To build automated dashboards"))

    if not recommendations:
        recommendations.append(("ChatGPT", "To help draft content or answer business questions"))
        recommendations.append(("Zapier", "To automate workflows between your apps"))

    return pd.DataFrame(recommendations, columns=["Recommended Tool", "Why It Helps"])

st.title("🔍 AI Use Case Recommender for Small Businesses")

st.write("Answer two quick questions to get instant AI tool suggestions tailored to your business.")

business_type = st.selectbox("What type of business are you helping?", ["", "Retail", "Service", "Professional"])
pain_point = st.text_input("What's the biggest challenge they’re facing? (e.g., customer support, scheduling, reporting)")

if st.button("Get Recommendations") and business_type:
    results = recommend_ai_tools(business_type, pain_point)
    st.write("### Recommended AI Tools and Why They Help:")
    st.dataframe(results)
