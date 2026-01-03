import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_marks_model.pkl")

st.title("🎓 Student Marks Prediction")

st.write(
    "Upload a CSV file containing **attendance** and **hours_studied**.\n\n"
    "The app will show the **expected marks range**."
)

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Validate columns
    required_cols = {"attendance", "hours_studied"}
    if not required_cols.issubset(df.columns):
        st.error("CSV must contain columns: attendance, hours_studied")
    else:
        st.subheader("📄 Uploaded Data Preview")
        st.dataframe(df.head())

        if st.button("Predict Marks"):
            # Predict marks 
            predictions = model.predict(df[["attendance", "hours_studied"]])

            results = []

            for i, pred in enumerate(predictions):
                att = df.loc[i, "attendance"]
                hrs = df.loc[i, "hours_studied"]

                if att == 100 and hrs == 30:
                    results.append("100")
                elif att == 0 and hrs == 0:
                    results.append("0")
                else:
                    lower = max(0, int(pred - 5))
                    upper = min(100, int(pred + 5))
                    results.append(f"{lower} - {upper}")

            df["Expected Marks"] = results

            st.success("✅ Prediction Completed")
            st.subheader("📊 Prediction Results")
            st.dataframe(df)
