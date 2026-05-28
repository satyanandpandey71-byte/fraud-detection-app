# import streamlit as st  
# import pandas as pd 
# import joblib   

# model = joblib.load("fraud_detection_model.pkl")

# st.title("Fraud Detection App")

# st.markdown("Please enter the transaction details and use the predict button.")
# st.divider()

# transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT","CASH_IN", "DEPOSIT"])
# amount = st.number_input("Amount", min_value=0.0, value = 1000.0)
# old_balance = st.number_input("Old Balance, (Sender)", min_value=0.0, value = 10000.0)
# new_balance = st.number_input("New Balance, (Sender)", min_value=0.0, value = 9000.0)
# old_balance_dest = st.number_input("Old Balance, (Receiver)", min_value=0.0, value = 0.0)
# new_balance_dest = st.number_input("New Balance, (Receiver)", min_value=0.0, value = 0.0) 

# if st.button("Predict"):
#     input_data = pd.DataFrame([{
#         "type": transaction_type,
#         "amount": amount,
#         "oldbalanceOrg": old_balance,
#         "newbalanceOrig": new_balance,
#         "oldbalanceDest": old_balance_dest,
#         "newbalanceDest": new_balance_dest
#     }])
    
#     prediction = model.predict(input_data)[0]

#     st.subheader(f"Prediction : '{int(prediction)}'")

#     if prediction == 1:
#         st.error("This transaction can be fraud.")

#     else:
#         st.success("This transaction is not fraud.")    
    
    
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Fraud Detection App",
    page_icon="🔍",
    layout="centered"
)

st.markdown("""
    <style>
    .stSelectbox label, .stNumberInput label { font-size: 13px !important; color: #888 !important; font-weight: 500; }
    .block-container { max-width: 700px; padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

model = joblib.load("fraud_detection_model.pkl")

col_icon, col_title = st.columns([1, 8])
with col_icon:
    st.markdown("## 🔍")
with col_title:
    st.markdown("## Fraud Detection App")
    st.caption("AI-powered transaction risk analysis")

st.divider()

m1, m2, m3 = st.columns(3)
m1.metric("Transactions Trained", "6.3M+")
m2.metric("Model Accuracy", "99.8%")
m3.metric("Transaction Types", "5")

st.divider()

st.markdown("#### Transaction Details")

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEPOSIT"],
    help="Select the type of financial transaction"
)

amount = st.number_input(
    "Amount (₹)",
    min_value=0.0,
    value=1000.0,
    step=100.0,
    help="Enter transaction amount"
)

st.markdown("**Sender Balance**")
col1, col2 = st.columns(2)
with col1:
    old_balance = st.number_input("Old Balance", min_value=0.0, value=10000.0, step=500.0, key="old_bal")
with col2:
    new_balance = st.number_input("New Balance", min_value=0.0, value=9000.0, step=500.0, key="new_bal")

st.markdown("**Receiver Balance**")
col3, col4 = st.columns(2)
with col3:
    old_balance_dest = st.number_input("Old Balance", min_value=0.0, value=0.0, step=500.0, key="old_dest")
with col4:
    new_balance_dest = st.number_input("New Balance", min_value=0.0, value=0.0, step=500.0, key="new_dest")

st.markdown("")

if st.button("🧠 Predict Transaction", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": old_balance,
        "newbalanceOrig": new_balance,
        "oldbalanceDest": old_balance_dest,
        "newbalanceDest": new_balance_dest
    }])

    with st.spinner("Analyzing transaction..."):
        prediction = model.predict(input_data)[0]

    st.divider()

    if prediction == 1:
        st.error(f"### ⚠️ Fraud Detected — Prediction: {int(prediction)}")
        st.markdown("This transaction shows **suspicious patterns**. Please verify before proceeding.")
    else:
        st.success(f"### ✅ Transaction is Safe — Prediction: {int(prediction)}")
        st.markdown("No fraudulent patterns detected. This transaction appears **legitimate**.")

    with st.expander("View Input Summary"):
        st.dataframe(input_data, use_container_width=True)