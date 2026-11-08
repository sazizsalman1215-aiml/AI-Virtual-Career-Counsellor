import streamlit as st 
from fpdf import FPDF 

# =====================================================
# PROJECT: AI VIRTUAL CAREER COUNSELLOR
# DOMAIN: ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
# =====================================================

st.set_page_config(
    page_title="AI Virtual Career Counsellor",
    page_icon="🎓",
    layout="centered"
)

# =====================================================
# CAREER DATABASE
# =====================================================

career_data = {

    "Mathematics": {
        "Numbers, Statistics and Data": {
            "careers": [
                "Data Analyst",
                "Statistician",
                "Data Scientist"
            ],
            "skills": "Mathematics, Statistics, Python, Data Analysis",
            "roadmap": [
                "Learn basic Mathematics and Statistics.",
                "Learn Python programming.",
                "Practice data analysis using real datasets.",
                "Build data analysis projects and create a portfolio."
            ]
        },

        "Finance and Money": {
            "careers": [
                "Financial Analyst",
                "Accountant",
                "Investment Analyst"
            ],
            "skills": "Mathematics, Accounting, Financial Analysis, Excel",
            "roadmap": [
                "Learn basic financial concepts.",
                "Study Accounting and Economics.",
                "Learn Excel and financial analysis.",
                "Practice with financial projects."
            ]
        },

        "Engineering and Technology": {
            "careers": [
                "Civil Engineer",
                "Mechanical Engineer",
                "Electrical Engineer"
            ],
            "skills": "Mathematics, Physics, Problem Solving, Engineering",
            "roadmap": [
                "Build strong Mathematics and Physics knowledge.",
                "Learn engineering fundamentals.",
                "Practice technical tools and software.",
                "Work on engineering projects."
            ]
        },

        "Teaching and Research": {
            "careers": [
                "Mathematics Teacher",
                "Research Scientist",
                "Mathematics Professor"
            ],
            "skills": "Mathematics, Communication, Research, Problem Solving",
            "roadmap": [
                "Develop strong mathematical knowledge.",
                "Improve communication and teaching skills.",
                "Study advanced Mathematics.",
                "Participate in research and teaching activities."
            ]
        }
    },

    "Computer Science": {
        "AI and Machine Learning": {
            "careers": [
                "AI Engineer",
                "Machine Learning Engineer",
                "Data Scientist"
            ],
            "skills": "Python, Mathematics, Machine Learning, Data Analysis",
            "roadmap": [
                "Learn Python programming.",
                "Study Mathematics and Statistics.",
                "Learn Machine Learning fundamentals.",
                "Build AI and Machine Learning projects."
            ]
        },

        "Software and Programming": {
            "careers": [
                "Software Developer",
                "Web Developer",
                "Application Developer"
            ],
            "skills": "Python, Java, HTML, CSS, Problem Solving",
            "roadmap": [
                "Learn a programming language.",
                "Practice Data Structures and Algorithms.",
                "Learn web or application development.",
                "Build and publish software projects."
            ]
        },

        "Cybersecurity and Networks": {
            "careers": [
                "Cybersecurity Analyst",
                "Network Engineer",
                "Security Consultant"
            ],
            "skills": "Computer Networks, Linux, Security Concepts, Problem Solving",
            "roadmap": [
                "Learn computer fundamentals.",
                "Study networking and operating systems.",
                "Learn cybersecurity concepts in legal practice environments.",
                "Build security knowledge through safe projects and certifications."
            ]
        },

        "Hardware and Robotics": {
            "careers": [
                "Robotics Engineer",
                "Embedded Systems Engineer",
                "Hardware Engineer"
            ],
            "skills": "Electronics, Programming, Robotics, Microcontrollers",
            "roadmap": [
                "Learn basic electronics.",
                "Study programming and microcontrollers.",
                "Understand sensors and robotics concepts.",
                "Build safe robotics and hardware projects."
            ]
        }
    },

    "Biology": {
        "Patient Care and Healthcare": {
            "careers": [
                "Doctor",
                "Nurse",
                "Physiotherapist"
            ],
            "skills": "Biology, Communication, Patient Care, Medical Knowledge",
            "roadmap": [
                "Study Biology and Human Anatomy.",
                "Understand healthcare and medical subjects.",
                "Complete the required professional education.",
                "Gain supervised practical experience."
            ]
        },

        "Laboratory and Research": {
            "careers": [
                "Microbiologist",
                "Biochemist",
                "Research Scientist"
            ],
            "skills": "Biology, Chemistry, Laboratory Skills, Research",
            "roadmap": [
                "Learn Biology and Chemistry fundamentals.",
                "Study Microbiology and Biochemistry.",
                "Learn laboratory techniques under supervision.",
                "Participate in research projects."
            ]
        },

        "Medicines and Pharmacy": {
            "careers": [
                "Pharmacist",
                "Clinical Research Associate",
                "Pharmaceutical Scientist"
            ],
            "skills": "Chemistry, Biology, Pharmaceutical Knowledge, Research",
            "roadmap": [
                "Study Biology and Chemistry.",
                "Learn about medicines and pharmaceutical science.",
                "Complete the required pharmacy or related degree.",
                "Gain professional training and experience."
            ]
        },

        "Plants and Animals": {
            "careers": [
                "Botanist",
                "Zoologist",
                "Wildlife Biologist"
            ],
            "skills": "Biology, Environmental Science, Observation, Research",
            "roadmap": [
                "Learn plant and animal biology.",
                "Study Botany or Zoology.",
                "Participate in supervised field studies.",
                "Work on biodiversity and conservation projects."
            ]
        },

        "Environment and Nature": {
            "careers": [
                "Environmental Scientist",
                "Ecologist",
                "Conservation Scientist"
            ],
            "skills": "Environmental Science, Biology, Research, Data Analysis",
            "roadmap": [
                "Learn environmental science basics.",
                "Study ecosystems and biodiversity.",
                "Participate in environmental projects.",
                "Develop skills in conservation and research."
            ]
        }
    },

    "Arts and Design": {
        "Drawing and Visual Design": {
            "careers": [
                "Graphic Designer",
                "Illustrator",
                "UI Designer"
            ],
            "skills": "Creativity, Drawing, Design Tools, Visual Communication",
            "roadmap": [
                "Practice drawing and creative thinking.",
                "Learn graphic design fundamentals.",
                "Practice using design software.",
                "Create a design portfolio."
            ]
        },

        "Writing and Communication": {
            "careers": [
                "Content Writer",
                "Journalist",
                "Copywriter"
            ],
            "skills": "Writing, Communication, Creativity, Research",
            "roadmap": [
                "Improve reading and writing skills.",
                "Practice different writing styles.",
                "Learn research and editing.",
                "Create a writing portfolio."
            ]
        },

        "Film and Entertainment": {
            "careers": [
                "Film Director",
                "Video Editor",
                "Animator"
            ],
            "skills": "Creativity, Storytelling, Editing, Visual Design",
            "roadmap": [
                "Learn storytelling and creative concepts.",
                "Understand filmmaking basics.",
                "Practice video editing and animation.",
                "Create short films or animation projects."
            ]
        },

        "Fashion and Creativity": {
            "careers": [
                "Fashion Designer",
                "Fashion Illustrator",
                "Fashion Stylist"
            ],
            "skills": "Creativity, Drawing, Design, Fashion Knowledge",
            "roadmap": [
                "Learn fashion and design fundamentals.",
                "Practice sketching and illustration.",
                "Study fabrics, colours and patterns.",
                "Create a fashion design portfolio."
            ]
        }
    },

    "Business": {
        "Finance and Accounting": {
            "careers": [
                "Accountant",
                "Financial Analyst",
                "Auditor"
            ],
            "skills": "Accounting, Mathematics, Excel, Financial Knowledge",
            "roadmap": [
                "Learn basic accounting concepts.",
                "Study finance and taxation.",
                "Practice Excel and accounting software.",
                "Gain practical experience through projects."
            ]
        },

        "Marketing and Sales": {
            "careers": [
                "Marketing Manager",
                "Digital Marketing Specialist",
                "Sales Executive"
            ],
            "skills": "Communication, Marketing, Creativity, Market Research",
            "roadmap": [
                "Learn marketing fundamentals.",
                "Study digital marketing concepts.",
                "Practice content creation and market research.",
                "Work on marketing projects."
            ]
        },

        "Management and Leadership": {
            "careers": [
                "Business Manager",
                "Project Manager",
                "Human Resource Manager"
            ],
            "skills": "Leadership, Communication, Planning, Teamwork",
            "roadmap": [
                "Learn business management basics.",
                "Improve communication and teamwork.",
                "Practice planning and decision-making.",
                "Develop leadership experience through projects."
            ]
        },

        "Starting a Business": {
            "careers": [
                "Entrepreneur",
                "Startup Founder",
                "Business Consultant"
            ],
            "skills": "Business Planning, Creativity, Communication, Finance",
            "roadmap": [
                "Learn basic business concepts.",
                "Identify problems and business opportunities.",
                "Prepare a simple business plan.",
                "Develop and test a small business idea."
            ]
        },

        "Economics and Analysis": {
            "careers": [
                "Economist",
                "Business Analyst",
                "Market Research Analyst"
            ],
            "skills": "Economics, Mathematics, Statistics, Analytical Thinking",
            "roadmap": [
                "Learn basic Economics.",
                "Study Statistics and Mathematics.",
                "Practice analysing economic information.",
                "Build research and analysis projects."
            ]
        }
    }
}


# =====================================================
# PDF REPORT GENERATION
# =====================================================

def create_pdf(name, subject, interest, result):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    pdf.add_page()

    # Safe text for built-in PDF fonts
    def safe_text(value):
        return str(value).encode("latin-1", "replace").decode("latin-1")

    # Common text function
    def write_text(text, height=8, bold=False, size=11):
        pdf.set_x(pdf.l_margin)
        pdf.set_font("Arial", "B" if bold else "", size)
        pdf.multi_cell(
            pdf.epw,
            height,
            safe_text(text)
        )

    # Main heading
    write_text("AI VIRTUAL CAREER COUNSELLOR", 12, True, 16)
    pdf.ln(5)

    # Student details
    write_text("STUDENT DETAILS", 10, True, 13)
    write_text(f"Name: {name}")
    write_text(f"Subject: {subject}")
    write_text(f"Interest: {interest}")
    pdf.ln(4)

    # Career recommendations
    write_text("RECOMMENDED CAREERS", 10, True, 13)

    careers = result.get("careers", [])
    for index, career in enumerate(careers, 1):
        write_text(f"{index}. {career}")

    pdf.ln(4)

    # Required skills
    write_text("REQUIRED SKILLS", 10, True, 13)

    skills = result.get("skills", [])
    if isinstance(skills, list):
        for skill in skills:
            write_text(f"- {skill}")
    else:
        write_text(skills)

    pdf.ln(4)

    # Career roadmap
    write_text("CAREER ROADMAP", 10, True, 13)

    roadmap = result.get("roadmap", [])
    if isinstance(roadmap, list):
        for index, step in enumerate(roadmap, 1):
            write_text(f"{index}. {step}")
    else:
        write_text(roadmap)

    pdf.ln(5)

    # Footer note
    write_text(
        "Note: These career suggestions are based on your selected "
        "subject and interests. Explore each career before making "
        "your final decision.",
        8,
        False,
        10
    )

    # Return PDF as bytes
    return bytes(pdf.output())



    
# =====================================================
# STREAMLIT USER INTERFACE
# =====================================================

st.title("🎓 AI Virtual Career Counsellor")

st.write(
    "Discover career options based on your favourite subject "
    "and personal interests."
)

st.divider()

st.subheader("Enter Your Details")

name = st.text_input(
    "Enter Your Name",
    placeholder="Enter your full name"
)

subject = st.selectbox(
    "Select Your Favourite Subject",
    ["Select Subject"] + list(career_data.keys())
)

if subject != "Select Subject":

    interest_options = list(career_data[subject].keys())

    interest = st.selectbox(
        "Select Your Area of Interest",
        ["Select Interest"] + interest_options
    )

else:
    interest = "Select Interest"

st.divider()

if st.button("🔍 Find My Career", use_container_width=True):

    if not name.strip():
        st.warning("Please enter your name.")

    elif subject == "Select Subject":
        st.warning("Please select your favourite subject.")

    elif interest == "Select Interest":
        st.warning("Please select your area of interest.")

    else:
        st.session_state["report"] = {
            "name": name.strip(),
            "subject": subject,
            "interest": interest,
            "result": career_data[subject][interest]
        }

    
# =====================================================
# DISPLAY CAREER REPORT
# =====================================================

if "report" in st.session_state:

    report = st.session_state["report"]

    st.success("Your Career Report Is Ready!")

    st.header("Hello, " + report["name"] + "!")

    st.subheader("Your Selected Details")

    st.write("**Subject:**", report["subject"])
    st.write("**Interest:**", report["interest"])

    st.divider()

    st.subheader("🌟 Recommended Careers")

    for index, career in enumerate(report["result"]["careers"], 1):
        st.write(f"{index}. **{career}**")

    st.divider()

    st.subheader("💡 Required Skills")

    st.write(report["result"]["skills"])

    st.divider()

    st.subheader("🗺️ Your Career Roadmap")

    for index, step in enumerate(report["result"]["roadmap"], 1):
        st.write(f"**Step {index}:** {step}")

    st.divider()
    

    st.subheader("📄 Download Your Report")

    pdf_data = create_pdf(
        report["name"],
        report["subject"],
        report["interest"],
        report["result"]
    )

    st.download_button(
        label="⬇️ Download Career Report (PDF)",
        data=pdf_data,
        file_name="Career_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.divider()

st.caption(
    "AI Virtual Career Counsellor | AIML Project | "
    "Career suggestions are based on a predefined career database."
)
