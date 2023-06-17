import streamlit as st
import numpy as np
import pickle as pkl

loaded_model = pkl.load(open(r"C:\Users\Manoj Gaikwad\MG\trained_model.sav", "rb"))

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
    
    # Giving a title
    st.title("Compressive Strength Web App")
    
    # Getting the input data from the user
   
    cement = st.text_input("Cement Content")
    blastFurnace = st.text_input("BlastFurnance Content")
    flyAsh = st.text_input("FlyAsh Content")
    Water = st.text_input("Water Content")
    Plasticizer = st.text_input("Plasticizer Content")
    CourseAgg = st.text_input("CourseAgg Content")
    FineAgg = st.text_input("FineAgg Content")
    Age = st.text_input("Testing period")
    
    # Code for prediction
    result = ""
    
    #Creating a button for prediction
    if st.button("Calculate"):
        result = strength_prediction([cement,blastFurnace,flyAsh,Water,Plasticizer,CourseAgg,FineAgg,Age])
     
    st.success(result)
    
    
if __name__ == "__main__":
    main()