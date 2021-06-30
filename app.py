import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Utils
import os
import joblib 
import hashlib
# passlib,bcrypt

# Data Viz Pkgs
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

from PIL import Image

# DB
from managed_db import *
def generate_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()


# Password
def verify_hashes(password,hashed_text):
	if generate_hashes(password) == hashed_text:
		return hashed_text
	return False

feature_names_best = ['continuous_sneezing','shivering','chills','joint_pain','vomiting','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','cough','high_fever','sunken_eyes','breathlessness','sweating','headache','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','mild_fever','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','dizziness','obesity','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','movement_stiffness','loss_of_smell','depression','irritability','muscle_pain','abnormal_menstruation','watering_from_eyes','increased_appetite','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','history_of_alcohol_consumption','blood_in_sputum','palpitations','painful_walking','red_sore_around_nose']
feature_dict = {"No":0,"Yes":1}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value 

def get_key(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return key

def get_fvalue(val):
    feature_dict = {"No":0,"Yes":1}
    for key,value in feature_dict.items():
        if val == key:
            return value 

# Load ML Models
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

html_temp = """
        <div style="background-color:{};padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;font-style:verdana;">ASTHMA DETECTION </h1>
        </div>
        """
avatar1 ="https://www.shareicon.net/data/2016/07/26/801997_user_512x512.png"

result_temp ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
    <img src="https://www.shareicon.net/data/2016/07/26/801997_user_512x512.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
    <br/>
    <br/>   
    <p style="text-align:justify;color:white">{} % Prediction of future orders {}s</p>
    </div>
    """

result_temp2 ="""
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
    <h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
    <img src="https://www.shareicon.net/data/2016/07/26/801997_user_512x512.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
    <br/>
    <br/>   
    <p style="text-align:justify;color:white">{} % Prediction of future orders {}s</p>
    </div>
    """

prescriptive_message_temp ="""
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
        <h3 style="text-align:justify;color:black;padding:10px">RECOMMENDED WAREHOUSE GOODS MODIFICATION</h3>
        <ul>
        <li style="text-align:justify;color:black;padding:10px">Recession Period Ahead</li>
        <li style="text-align:justify;color:black;padding:10px">Stock up the warehouse only with the number of orders predicted</li>
        <li style="text-align:justify;color:black;padding:10px">Don't stock up much perishable goods as they might lead to a loss due to rotting</li>
        <li style="text-align:justify;color:black;padding:10px">If the warehouse is already stocked high, check the temperature controls to prevent rotting.</li>
        <li style="text-align:justify;color:black;padding:10px">Promote the food items through email for a larger reach and thus profit</li>
        <ul>
        <h3 style="text-align:justify;color:black;padding:10px">Plan on providing free home delivery as people have just overcome from a pandemic situation</h3>
        <ul>
        <li style="text-align:justify;color:black;padding:10px">Count the stocks today</li>
        <li style="text-align:justify;color:black;padding:10px">Stock as per predicted</li>
        <li style="text-align:justify;color:black;padding:10px">Lose Less and be rewarded with happy customers!!</li>
        <ul>
    </div>
    """
descriptive_message_temp ="""
    <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
        <h3 style="text-align:justify;color:black;padding:10px">Why Food Demand Forecasting?</h3>
        <p>The world has just recovered from a pandemic situation. If the demands of food items are less and stocks in the warehouse are more,it would lead to a loss. Also, higher demands and less warehouse stocks would lead to unhappy customer thus destroying the company's image. Hence, if the food demands in the future are predicted and perishable goods are stocked up as per upcoming predicted number of orders, the company would be at profit and customers shall be happy. Happy Food Demand Forecasting!!!</p>

    </div>
    """

@st.cache

def change_avatar():
    avatar_img = 'avatar.png'
    return avatar_img




def main():
    st.title("LET'S CHECK YOUR LUNGS!")
    st.markdown(html_temp.format('royalblue'),unsafe_allow_html=True)

    menu = ["Home","Login","SignUp"]
    submenu = ["Plot","Prediction"]
    

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.text("ASTHMA PREDICTION")
        st.markdown(descriptive_message_temp,unsafe_allow_html=True)
        
        im=Image.open('asthma1.png')
        st.image(im,caption='PERISHABLE FOOD ITEMS',use_column_width=True)
    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type='password')
        # av=Image.open('avatar.png')
        st.sidebar.markdown("![Alt Text](http://manabadi.co.in/Graphics/images/reguserEAM_icon.gif)")
        st.markdown("![Alt Text](https://s3-eu-west-1.amazonaws.com/rpf-futurelearn/programming-101-educators/Illustrations+and+animations/4.7-What-is-Abstraction.gif)")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = generate_hashes(password)
            result = login_user(username,verify_hashes(password,hashed_pswd))
            # if password == "12345":
            if result:
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity",submenu)
                if activity == "Plot":
                    st.subheader("Data Vis Plot")
                    df=pd.read_csv("data/Lungs_Training.csv")
                    st.dataframe(df.head(50))
                    st.bar_chart(df['num_orders'])

                    if st.checkbox("Area Chart"):
                        all_columns = df.columns.to_list()
                        feat_choices = st.multiselect("Choose a Feature",all_columns)
                        new_df = df[feat_choices].head(50)
                        st.area_chart(new_df)
                elif activity == "Prediction":
                    st.subheader("Predictive Analytics")
                    st.subheader("Do you have any of the following symptoms?")
                    continuous_sneezing = st.radio("CONTINUOUS SNEEZING",tuple(feature_dict.keys()))
                    shivering = st.radio("SHIVERING",tuple(feature_dict.keys()))
                    chills = st.radio("CHILLS",tuple(feature_dict.keys()))
                    joint_pain = st.radio("JOINT PAIN",tuple(feature_dict.keys()))
                    vomiting = st.radio("VOMITING",tuple(feature_dict.keys()))
                    fatigue = st.radio("FATIGUE",tuple(feature_dict.keys()))
                    weight_gain = st.radio("WEIGHT GAIN",tuple(feature_dict.keys()))
                    weight_loss = st.radio("WEIGHT LOSS",tuple(feature_dict.keys()))
                    anxiety = st.radio("ANXIETY",tuple(feature_dict.keys()))
                    cool_hands_and_feets = st.radio("COOL HANDS AND FEET",tuple(feature_dict.keys()))
                    mood_swings = st.radio("MOOD SWINGS",tuple(feature_dict.keys()))
                    restlessness = st.radio("RESTLESSNESS",tuple(feature_dict.keys()))
                    lethargy = st.radio("LETHARGY",tuple(feature_dict.keys()))
                    patches_in_throat = st.radio("PATCHES IN THROAT",tuple(feature_dict.keys()))
                    high_fever = st.radio("HIGH FEVER",tuple(feature_dict.keys()))
                    sunken_eyes = st.radio("SUNKEN EYES",tuple(feature_dict.keys()))
                    breathlessness = st.radio("BREATHLESSNESS",tuple(feature_dict.keys()))
                    sweating = st.radio("SWEATING",tuple(feature_dict.keys()))
                    headache = st.radio("HEADACHE",tuple(feature_dict.keys()))
                    nausea= st.radio("NAUSEA",tuple(feature_dict.keys()))
                    loss_of_appetite= st.radio("LOSS OF APETITE",tuple(feature_dict.keys()))
                    pain_behind_the_eyes= st.radio("PAIN BEHIND THE EYES",tuple(feature_dict.keys()))
                    back_pain= st.radio("BACK PAIN",tuple(feature_dict.keys()))
                    mild_fever= st.radio("MILD FEVER",tuple(feature_dict.keys()))
                    malaise= st.radio("MALAISE",tuple(feature_dict.keys()))
                    blurred_and_distorted_vision= st.radio("BLURRED AND DISTORTED VISION",tuple(feature_dict.keys()))
                    phlegm= st.radio("PHLEGM",tuple(feature_dict.keys()))
                    throat_irritation= st.radio("THROAT IRRITATION",tuple(feature_dict.keys()))
                    redness_of_eyes= st.radio("REDNESS OF EYES",tuple(feature_dict.keys()))
                    sinus_pressure= st.radio("SINUS PRESSURE",tuple(feature_dict.keys()))
                    runny_nose= st.radio("RUNNY NOSE",tuple(feature_dict.keys()))                    
                    congestion= st.radio("CONGESTION",tuple(feature_dict.keys()))
                    chest_pain= st.radio("CHEST PAIN",tuple(feature_dict.keys()))
                    weakness_in_limbs= st.radio("WEAKNESS IN LIMBS",tuple(feature_dict.keys()))
                    fast_heart_rate= st.radio("FAST HEART RATE",tuple(feature_dict.keys()))
                    dizziness= st.radio("DIZZINESS",tuple(feature_dict.keys()))
                    obesity= st.radio("OBESITY",tuple(feature_dict.keys()))
                    drying_and_tingling_lips= st.radio("DRYING AND TINGLING LIPS",tuple(feature_dict.keys()))
                    slurred_speech= st.radio("SLURRED SPEECH",tuple(feature_dict.keys()))
                    knee_pain = st.radio("KNEE PAIN",tuple(feature_dict.keys()))
                    hip_joint_pain = st.radio("HIP JOINT_PAIN",tuple(feature_dict.keys()))
                    muscle_weakness = st.radio("MUSCLE WEAKNESS",tuple(feature_dict.keys()))
                    movement_stiffness= st.radio("MOVEMENT STIFFNESS",tuple(feature_dict.keys()))
                    loss_of_smell = st.radio("LOSS OF SMELL",tuple(feature_dict.keys()))
                    depression = st.radio("DEPRESSION",tuple(feature_dict.keys()))
                    irritability = st.radio("IRRITABILITY",tuple(feature_dict.keys()))
                    muscle_pain = st.radio("MUSCLE PAIN",tuple(feature_dict.keys()))
                    abnormal_menstruation = st.radio("ABNORMAL MENSTRUATION",tuple(feature_dict.keys()))
                    watering_from_eyes = st.radio("WATERING FROM EYES",tuple(feature_dict.keys()))
                    increased_appetite = st.radio("INCREASED APPETITE",tuple(feature_dict.keys()))
                    family_history = st.radio("FAMILY HISTORY",tuple(feature_dict.keys()))
                    mucoid_sputum = st.radio("MUCOID SPUTUM",tuple(feature_dict.keys()))
                    rusty_sputum = st.radio("RUSTY SPUTUM",tuple(feature_dict.keys()))
                    blood_in_sputum = st.radio("BLOOD IN SPUTUM",tuple(feature_dict.keys()))
                    palpitations = st.radio("PALPITATIONS",tuple(feature_dict.keys()))
                    painful_walking = st.radio("PAINFUL WALKING",tuple(feature_dict.keys()))
                    red_sore_around_nose = st.radio("RED SORE AROUND NOSE",tuple(feature_dict.keys()))
                    feature_list = [get_fvalue('continuous_sneezing'),get_fvalue('shivering'),get_fvalue('chills'),get_fvalue('joint pain'),get_fvalue('vomiting'),get_fvalue('fatigue'),get_fvalue('weight_gain'),get_fvalue('anxiety'),get_fvalue('cold_hands_and_feets'),get_fvalue('mood_swings'),get_fvalue('weight_loss'),get_fvalue('restlessness'),get_fvalue('lethargy'),get_fvalue('patches_in_throat'),get_fvalue('cough'),get_fvalue('high_fever'),get_fvalue('sunken_eyes'),get_fvalue('breathlessness'),get_fvalue('sweating'),get_fvalue('headache'),get_fvalue('nausea'),get_fvalue('loss_of_appetite'),get_fvalue('pain_behind_the_eyes'),get_fvalue('back_pain'),get_fvalue('mild_fever'),get_fvalue('malaise'),get_fvalue('blurred_and_distorted_vision'),get_fvalue('phlegm'),get_fvalue('throat_irritation'),get_fvalue('redness_of_eyes'),get_fvalue('sinus_pressure'),get_fvalue('runny_nose'),get_fvalue('congestion'),get_fvalue('chest_pain'),get_fvalue('weakness_in_limbs'),get_fvalue('fast_heart_rate'),get_fvalue('dizziness'),get_fvalue('obesity'),get_fvalue('drying_and_tingling_lips'),get_fvalue('slurred_speech'),get_fvalue('knee_pain'),get_fvalue('hip_joint_pain'),get_fvalue('muscle_weakness'),get_fvalue('movement_stiffness'),get_fvalue('loss_of_smell'),get_fvalue('depression'),get_fvalue('irritability'),get_fvalue('muscle_pain'),get_fvalue('abnormal_menstruation'),get_fvalue('watering_from_eyes'),get_fvalue('increased_appetite'),get_fvalue('family_history'),get_fvalue('mucoid_sputum'),get_fvalue('rusty_sputum'),get_fvalue('lack_of_concentration'),get_fvalue('history_of_alcohol_consumption'),get_fvalue('blood_in_sputum'),get_fvalue('palpitations'),get_fvalue('painful_walking'),get_fvalue('red_sore_around_nose')]
                    st.write(len(feature_list))
                    st.write(feature_list)
                    
                    single_sample = np.array(feature_list).reshape(1,-1)
                    model_choice = st.selectbox("Select Model",["MLP Classifier","Decision Tree Classifier","Random Forest Classifier"])
                    if st.button("Predict"):
                    	st.subheader("YOU PROBABLY HAVE:")
                    	if model_choice == "MLP Classifier":
                    		loaded_model = load_model("models/MLP_Classifier_model.pkl")
                    		prediction = loaded_model.predict(single_sample)
                    	elif model_choice == "Decision Tree Classifier":
                    		loaded_model = load_model("models/DT_Classifier_model.pkl")
                    		prediction = loaded_model.predict(single_sample)
                    	else:
                    		loaded_model = load_model("models/RF_Classifier_model.pkl")
                    		prediction = loaded_model.predict(single_sample)
                    	st.write(prediction.round(0))
                    	st.bar_chart(prediction)
                    	if(prediction>=350):
                    		st.success("THERE SHALL BE A SURGE IN THE NUMBER OF ORDERS IN THE NEAR FUTURE!")
                    		st.success(" STOCK UP EARLY TO FULFIL ALL THE CUSTOMER DEMANDS")
                    		st.balloons()
                    	else:
                    		st.warning("THERE SHALL BE A DROP IN THE NUMBER OF ORDERS IN THE NEAR FUTURE")
                    		st.warning(" DO NOT STOCK UP MUCH AS IT WOULD LEAD TO A LOSS")
                    		st.subheader("Follow the steps to prevent loss:")
                    		st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
    elif choice == "SignUp":
    	new_username = st.text_input("User name")
    	new_password = st.text_input("Password", type='password')
    	confirm_password = st.text_input("Confirm Password",type='password')
    	if new_password == confirm_password:
    		st.success("Password Confirmed")
    	else:
    		st.warning("Passwords not the same")
    		if st.button("Submit"):
    			create_usertable()
    			hashed_new_password = generate_hashes(new_password)
    			add_userdata(new_username,hashed_new_password)
    			st.success("You have successfully created a new account")
    			st.info("Login to Get Started")


    





if __name__ == '__main__':
    main()