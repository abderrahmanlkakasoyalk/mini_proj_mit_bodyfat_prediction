import streamlit as st
import pickle

def predict_body_fat(model_name, features):
    # Load the selected model
    with open(f'{model_name}.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # Make predictions
    prediction = model.predict([features])
    return prediction[0]

def main():
    st.title("Body Fat Percentage Prediction")

    # Input fields for user to enter features
    age = st.number_input('Age', value=30, step=1)
    weight = st.number_input('Weight (kg)', value=70.0, step=0.1)
    height = st.number_input('Height (m)', value=1.70, step=0.01)
    neck = st.number_input('Neck circumference (cm)', value=40.0, step=0.1)
    chest = st.number_input('Chest circumference (cm)', value=90.0, step=0.1)
    abdomen = st.number_input('Abdomen circumference (cm)', value=80.0, step=0.1)
    hip = st.number_input('Hip circumference (cm)', value=90.0, step=0.1)
    thigh = st.number_input('Thigh circumference (cm)', value=50.0, step=0.1)
    knee = st.number_input('Knee circumference (cm)', value=35.0, step=0.1)
    biceps = st.number_input('Biceps circumference (cm)', value=30.0, step=0.1)

    # Dropdown to select model
    model_name = st.selectbox("Select Model", ["linear_regression_model", "lasso_regression_model", "ridge_regression_model", "random_forest_regression_model", "svm_regression_model"])

    if st.button('Predict'):
        features = [age, weight, height, neck, chest, abdomen, hip, thigh, knee, biceps]
        prediction = predict_body_fat(model_name, features)
        st.success(f"Predicted Body Fat Percentage: {prediction:.2f}%")

if __name__ == '__main__':
    main()
