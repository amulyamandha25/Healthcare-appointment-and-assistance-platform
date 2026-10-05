import streamlit as st


st.set_page_config(
    page_title="AI Healthcare Platform",
    page_icon="🏥",
    layout="wide"
)


# -----------------------------
# Initialize session data
# -----------------------------

if "patient" not in st.session_state:
    st.session_state.patient = None

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "doctors" not in st.session_state:

    st.session_state.doctors = [

        {
            "name": "Dr. Anjali Sharma",
            "specialization": "General Physician",
            "days": "Monday, Wednesday, Friday",
            "time": "10:00 AM - 2:00 PM"
        },

        {
            "name": "Dr. Rahul Kumar",
            "specialization": "Cardiologist",
            "days": "Tuesday, Thursday",
            "time": "10:00 AM - 1:00 PM"
        },

        {
            "name": "Dr. Priya Reddy",
            "specialization": "Dermatologist",
            "days": "Monday, Thursday, Saturday",
            "time": "11:00 AM - 3:00 PM"
        },

        {
            "name": "Dr. Arjun Rao",
            "specialization": "Neurologist",
            "days": "Wednesday, Friday",
            "time": "2:00 PM - 5:00 PM"
        },

        {
            "name": "Dr. Sneha Patel",
            "specialization": "Pediatrician",
            "days": "Monday, Tuesday, Friday",
            "time": "9:00 AM - 12:00 PM"
        }
    ]


# -----------------------------
# Home page
# -----------------------------

st.title(
    "🏥 AI Healthcare Appointment & Assistance Platform"
)

st.write(
    "Welcome to an AI-powered healthcare assistance "
    "and appointment platform."
)


st.divider()


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("🤖 AI Assistant")

    st.write(
        "Ask general healthcare questions "
        "using our local Ollama AI."
    )


with col2:

    st.subheader("👨‍⚕️ Doctors")

    st.write(
        "Explore doctors and their "
        "medical specializations."
    )


with col3:

    st.subheader("📅 Appointments")

    st.write(
        "Book and manage your appointments."
    )


st.divider()


if st.session_state.patient:

    patient = st.session_state.patient

    st.success(
        f"Welcome, {patient['name']}!"
    )

    st.write(
        f"Registered email: {patient['email']}"
    )

else:

    st.info(
        "Please register your patient profile "
        "from the sidebar before booking an appointment."
    )


st.warning(
    """
    ⚠️ Medical Safety Notice

    This is an academic prototype. The AI provides
    general healthcare information and does not
    diagnose diseases or replace a qualified healthcare professional.

    For a medical emergency, seek immediate professional medical care.
    """
)
