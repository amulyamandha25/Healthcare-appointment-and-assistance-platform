import streamlit as st

from datetime import date


st.set_page_config(
    page_title="Appointments",
    page_icon="📅"
)


st.title("📅 Book an Appointment")


st.write(
    "Schedule an appointment with a healthcare professional."
)


# ------------------------------------------------
# Check whether patient profile exists
# ------------------------------------------------

if "patient" not in st.session_state:

    st.warning(
        "⚠️ Please create your Patient Profile first."
    )

    st.stop()


if st.session_state.patient is None:

    st.warning(
        "⚠️ Please create your Patient Profile first."
    )

    st.stop()


patient = st.session_state.patient


# ------------------------------------------------
# Patient information
# ------------------------------------------------

st.success(
    f"Booking appointment for: {patient['name']}"
)


st.divider()


# ------------------------------------------------
# Doctor list
# ------------------------------------------------

doctors = [

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
    },

    {
        "name": "Dr. Vikram Singh",
        "specialization": "Orthopedic",
        "days": "Tuesday, Friday, Saturday",
        "time": "10:00 AM - 3:00 PM"
    }
]


# ------------------------------------------------
# Doctor selection
# ------------------------------------------------

doctor_names = []

for doctor in doctors:

    doctor_names.append(
        f"{doctor['name']} - "
        f"{doctor['specialization']}"
    )


selected_doctor_name = st.selectbox(
    "👨‍⚕️ Select Doctor",
    doctor_names
)


# Find selected doctor

selected_doctor = None


for doctor in doctors:

    if (
        f"{doctor['name']} - "
        f"{doctor['specialization']}"
        == selected_doctor_name
    ):

        selected_doctor = doctor

        break


# ------------------------------------------------
# Show doctor availability
# ------------------------------------------------

if selected_doctor:

    st.info(
        f"""
**Doctor:** {selected_doctor['name']}

**Specialization:** {selected_doctor['specialization']}

**Available Days:** {selected_doctor['days']}

**Available Time:** {selected_doctor['time']}
"""
    )


# ------------------------------------------------
# Appointment details
# ------------------------------------------------

st.subheader("📅 Appointment Details")


appointment_date = st.date_input(
    "Select Date",
    min_value=date.today()
)


appointment_time = st.time_input(
    "Select Time"
)


reason = st.text_area(
    "Reason for Appointment",
    placeholder=(
        "Example: General consultation, "
        "skin consultation, follow-up, etc."
    )
)


# ------------------------------------------------
# Book appointment
# ------------------------------------------------

if st.button(
    "📅 Book Appointment",
    type="primary"
):

    if not reason.strip():

        st.warning(
            "Please enter the reason for your appointment."
        )

    else:

        appointment = {

            "patient_name": patient["name"],

            "doctor_name": selected_doctor["name"],

            "specialization":
                selected_doctor["specialization"],

            "date":
                str(appointment_date),

            "time":
                str(appointment_time),

            "reason":
                reason,

            "status":
                "Booked"
        }


        # Create appointment list if it doesn't exist

        if "appointments" not in st.session_state:

            st.session_state.appointments = []


        # Save appointment

        st.session_state.appointments.append(
            appointment
        )


        st.success(
            "✅ Appointment booked successfully!"
        )


        st.balloons()


        # Confirmation

        st.subheader(
            "📋 Appointment Confirmation"
        )


        st.write(
            f"**Patient:** {patient['name']}"
        )

        st.write(
            f"**Doctor:** {selected_doctor['name']}"
        )

        st.write(
            f"**Specialization:** "
            f"{selected_doctor['specialization']}"
        )

        st.write(
            f"**Date:** {appointment_date}"
        )

        st.write(
            f"**Time:** {appointment_time}"
        )

        st.write(
            f"**Reason:** {reason}"
        )

        st.write(
            "**Status:** 🟢 Booked"
        )
