import streamlit as st
import numpy as np
import pickle as pkl
from PIL import Image

loaded_model = pkl.load(open("trained_model.sav", "rb"))

#creating a function for prediction

def strength_prediction(input_data):
    # # Taking input data
    # input_data = (540, 0.0, 0.0, 162.0, 2.5, 1040.0, 676.0, 28)

    # changing the input data into array
    input_data_in_array = np.asarray(input_data)

    # reshaping the data as we are predicting for one instance
    reshaped_input_data = input_data_in_array.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_input_data)
    print(prediction, "MPa")
    
    return prediction


def main():
    pic1 = Image.open("logo.jpeg")
    st.image(pic1, width = 200, channels="RGB")
    st.markdown("<h1 style='text-align: center; color: red;'>Compressive Strength Web App</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'><i>Calculate the Compressive Strength by Giving mix design as an input<i></h2>", unsafe_allow_html=True)
    pic = Image.open("con.jpg")
    st.sidebar.image(pic, caption="Just an Image of Concrete", width= 300,channels="RGB")
    
    # Getting the input data from the user
    age = st.sidebar.selectbox("Testing period (in days)", ("3","7", "14", "28"))
    cement = st.sidebar.slider("Cement Content (in Kg)", 300, 550)
    # cement = st.text_input("Cement Content")
    blastFurnace = st.text_input("BlastFurnance Content")
    flyAsh = st.text_input("FlyAsh Content")
    Water = st.text_input("Water Content")
    Plasticizer = st.text_input("Plasticizer Content")
    CourseAgg = st.text_input("CourseAgg Content")
    FineAgg = st.text_input("FineAgg Content")

    
    # Code for prediction
    result = ""
    
    #Creating a button for prediction
    if st.button("Calculate"):
        result = strength_prediction([cement,blastFurnace,flyAsh,Water,Plasticizer,CourseAgg,FineAgg,age])
     
    st.success(result)

    st.markdown("<h4 style = 'text_align:center; color:green;'><i>Quality concrete is our aim<i></h4>", unsafe_allow_html=True)
    st.markdown("<marquee behavior="scroll" direction="left">Thank you for visiting us!</marquee>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
