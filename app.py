import streamlit as st
import pandas as pd
from src.DiamondPricePrediction.pipelines.Prediction_Pipeline import CustomData, PredictPipeline

# Set the title of the web app
st.title('Diamond Price Prediction')

# Create input fields for the diamond features
carat = st.number_input('Carat', min_value=0.0, format="%.2f")
depth = st.number_input('Depth', min_value=0.0, format="%.2f")
table = st.number_input('Table', min_value=0.0, format="%.2f")
x = st.number_input('X', min_value=0.0, format="%.2f")
y = st.number_input('Y', min_value=0.0, format="%.2f")
z = st.number_input('Z', min_value=0.0, format="%.2f")
cut = st.selectbox('Cut', options=['', 'Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color', options=['', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', options=['', 'I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

# Button to make predictions
if st.button('Predict Price'):
    if cut and color and clarity:
        # Create the CustomData object with the input values
        data = CustomData(carat, depth, table, x, y, z, cut, color, clarity)

        # Convert the data into a DataFrame for the prediction pipeline
        final_data = data.get_data_as_dataframe()

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()

        # Make prediction
        prediction = predict_pipeline.predict(final_data)

        # Display the result
        result = round(prediction[0], 2)
        st.success(f'Predicted Diamond Price: ${result}')
    else:
        st.error('Please fill all the fields')

# Run this with 'streamlit run app.py' in your command line
