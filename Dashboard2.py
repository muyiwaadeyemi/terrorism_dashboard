import streamlit as st
import pandas as pd
from PIL import Image


# Dashboard Layout
st.title("World Terrorism Analysis Dashboard 1970-2017")

with st.container():
    st.subheader("Global Terrorist Incidents")
    col1, col2, col3 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col1:
        st.subheader("Incident over time")
        image1 = Image.open("Capture 01.JPG")
        st.image(image1, caption="Incident over time", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col2:
        st.subheader("Casualties")
        image2 = Image.open("Capture 02.JPG")
        st.image(image2, caption="Calsualties by Region", use_container_width=True)

    #Customer Distribution by Customer Type
    with col3:    
        st.subheader("Casualties over time")
        image3 = Image.open("Capture 03.JPG")
        st.image(image3, caption="casualties over time", use_container_width=True)
        

        
        
        
with st.container():
    st.subheader("")
    col4, col5, col6 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col4:
        st.subheader("Most Common Attack Type")
        image1 = Image.open("Capture 04.JPG")
        st.image(image1, caption="Most Common Attack Type", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col5:
        st.subheader("Most Common Attack")
        image2 = Image.open("Capture 05.JPG")
        st.image(image2, caption="Most Common Attack", use_container_width=True)

    #Customer Distribution by Customer Type
    with col6:    
        st.subheader("Regional Attacks")
        image3 = Image.open("Capture 06.JPG")
        st.image(image3, caption="Regional Distribution of Attacks", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col7, col8, col9 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col7:
        st.subheader("Average Attacks")
        image1 = Image.open("Capture 07.JPG")
        st.image(image1, caption="Average successful vs Unsuccessful", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col8:
        st.subheader("Rate of Attack by Region")
        image2 = Image.open("Capture 08.JPG")
        st.image(image2, caption="Rate of Attack by Region", use_container_width=True)

    #Customer Distribution by Customer Type
    with col9:    
        st.subheader("Suicide vs Non_Suicide")
        image3 = Image.open("Capture 09.JPG")
        st.image(image3, caption="Suicide vs Non_Suicide", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col10, col11, col12 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col10:
        st.subheader("Trends in Suicide Attacks")
        image1 = Image.open("Capture 10.JPG")
        st.image(image1, caption="Trends in Suicide Attacks", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col11:
        st.subheader("Most Active Terrorist Group")
        image2 = Image.open("Capture 11.JPG")
        st.image(image2, caption="Most Active Terrorist Group", use_container_width=True)

    #Customer Distribution by Customer Type
    with col12:    
        st.subheader("Casualties by Terrorist Group")
        image3 = Image.open("Capture 12.JPG")
        st.image(image3, caption="Casualties by Terrorist Group", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col13, col14, col15 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col13:
        st.subheader("Regional Presence of Terrorist Group")
        image1 = Image.open("Capture 13.JPG")
        st.image(image1, caption="Regional Presence of Terrorist Group", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col14:
        st.subheader("Most Common Attack Type")
        image2 = Image.open("Capture 14.JPG")
        st.image(image2, caption="Most Common Attack Type", use_container_width=True)

    #Customer Distribution by Customer Type
    with col15:    
        st.subheader("Most Common Target Type")
        image3 = Image.open("Capture 15.JPG")
        st.image(image3, caption="Most Common Target Type", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col16, col17, col18 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col16:
        st.subheader("Casualties by Attack and Target Type")
        image1 = Image.open("Capture 16.JPG")
        st.image(image1, caption="Casualties by Attack and Target Type", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col17:
        st.subheader("Most Common Weapon Types")
        image2 = Image.open("Capture 17.JPG")
        st.image(image2, caption="Most Common Weapon Types", use_container_width=True)

    #Customer Distribution by Customer Type
    with col18:    
        st.subheader("Average Casualties by Weapon Type")
        image3 = Image.open("Capture 18.JPG")
        st.image(image3, caption="Average Casualties by Weapon Type", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col19, col20, col21 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col19:
        st.subheader("Trends in Weapon Use Over Time")
        image1 = Image.open("Capture 19.JPG")
        st.image(image1, caption="Trends in Weapon Use Over Time", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col20:
        st.subheader("Casualties Over Time by Region")
        image2 = Image.open("Capture 20.JPG")
        st.image(image2, caption="Casualties Over Time by Region", use_container_width=True)

    #Customer Distribution by Customer Type
    with col21:    
        st.subheader("Total Incidents by Region")
        image3 = Image.open("Capture 21.JPG")
        st.image(image3, caption="Total Incidents by Region", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col22, col23, col24 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col22:
        st.subheader("Total Casualties by Region")
        image1 = Image.open("Capture 22.JPG")
        st.image(image1, caption="Total Casualties by Region", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col23:
        st.subheader("Global Trends in Terrorism (Incidents and Casualties) Over Time")
        image2 = Image.open("Capture 23.JPG")
        st.image(image2, caption="'Global Trends in Terrorism (Incidents and Casualties) Over Time", use_container_width=True)

    #Customer Distribution by Customer Type
    with col24:    
        st.subheader("Trends in Terrorist Incidents in High-Risk Regions Over Time")
        image3 = Image.open("Capture 24.JPG")
        st.image(image3, caption="Trends in Terrorist Incidents in High-Risk Regions Over Time", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col25, col26, col27 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col25:
        st.subheader("Trends in Terrorist Casualties in High-Risk Regions Over Time")
        image1 = Image.open("Capture 25.JPG")
        st.image(image1, caption="Trends in Terrorist Casualties in High-Risk Regions Over Time", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col26:
        st.subheader("average casualties per incident")
        image2 = Image.open("Capture 26.JPG")
        st.image(image2, caption="average casualties per incident", use_container_width=True)

    #Customer Distribution by Customer Type
    with col27:    
        st.subheader("Top 10 Most Affected Countries by Incidents and Casualties")
        image3 = Image.open("Capture 27.JPG")
        st.image(image3, caption="Top 10 Most Affected Countries by Incidents and Casualties", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col28, col29, col30 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col28:
        st.subheader("Trends in Attack Types Over Time")
        image1 = Image.open("Capture 28.JPG")
        st.image(image1, caption="Trends in Attack Types Over Time", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col29:
        st.subheader("Trends in Target Types Over Time")
        image2 = Image.open("Capture 29.JPG")
        st.image(image2, caption="Trends in Target Types Over Time", use_container_width=True)

    #Customer Distribution by Customer Type
    with col30:    
        st.subheader("Top 3 Weapon Types Used by Region")
        image3 = Image.open("Capture 30.JPG")
        st.image(image3, caption="Top 3 Weapon Types Used by Region", use_container_width=True)
        
        
with st.container():
    st.subheader("")
    col31, col32, col33 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col31:
        st.subheader("Top 10 Terrorism Hotspot Countries Over Time")
        image1 = Image.open("Capture 31.JPG")
        st.image(image1, caption="Top 10 Terrorism Hotspot Countries Over Time", use_container_width=True)

    # Satisfaction Breakdown (Pie Chart)
   # with col32:
       # st.subheader("Trends in Target Types Over Time")
       # image2 = Image.open("Capture 32.JPG")
       # st.image(image2, caption="Trends in Target Types Over Time", use_container_width=True)

    #Customer Distribution by Customer Type
   # with col33:    
      #  st.subheader("Top 3 Weapon Types Used by Region")
      #  image3 = Image.open("Capture 33.JPG")
       # st.image(image3, caption="Top 3 Weapon Types Used by Region", use_container_width=True)