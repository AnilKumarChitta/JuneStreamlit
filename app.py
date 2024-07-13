import streamlit as st

st.title('Uber pickups in NYC')
st.header('This is a header with a divider', divider='rainbow')

st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

# Checkbox demo
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")


# Radio button demo to select Genre
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")


# Radio button to select male or female
status = st.radio("Select Gender: ", ('Male','Female'))
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

# Button demo
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

# Square function
def square(num):
    return num*num

number = st.number_input("Insert a number")

if(st.button("Calculate Square")):
    res = square(number)
    st.write("The current number is ", res)
