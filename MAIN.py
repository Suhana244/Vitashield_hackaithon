import streamlit as st 

st.set_page_config(
    page_title="VITASHIELD APP"
)
st.title("MAIN PAGE")
menu = ["HOME","GOALS"]
choice = st.sidebar.selectbox("menu",menu)
st.sidebar.success("select a page above.")

if choice == "HOME":
    st.subheader("Please enter your details")
    with st.form(key='forml'):
      firstname = st.text_input("First name")
      lastname = st.text_input("Last name")
      dob = st.date_input("Date of Birth")

      submit_button = st.form_submit_button(label='submit')

      if submit_button:
                        st.success("hello {} you have submitted your details")
#if "my_input" not in st.session_state:
 #   st.session_state["my_input"] = ""

#my_input = st.text_input("Input your name  ",st.session_state["my_input"])

#submit = st.button("submit")
#if submit:
#    st.session_state["my_input"] = my_input
 #   st.write("you have entered:", my_input)
 
        
      