import streamlit as st
from datetime import datetime
import time
import venmoDriver as vd

"""
# Venmo Payment Scheduler

"""
st.subheader("Make sure all fields are correct before submitting!")
            
def main():
    print("Back to the top")
    container = st.empty()
    submitCont = st.empty()
    confirmCodeCont = st.empty()
    extraCont = st.empty()

    if "load_state" not in st.session_state:
        st.session_state["load_state"] = False

    with container.container():
        if not st.session_state["load_state"]:
            with st.form(key="inputs"):
                st.session_state["number"] = st.text_input('Enter the phone number associated with your Venmo account')
                st.session_state["password"] = st.text_input('Enter the password to your Venmo account. This information will be discarded as soon as your payment goes through.')
                st.session_state["recipient"] = st.text_input('Enter the recipient of your payment')
                st.session_state["payAmt"] = st.text_input('Enter in the payment amount in the form $XX.XX')
                st.session_state["comment"] = st.text_area('Enter in any comments you want to add to the payment. Leave blank if none.')
                st.session_state["selected_date"] = st.date_input("Enter in the date of transaction", datetime.now())
                st.session_state["selected_time"] = st.time_input("Enter in the time of the transaction -- You can enter in it manually if you want a more specific time", datetime.now().time())
                submit = st.form_submit_button("Submit")

    #here, pass in to login() in main.py with phone number and password

    if st.session_state["load_state"] or submit:
        container.empty()
        if "driver" not in st.session_state:
            with st.spinner('Please wait for a 6-digit SMS'):
                st.session_state["driver"] = vd.loginVenmo(st.session_state["number"], st.session_state["password"]) 
        #st.session_state["number"], st.session_state["password"]
        print("First if statement")
        st.session_state["load_state"] = True
        #st.session_state["load_state"] = True


        if "venmoCode" not in st.session_state:
            st.session_state["venmoCode"] = False

        if not st.session_state["venmoCode"]:
            with confirmCodeCont.container():
                with st.form(key="sms"):
                    st.session_state["code"] = st.text_input("Please enter in the 6-digit code from Venmo here")
                    submitCode = st.form_submit_button("Confirm")
                    print("Im here!!")
        
        print("submitCode: " + str(submitCode))

        if submitCode:
            print("POOP")
            st.session_state["venmoCode"] = True
        #if "load_state" not in st.session_state:
            #st.session_state["load_state"] = False
        print(st.session_state["venmoCode"])
        if st.session_state["venmoCode"] or submitCode:
            confirmCodeCont.empty()
            st.success("Thank you! Your payment has been scheduled!")
            vd.continuePayment(st.session_state["driver"], st.session_state["recipient"], st.session_state["code"], st.session_state["payAmt"], st.session_state["comment"])
            print(st.session_state["number"])
            time.sleep(5)


if __name__ == "__main__":
    main()
