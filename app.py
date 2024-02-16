from pathlib import Path
import streamlit as st
from PIL import Image 


#path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

# Genral settings
PAGE_TITLE = "Digital CV | Bhagyashree Mahajan"
PAGE_ICON = ":computer"
NAME = "Bhagyashree Mahajan"
DESCRIPTION = """
Interested in deriving insights, refining data, and deploying diverse analytics to craft impactful solutions for informed decision-making.
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
col1, col2, col3, col4 = st.columns(4)

# Add Email link
with col1:
    st.markdown('<a href="mailto:mahajanbhagyashree377@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

# Add LinkedIn link
with col2:
    st.markdown('<a href="https://www.linkedin.com/in/bhagyashree-mahajan-a2577520b/" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add WhatsApp link
with col3:
    st.markdown('<a href="https://api.whatsapp.com/send/?phone=918104918297&text=Hello+there%2C+thanks+for+connecting%21&type=phone_number&app_absent=0" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1200px-WhatsApp.svg.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">WhatsApp</p>', unsafe_allow_html=True)

# Add GitHub link
with col4:
    st.markdown('<a href="https://github.com/shreearn" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)


#Experience
st.write('\n')
st.write('\n')
st.subheader("Experience")
st.write('\n')
st.write("📌","[Data Analyst Intern at AI Variant](https://drive.google.com/file/d/1-u2qiuU7Jg_2Y_hpkdJ5KFzepqJm5czP/view?usp=sharing)")
st.write("-"+" Sep 2023 - Dec 2023")
st.write(""" 
-  🔗Led a collaborative effort within a team to manage and refine extensive Excel datasets, significantly improving data quality and accuracy for a critical bank loan analysis project.
-  🔗Utilized advanced Excel Power Query techniques to clean and standardize data, resulting in a 25% reduction in data errors and inconsistencies. Integrated datasets to optimize data integrity, reducing redundant columns by 30% and harmonizing disparate data sources for more efficient analysis. Additionally, leveraged SQL expertise to extract and analyze critical KPIs.
-  🔗Created high-impact dashboards using Excel, Power BI, and Tableau, improving data visualization and enabling enhance process to make informed decisions based on finance KPIs. This effort contributed to a 15% increase in actionable insights, particularly through Power BI, for the finance domain.
-  🔗Continuously sought out and implemented new tools and techniques to enhance data analysis processes, resulting in a 10% increase in productivity.
-  🔗This hands-on experience has fostered a deep understanding of data management, analysis, and visualization within the finance sector, providing a robust foundation for contributing effectively to industry challenges

""")

#Virtual Internships
st.write('\n')
st.write('\n')
st.subheader("Virtual Internship")
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
st.write("- →✍️🛡️🚀🛟⚓🚧🟡🔴🟠🔶 BSc Data Science")
st.write("- -  Kes Shroff College")           
st.write("- - "+"2020 - 2023")
st.write('\n')
st.write("- ❇️ HSC")
st.write("- -  Swami Vivekanand International School and Jr College")
st.write("- - "+"2018 - 2020")
st.write('\n')
st.write("- ❇️ SSC")
st.write("- -  Indian Education Society")
st.write("- - "+"2007 - 2018")






#Technical skills
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Technical Skills")
st.write("---")
st.write(
    """
-   ▶️Data Analysis
-	▶️Python
-	▶️Machine Learning
-	▶️Tableau
-   ▶️Power bi
-   ▶️Data Visualization 
-   ▶️Data Mining
-   ▶️Microsoft Excel
-   ▶️Microsoft Word
-   ▶️Microsoft PowerPoint


"""
)

#soft skills
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Soft Skills")
st.write("---")
st.write(
    """
-   ▶️Adapyibility
-	▶️Communication Skills
-	▶️Teamwork

"""
)


#projects
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects")
st.write("---")
st.write("🔰[WhatsApp Chat Analyzer - Analyze chat data, visualize trends.](https://whatsapp-chat-analyzer-asxkkmsg7tccppetijqnfq.streamlit.app/)")
st.write("🔰Digital CV - Enhanced, interactive CV platform")





#Certifications
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Certifications")
st.write("---")

st.write("🎖️[Data Analyst by ExcelR ](https://drive.google.com/file/d/10nynr_WKnOBmSEG627A9YrWrxeeFN7Tc/view?usp=share_link)")
st.write("🎖️[Data Visualization: Empowering Business with Effective Insights by Tata](https://drive.google.com/file/d/11Dd7WZyU5LIhk8i9w7eZzmwoMOJ1Imvn/view?usp=share_link)")
st.write("🎖️[Advanced Ms-Excel by Kes Shroff College](https://drive.google.com/file/d/1JYDrTZ5RxPj8yPTs7Pgjo4jdCp-xUwRV/view?usp=drive_link)")
st.write("🎖️[Introduction to Large Language Models by Google](https://drive.google.com/file/d/1t_BCDRbKbr_Ost-kKI3IxpBAiQt1howe/view?usp=sharing)")
#languages known
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Languages known")
st.write("---")
st.write(
    """
- 📍English
- 📍Marathi
- 📍Hindi

"""
)





