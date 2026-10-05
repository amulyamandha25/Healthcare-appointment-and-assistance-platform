import streamlit as st


st.set_page_config(
    page_title="Doctors",
    page_icon="👨‍⚕️"
)


st.title("👨‍⚕️ Find a Doctor")

st.write(
    "Search doctors by name or medical specialization."
)


# Sample doctor data
# These are fictional doctors for project demonstration.

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


# Search box
search = st.text_input(
    "🔎 Search Doctor or Specialization",
    placeholder="Example: Cardiologist"
)


st.divider()


# Display doctors
found_doctor = False


for doctor in doctors:

    search_text = (
        doctor["name"]
        + " "
        + doctor["specialization"]
    ).lower()


    if search.lower() in search_text:

        found_doctor = True

        with st.container(border=True):

            col1, col2 = st.columns([1, 3])


            with col1:

                st.markdown(
                    "### 👨‍⚕️"
                )


            with col2:

                st.subheader(
                    doctor["name"]
                )

                st.write(
                    f"🩺 **Specialization:** "
                    f"{doctor['specialization']}"
                )

                st.write(
                    f"📅 **Available Days:** "
                    f"{doctor['days']}"
                )

                st.write(
                    f"⏰ **Available Time:** "
                    f"{doctor['time']}"
                )


if not found_doctor:

    st.warning(
        "No doctor found. Try another name or specialization."
    )
