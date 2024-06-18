# this is the code for keshav.py file!!

import streamlit as st


# Pre-defined mapping of emotions to ragas
raga_mapping = {
    "Happy": "Raga Bhairavi",
    "Sad": "Raga Yaman",
    "Angry": "Raga Bhimpalasi",
    "Surprise": "Raga Darbari",
    "Fear": "Raga Malkauns",
    "Love": "Raga Kafi"
}

# Function to predict emotion based on input text
def predict_emotion(input_text):
    # Example: Perform prediction based on your model
    # Here, we are assuming a pre-defined prediction for demonstration
    # Check for specific keywords related to each emotion in the input text
    if any(word in input_text for word in ["खुश", "आनंद", "खुशी", "मुस्कान", "हंसी", "उल्लास", "प्रसन्नता", "खुशियाँ", "हर्ष", "आचरण"]):
        predicted_emotion = "Happy"
    elif any(word in input_text for word in [ "दुःख", "दुःखी", "दु:ख", "आंसू", "रोना", "उदास", "विचलित", "व्यथित", "दु:खी", "दर्द", "दुःखद"]):
        predicted_emotion = "Sad"
    elif any(word in input_text for word in ["गुस्सा", "नाराज", "क्रोध", "खींचाव", "रोष", "क्रोधित", "क्रोधी", "अभिमान", "कोप", "आवेग"]):
        predicted_emotion = "Angry"
    elif any(word in input_text for word in ["अचंभित", "आश्चर्य", "हैरान", "अच्छा", "अद्भुत", "आश्चर्यजनक", "अविश्वसनीय", "विस्मित", "अचरज"]):
        predicted_emotion = "Surprise"
    elif any(word in input_text for word in [ "डर", "भय", "खौफ", "भीति", "दहशत", "डराना", "आतंक", "भयभीत", "चिंता", "भ्रम"]):
        predicted_emotion = "Fear"
    elif any(word in input_text for word in [ "प्यार", "मोहब्बत", "इश्क", "प्रेम", "आदर", "प्रेमपूर्ण", "लव", "भावना", "अभिमान", "ममता"]):
        predicted_emotion = "Love"
    else:
        predicted_emotion = "Unknown"  # Default prediction
    return predicted_emotion

# Streamlit app
def main():
    st.title("Emotion and Raga Recommender")

    # Get input text from the user
    input_text = st.text_input("Enter your text in Hindi:")

    # Check if input text is provided
    if input_text:
        # Predict emotion based on input text
        predicted_emotion = predict_emotion(input_text)

        # Get recommended raga based on predicted emotion
        recommended_raga = raga_mapping.get(predicted_emotion, "Unknown")

        # Display predicted emotion and recommended raga
        st.write(f"Predicted Emotion: {predicted_emotion}")
        st.write(f"Recommended Raga: {recommended_raga}")

if __name__ == "__main__":
    main()
