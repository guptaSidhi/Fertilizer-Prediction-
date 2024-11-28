import pickle
import streamlit as st

# Load the pickled model
pickled_model = pickle.load(open('model.pkl', 'rb'))

# Define soil and crop options
soil_options = {
    'Loamy': 2,
    'Sandy': 4,
    'Clayey': 1,
    'Black': 0,
    'Red': 3
}

crop_options = {
    'Sugarcane': 8,
    'Cotton': 1,
    'Millets': 4,
    'Paddy': 6,
    'Pulses': 7,
    'Wheat': 10,
    'Tobacco': 9,
    'Barley': 0,
    'Oil seeds': 5,
    'Ground Nuts': 2,
    'Other': 3
}

def main():
    st.set_page_config(page_title="HarvestIQ - Fertilizer Prediction", page_icon=":farm:", layout="wide")
    
    # Header with image and title
    st.image("fertz.jpg", width=1000)  # Image fixed width
    # st.title("SMART FERTILIZER RECOMMENDATIONS")
    st.markdown("<h1 style='text-align: center; color: white;'>SMART FERTILIZER RECOMMENDATIONS</h1>", unsafe_allow_html=True)

    # Create sidebar options
    st.sidebar.header('HarvestIQ')

    # Taking direct inputs for parameters (no step for sliders)
    mois = st.sidebar.number_input("Moisture (%)", min_value=0, max_value=100, value=50)
    nitrogen = st.sidebar.number_input("Nitrogen Content in Soil (ppm)", min_value=0, max_value=200, value=100)
    potassium = st.sidebar.number_input("Potassium Content in Soil (ppm)", min_value=0, max_value=200, value=100)
    phosphorous = st.sidebar.number_input("Phosphorous Content in Soil (ppm)", min_value=0, max_value=200, value=100)

    soil_type = st.sidebar.selectbox(
        "Select Soil Type",
        list(soil_options.keys())
    )

    crop_type = st.sidebar.selectbox(
        "Select Crop Type",
        list(crop_options.keys())
    )

    # Get the soil and crop parameters
    soil_param = soil_options[soil_type]
    crop_param = crop_options[crop_type]

    inputs = [[mois, soil_param, crop_param, nitrogen, potassium, phosphorous]]

    if st.sidebar.button("Predict"):
        prediction = pickled_model.predict(inputs)

        # Map the predicted value to a fertilizer type
        fertilizer_types = {
            0: "UREA",
            1: "DAP",
            2: "GROMOR 28-28",
            3: "GROMOR 14-35-14",
            4: "GROMOR 20-20",
            5: "GROMOR 17-17-17",
            6: "GROMOR 10-26-26",
        }

        result = fertilizer_types[prediction[0]]

        # Display the output
        st.header('Output')
        st.success(f"The recommended fertilizer for your crops is: {result}")

if __name__ == '__main__':
    main()
