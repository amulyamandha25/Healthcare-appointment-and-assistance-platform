import streamlit as st


st.set_page_config(
    page_title="Patient Profile",
    page_icon="👤"
)


st.title("👤 Patient Profile")

st.write(
    "Enter your basic information to create your patient profile."
)


# Patient registration form
with st.form("patient_profile_form"):

    name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "Email Address",
        placeholder="example@gmail.com"
    )

    phone = st.text_input(
        "Phone Number",
        placeholder="Enter your phone number"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=18
    )

    gender = st.selectbox(
        "Gender",
        [
            "Prefer not to say",
            "Male",
            "Female",
            "Other"
        ]
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "Prefer not to say",
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    submit = st.form_submit_button(
        "💾 Save Profile"
    )


# Save profile
if submit:

    if not name.strip():

        st.error("Please enter your name.")

    elif not email.strip():

        st.error("Please enter your email address.")

    elif not phone.strip():

        st.error("Please enter your phone number.")

    else:

        st.session_state.patient = {

            "name": name,

            "email": email,

            "phone": phone,

            "age": age,

            "gender": gender,

            "blood_group": blood_group
        }

        st.success(
            "✅ Patient profile saved successfully!"
        )


# Display saved profile
if "patient" in st.session_state:

    if st.session_state.patient:

        st.divider()

        st.subheader("📋 Your Profile")

        patient = st.session_state.patient

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Name:** {patient['name']}"
            )

            st.write(
                f"**Email:** {patient['email']}"
            )

            st.write(
                f"**Phone:** {patient['phone']}"
            )

        with col2:

            st.write(
                f"**Age:** {patient['age']}"
            )

            st.write(
                f"**Gender:** {patient['gender']}"
            )

            st.write(
                f"**Blood Group:** {patient['blood_group']}"
            )

        st.success(
            "Your profile is ready for appointment booking."
        )
