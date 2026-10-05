import streamlit as st


st.set_page_config(
    page_title="Appointment History",
    page_icon="📋"
)


st.title("📋 Appointment History")

st.write(
    "View and manage your booked appointments."
)


# ------------------------------------------------
# Check patient profile
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
# Get appointments
# ------------------------------------------------

if "appointments" not in st.session_state:

    st.session_state.appointments = []


appointments = st.session_state.appointments


# ------------------------------------------------
# Check appointments
# ------------------------------------------------

if len(appointments) == 0:

    st.info(
        "📭 You don't have any appointments yet."
    )

    st.write(
        "Go to the **Appointments** page to book one."
    )

    st.stop()


# ------------------------------------------------
# Display appointments
# ------------------------------------------------

for index, appointment in enumerate(appointments):


    # Only show appointments for current patient

    if (
        appointment["patient_name"]
        != patient["name"]
    ):

        continue


    st.divider()


    st.subheader(
        f"📅 Appointment #{index + 1}"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            f"👤 **Patient:** "
            f"{appointment['patient_name']}"
        )

        st.write(
            f"👨‍⚕️ **Doctor:** "
            f"{appointment['doctor_name']}"
        )

        st.write(
            f"🩺 **Specialization:** "
            f"{appointment['specialization']}"
        )


    with col2:

        st.write(
            f"📅 **Date:** "
            f"{appointment['date']}"
        )

        st.write(
            f"⏰ **Time:** "
            f"{appointment['time']}"
        )

        st.write(
            f"📝 **Reason:** "
            f"{appointment['reason']}"
        )


    # ------------------------------------------------
    # Status
    # ------------------------------------------------

    if appointment["status"] == "Booked":

        st.success(
            "🟢 Status: Booked"
        )


        # Cancel button

        if st.button(
            "❌ Cancel Appointment",
            key=f"cancel_{index}"
        ):

            st.session_state.appointments[
                index
            ]["status"] = "Cancelled"


            st.success(
                "Appointment cancelled successfully."
            )


            st.rerun()


    else:

        st.error(
            "🔴 Status: Cancelled"
        )
