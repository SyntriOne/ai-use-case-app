
import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="Silent Edge Architect", layout="centered")

# Load OpenAI key securely
openai.api_key = st.secrets["openai_key"]

# App header
st.title("🧠 Silent Edge Architect")
st.subheader("AI Strategy Engine for Businesses")
st.markdown("Enter a short description of a business and a challenge they’re facing, and get detailed AI use cases, tools, and implementation insights.")

# Input form
with st.form("ai_discovery_form"):
    business_description = st.text_area("Describe the business and their pain point(s):", height=150,
                                        placeholder="Example: A real estate agent who spends too much time on paperwork and manual follow-ups.")
    submitted = st.form_submit_button("Generate AI Use Cases")

# If form is submitted
if submitted and business_description.strip():
    with st.spinner("Analyzing your business challenge and finding AI solutions..."):

        prompt = f"""You are an expert AI business consultant. A user has described the following business and challenge:

        {business_description}

        Your job is to:
        1. Identify the business type and summarize the core problem.
        2. Recommend 2–4 AI-powered use cases to solve it.
        3. For each, provide:
           - A named AI tool or platform
           - A short description of how it works
           - The business impact or benefit (e.g. saves time, increases sales)
        4. Format the output clearly and professionally.

        Only return the structured report. Do not mention that you are an AI.

        Now generate the AI strategy."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800
            )
            reply = response["choices"][0]["message"]["content"]
            st.markdown("### 🧩 AI Strategy Report")
            st.markdown(reply)

            # Option to copy to clipboard
            st.download_button("📄 Download Report as Text", reply, file_name="ai_strategy_report.txt")

        except Exception as e:
            st.error(f"Error: {e}")
