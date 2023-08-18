import streamlit as st
from datetime import datetime
import time

"""
# Venmo Payment Scheduler

"""
submit = False

            
def main():
    container = st.empty()
    submitCont = st.empty()
    confirmCodeCont = st.empty()

    with container.container():
        number = st.text_input('Enter the phone number associated with your Venmo account')
        password = st.text_input('Enter the password to your Venmo account. This information will be discarded as soon as your payment goes through.')
        recipient = st.text_input('Enter the recipient of your payment')
        payAmt = st.text_input('Enter in the payment amount in the form $XX.XX')
        comment = st.text_area('Enter in any comments you want to add to the payment. Leave blank if none.')
        selected_date = st.date_input("Enter in the date of transaction", datetime.now())
        selected_time = st.time_input("Enter in the time of the transaction -- You can enter in it manually if you want a more specific time", datetime.now().time())

    with submitCont.container():
        submit = st.button("Submit")

    if submit:
        container.empty()
        submitCont.empty()

        with st.spinner('Please wait for a 6-digit SMS'):
            time.sleep(5)
        
                
        with confirmCodeCont.container():
            code = st.text_input("Please enter in the 6-digit code from Venmo here")
            submitCode = st.button("Confirm")
    
        if submitCode:
            confirmCodeCont.empty()
            st.header("Thank you! Your payment has been scheduled!")
            

if __name__ == "__main__":
    main()
