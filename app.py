from pathlib import Path
import streamlit as st
from PIL import Image


#path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile pic.png"

# Genral settings
PAGE_TITLE = "Digital CV | Bhagyashree Mahajan"
PAGE_ICON = ":computer"
NAME = "Bhagyashree Mahajan"
DESCRIPTION = """
Data Wizard with a Curious Mind and a Knack for Unveiling Insights that Drive Results.
"""

PROJECTS = {
    "🏆 WhatsApp Chat Analyzer": "https://shreearn-whatsapp-chat-analyzer-app-4qxd5g.streamlit.app/"
}
CERTIFICATIONS = {
    "Advanced Ms-Excel":"https://drive.google.com/file/d/1JYDrTZ5RxPj8yPTs7Pgjo4jdCp-xUwRV/view?usp=drive_link"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.write("\n")
# load css , pdf and profile pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=290)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


st.write('\n')
st.write('\n')
st.write('\n')


# Create columns for each social media link
col1, col2, col3 = st.columns(3)

# Add Email link
with col1:
    st.markdown('<a href="mailto:mahajanbhagyashree377@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

# Add LinkedIn link
with col2:
    st.markdown('<a href="https://www.linkedin.com/in/bhagyashree-mahajan-a2577520b/" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col3:
    st.markdown('<a href="https://github.com/shreearn" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

#Experience
st.write('\n')
st.write('\n')
st.subheader("Experience")
st.write('\n')
st.write("📌","[Data Science Intern at LetsGrowMore](https://drive.google.com/file/d/1dbRHXvTWWnDxYnoMQYbHk8NfqxtHMIaY/view?usp=drive_link)")
st.write("-"+" Mar 2023 - Apr 2023")
st.write(""" 
-  🔗Developed decision tree algorithm for classification with data preprocessing and feature engineering.
-  🔗Analyzed Iris dataset, ensured data integrity through cleaning and preprocessing.
-  🔗Utilized statistical techniques and data visualization to accurately classify Iris flower species.
-  🔗Developed LSTM model for time series prediction with data preprocessing and hyperparameter tuning.
-  🔗Demonstrated strong problem-solving skills and proficiency in Python for machine learning.
""")



st.write('\n')
st.write('\n')
st.write('\n')
st.write("📌","[Data Visualization: Empowering Business with Effective Insights | TATA] (https://drive.google.com/file/d/11Dd7WZyU5LIhk8i9w7eZzmwoMOJ1Imvn/view?usp=sharing)")
st.write("-"+" May 2023 - Jul 2023")
st.write("""
-  🔗Frame business scenarios to understand objectives and define visualization requirements.
-  🔗Select appropriate visualizations based on data analysis to effectively represent patterns, trends, and relationships.
-  🔗Create impactful visualizations using Tableau, applying best practices in design for accuracy, reliability, and visual appeal.
-  🔗Communicate insights and analysis through clear narratives and presentations to stakeholders.
""")

st.write('\n')
st.write('\n')
st.write('\n')
st.write("📌","[Data Science & Business Analytics intern at The Sparks Foundation](https://drive.google.com/file/d/16F0T-6gsIOY2UpZnpwgTyEEI5IsrumLA/view?usp=sharing)")
st.write("-"+" Apr 2023 - May 2023")
st.write(""" 
-  🔗Utilized supervised machine learning techniques to predict student performance based on study hours using Linear Regression with Python's Scikit Learn library.Developed a model to forecast the percentage of a student based on the number of study hours.
-  🔗Employed unsupervised machine learning methods, specifically K-Means Clustering.Determined the optimal number of clusters and represented them visually.
"""
)

st.write('\n')
st.write('\n')
st.write('\n')
st.write("📌","[Data Science Intern at Bharat Intern](https://drive.google.com/file/d/1qHdecIs6TGUby3MGUFC2LRgVS30DrCvp/view?usp=drive_link)")
st.write("-"+" May 2023 - Jun 2023")
st.write(""" 
-  🔗Developed stock price prediction system using LSTM neural networks, preprocessing historical data, and evaluating performance.
-  🔗Built Titanic survival prediction system, preprocessing and analyzing data, using machine learning algorithms, and presenting findings.
"""
)

#Qualification
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Qualifications")
st.write("---")
st.write("- 📚 BSc Data Science ")
st.write("- -  KES Shroff College")
st.write("- - "+"2020 - 2023")
st.write('\n')
st.write("- 📚 HSC")
st.write("- -  Swami Vivekanand International School and Jr College")
st.write("- - "+"2018 - 2020")
st.write('\n')
st.write("- 📚 SSC")
st.write("- -  Indian Education Society")
st.write("- - "+"2007 - 2018")






#skills
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Skills")
st.write("---")
st.write(
    """
-   🎯 Data Analysis
-	🎯Python
-	🎯Machine Learning
-	🎯Excel
-	🎯Tableau
"""
)



#projects
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects")
st.write("---")
st.write("🏆WhatsApp Chat Analyzer")
st.write("🏆Digital CV")





#Certifications
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Certifications")
st.write("---")

st.write("📄[Advanced Ms-Excel](https://drive.google.com/file/d/1JYDrTZ5RxPj8yPTs7Pgjo4jdCp-xUwRV/view?usp=drive_link)")







