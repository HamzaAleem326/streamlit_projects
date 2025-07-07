import streamlit as st
import time

st.set_page_config(page_title='BMI Calculator', page_icon='⚖️', layout='centered')

st.title('🏃‍♂️ BMI Calculator')
st.markdown('---')

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader('Metric Units')
    weight = st.number_input('Weight (kg)', min_value=0.1, max_value=500.0, value=70.0, step=0.1)
    height_cm = st.number_input('Height (cm)', min_value=1.0, max_value=300.0, value=170.0, step=0.1)

with col2:
    st.subheader('Imperial Units')
    weight_lbs = st.number_input('Weight (lbs)', min_value=0.1, max_value=1100.0, value=154.0, step=0.1)
    height_in = st.number_input('Height (inches)', min_value=1.0, max_value=120.0, value=67.0, step=0.1)

# Unit conversion toggle
unit_system = st.radio('Select unit system:', ['Metric (kg/cm)', 'Imperial (lbs/in)'])

# Calculate BMI
if st.button('Calculate BMI', type='primary'):
    bmi = None
    error = False

    if unit_system == 'Metric (kg/cm)':
        if weight <= 0 or height_cm <= 0:
            st.error('Please enter valid weight and height values!')
            error = True
        else:
            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)
    else:
        if weight_lbs <= 0 or height_in <= 0:
            st.error('Please enter valid weight and height values!')
            error = True
        else:
            bmi = (weight_lbs / (height_in ** 2)) * 703

    if not error:
        # Display result with animation
        with st.spinner('Calculating...'):
            time.sleep(1)

        st.success(f'Your BMI is: **{bmi:.2f}**')

        # BMI categories
        if bmi < 18.5:
            category = 'Underweight'
            color = 'blue'
            advice = 'Consider consulting a healthcare provider for guidance on healthy weight gain.'
        elif 18.5 <= bmi < 25:
            category = 'Normal weight'
            color = 'green'
            advice = 'Great! You have a healthy weight. Keep up the good work!'
        elif 25 <= bmi < 30:
            category = 'Overweight'
            color = 'orange'
            advice = 'Consider adopting a healthier diet and increasing physical activity.'
        else:
            category = 'Obese'
            color = 'red'
            advice = 'Consult a healthcare provider for personalized guidance.'

        # Display category with color
        st.markdown(f'**Category:** <span style="color:{color}">{category}</span>', unsafe_allow_html=True)
        st.info(advice)

        # BMI scale visualization
        st.subheader('BMI Scale:')
        st.markdown('''
        - **Underweight:** BMI < 18.5
        - **Normal weight:** BMI 18.5 - 24.9
        - **Overweight:** BMI 25 - 29.9
        - **Obese:** BMI ≥ 30
        ''')

        # Progress bar showing where user falls on the scale
        progress_value = min(bmi / 40, 1.0)
        st.progress(progress_value)

# Additional information
st.markdown('---')
st.markdown('''
**Note:** BMI is a screening tool and doesn't diagnose body fatness or health.
For health assessments, consult with a healthcare provider.
''')

# Footer
st.markdown('---')
st.markdown('*Made with ❤️ using Streamlit*')