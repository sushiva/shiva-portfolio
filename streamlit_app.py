import streamlit as st
import base64
import os

# --- 0. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sudhir Shivaram - ML Engineer Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Clear cache (optional)
st.cache_data.clear()
st.cache_resource.clear()

# --- 1. GLOBAL CSS STYLING ---
st.markdown(
    '''
    <style>
    /* Hide Streamlit default menu & footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Global image styling */
    img {
        max-width: 300px;
        max-height: 300px;
        width: auto;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 10px;
    }

    /* Profile picture circular */
    .profile-img {
        border-radius: 50%;
        box-shadow: 0 0 10px rgba(0,0,0,0.4);
        max-width: 250px;
        object-fit: cover;
        margin: 0 auto;
        display: block;
    }

    /* Top navigation menu */
    .top-nav {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: -10px 0 10px 0;
        font-size: 18px;
    }

    .top-nav a {
        text-decoration: none;
        color: #333;
        font-weight: bold;
    }

    .top-nav a:hover {
        color: #0073e6;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: .35em .65em;
        font-size: 80%;
        font-weight: 700;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: .50rem;
        color: #fff;
        margin-right: 8px;
        margin-bottom: 5px;
    }
    .badge-primary { background-color: #007bff; }
    .badge-success { background-color: #28a745; }
    .badge-info { background-color: #17a2b8; }
    .badge-dark { background-color: #343a40; }
    .badge-secondary { background-color: #6c757d; }
    .badge-warning { background-color: #ffc107; color: #333; }

    /* Contact footer */
    .contact-footer-container {
        background-color: #343a40;
        color: white;
        padding: 20px 0;
        text-align: center;
    }
    .contact-footer-container a {
         color: white;
         margin: 0 10px;
    }
    .contact-footer-container i {
         margin-right: 5px;
         font-size: 1.5em;
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    ''',
    unsafe_allow_html=True
)

# --- 2. TOP NAVIGATION ---
st.markdown(
    '''
    <div class="top-nav">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
    </div>
    ''',
    unsafe_allow_html=True
)

# --- 3. PROFILE IMAGE ---
def get_image_base64(image_path):
    if not os.path.exists(image_path):
        return None
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

profile_img_path = "images/about/profile-pic.jpeg"
img_base64 = get_image_base64(profile_img_path)

# --- 4. HERO / HOME SECTION ---
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #f8f9fa; padding: 1.5rem 0; text-align: center; min-height: 200px;">
    <h1 style="font-weight: bold; font-size: 3.5rem; color: #212529;">Sudhir Shivaram</h1>
    <h2 style="font-weight: normal; font-size: 1.75rem; color: #007bff;">ML Engineer & Architect</h2>
    <p style="font-size: 1.25rem; margin-top: 20px;">Bridging Enterprise Software Engineering with Production-Ready AI.</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# --- 3. ABOUT ME SECTION ---
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>👋 About Me: Principal Engineer to ML Specialist</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Two columns: left for image, right for text
col_img, col_text = st.columns([1, 2])

with col_img:
    st.markdown(
        f'<img src="data:image/jpeg;base64,{img_base64}" alt="About Me" class="profile-img">',
        unsafe_allow_html=True
    )

with col_text:
    st.markdown("""
    **Experienced Software Engineer** with over a decade of success in **architecting and delivering end-to-end web and cloud-based applications**. Proven expertise across the full software development lifecycle—from design and integration to testing, deployment, and long-term support. 

    As a **Principal Engineer**, I’ve led cross-functional teams, shaped technical vision, and consistently elevated engineering standards in fast-paced, results-driven environments.
    """)
    
    st.markdown("""
    <p style='font-weight: bold; margin-top: 1rem; color: #007bff;'>Driven by a passion for intelligent systems. Actively expanding my skill set in:</p>
    <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
      <li><b>Machine Learning algorithms</b> and model development</li>
      <li><b>Python-based ML frameworks</b> (scikit-learn, TensorFlow, PyTorch)</li>
      <li>Data preprocessing, <b>feature engineering</b>, and visualization</li>
      <li><b>Cloud-based ML services</b> (AWS SageMaker, Azure ML, Google Vertex AI)</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.caption("My goal is to bridge the gap between robust software engineering and cutting-edge AI, creating solutions that learn, adapt, and scale.")

st.divider()

# --- 6. PROJECTS SECTION ---
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🛠️ Projects</h2>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)

def project_card(col, title, image_path, badges_html, description, study_link, code_link):
    with col:
        st.markdown(f"""
        <div style="border:1px solid #ccc; padding:15px; border-radius:10px; background-color:#f9f9f9;">
            <img src="data:image/png;base64,{get_image_base64(image_path)}" style="width:100%; border-radius:8px;" />
            <h5 style="margin-top: 10px;">{title}</h5>
            <div style="margin-bottom: 10px;">{badges_html}</div>
            <p>{description}</p>
            <div style="display: flex; justify-content: space-between;">
                <a href="{study_link}" target="_blank" style="text-decoration:none;">
                    <button style="padding:6px 12px;">Case Study</button>
                </a>
                <a href="{code_link}" target="_blank" style="text-decoration:none;">
                    <button style="padding:6px 12px;">Source Code</button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)


# Your project cards as per original
project_card(
    col_a, 
    "Food Hub Data Analysis", 
    "images/projects/foodhub-2.png",
    '<span class="badge badge-primary">Python</span><span class="badge badge-info">EDA</span><span class="badge badge-success">Numpy</span><span class="badge badge-dark">Pandas</span><span class="badge badge-dark">Seaborn</span>',
    "Exploratory Data Analysis (EDA) performed on a food aggregator dataset to uncover demand patterns and optimize delivery operations.",
    "#", "#"
)
project_card(
    col_b, 
    "Personal Loan Campaign Model", 
    "images/projects/loan-prediction.jpg",
    '<span class="badge badge-primary">Decision Tree</span><span class="badge badge-success">Model Evaluation</span><span class="badge badge-info">EDA</span><span class="badge badge-dark">Business Strategy</span>',
    "Built a Decision Tree model to predict loan acceptance, improving marketing efficiency and targeting accuracy.",
    "#", "#"
)
project_card(
    col_c, 
    "ReneWind: Predictive Maintenance", 
    "images/projects/renewind.jpg",
    '<span class="badge badge-primary">Neural Network</span><span class="badge badge-success">TensorFlow</span><span class="badge badge-info">Classification</span><span class="badge badge-dark">Data Preprocessing</span><span class="badge badge-warning">EDA</span>',
    "Developed a neural network-based classification model to predict generator failures using sensor data for proactive maintenance.",
    "#", "#"
)

st.divider()

# --- 7. SKILLS SECTION ---
st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🎯 Skills & Expertise</h2>", unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)

def skill_card(col, title, items_html):
    with col:
        st.markdown(f"""
        <div style="border:1px solid #ccc; padding:15px; border-radius:10px; background-color:#f9f9f9;">
            <h4 style="color: #007bff;">{title}</h4>
            {items_html}
        </div>
        """, unsafe_allow_html=True)


skill_card(
    col_s1, 
    "💻 Core Data Science & Languages", 
    """
    <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
      <li><b>Python (Data Stack)</b>: Expert in Pandas, NumPy, Scikit-learn, Matplotlib, and automation scripts.</li>
      <li><b>Machine Learning</b>: Supervised/unsupervised learning, Feature Engineering, and model evaluation using Scikit-learn.</li>
      <li><b>Deep Learning</b>: Hands-on with Neural Networks, CNNs, and LLM fine-tuning using TensorFlow & PyTorch.</li>
      <li><b>EDA & Data Visualization</b>: Proficient in Matplotlib, Seaborn, and Plotly for pattern discovery and data storytelling.</li>
      <li><b>SQL</b>: Skilled in complex joins, aggregations, and database optimization across multiple dialects.</li>
    </ul>
    """
)

skill_card(
    col_s2, 
    "☁️ MLOps & Enterprise Integration", 
    """
    <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.6;">
      <li><b>Cloud Computing (AWS/Azure)</b>: Deployment of scalable ML pipelines using SageMaker, Azure ML, and Dockerized workflows.</li>
      <li><b>DevOps & Containerization</b>: Proficient with Docker and Kubernetes for model serving and orchestration (MLOps).</li>
      <li><b>Snowflake</b>: Data warehousing, transformation, and ML integration using Snowpark for Python.</li>
      <li><b>Core Java & Backend Architecture</b>: 10+ years of enterprise Java design, development, and system integration experience.</li>
    </ul>
    """
)


st.divider()

# --- 8. CERTIFICATIONS SECTION ---
st.markdown("<div id='certifications'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🏅 Certifications & Courses</h2>", unsafe_allow_html=True)

col_c1, col_c2, col_c3, col_c4 = st.columns(4)


def cert_card(col, title, image_path, description, link):
    with col:
        st.markdown(f"""
        <div style="border:1px solid #ccc; padding:15px; border-radius:10px; background-color:#f9f9f9;">
            <img src="data:image/png;base64,{get_image_base64(image_path)}" style="width:100%; border-radius:8px;" />
            <h5 style="font-size: 1.1rem; margin-top: 10px;">{title}</h5>
            <p style="font-size: 0.9rem;">{description}</p>
            <a href="{link}" target="_blank" style="text-decoration:none;">
                <button style="padding:6px 12px;">View Credential</button>
            </a>
        </div>
        """, unsafe_allow_html=True)


cert_card(
    col_c3,
    "AWS Certified Cloud Practitioner",
    "images/certifications/aws-foundations.png",
    "Validated foundational knowledge of AWS Cloud concepts and services.",
    "https://achieve.snowflake.com/a317503c-10ef-4e3f-b233-1ed3a4660c0c#acc.Ajvy7JBH"
)
cert_card(
    col_c4,
    "Microsoft Azure Fundamentals (AZ-900)",
    "images/certifications/azure-fund.png",
    "Covers Azure concepts, cloud security, and compliance — demonstrating multi-cloud readiness.",
    "https://learn.microsoft.com/en-us/users/sudhirshivaram-4582/transcript/deegkcw45qxkyk0?source=docs&tab=tab-modules"
)

st.divider()

# --- 9. CONTACT SECTION ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-footer-container'>
    <h2 style='font-size: 1.5rem; color: white; margin-bottom: 10px;'>Contact Me</h2>
    <div style='display: flex; flex-wrap: wrap; justify-content: center; align-items: center;'>
      <div style='margin: 0 10px;'><i class="fas fa-envelope mr-1"></i> loremipsum@gmail.com</div>
      <div style='margin: 0 10px;'><i class="fas fa-phone mr-1"></i> 415xxxxxxx</div>
      <span style='color: #6c757d; margin: 0 10px;'>|</span> 
      <a href="https://linkedin.com/in/yourusername" target="_blank" class="contact-icon"><i class="fab fa-linkedin"></i></a>
      <a href="https://github.com/sudhirshivaram" target="_blank" class="contact-icon"><i class="fab fa-github"></i></a>
      <a href="https://medium.com/@yourusername" target="_blank" class="contact-icon"><i class="fab fa-medium"></i></a>
    </div>
</div>
""", unsafe_allow_html=True)
