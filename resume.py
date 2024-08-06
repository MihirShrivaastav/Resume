import json

def parse_resume(resume_text):
    # Initialize a dictionary to store parsed data
    parsed_data = {
        "Name": "",
        "Contact": {
            "LinkedIn": "",
            "Email": "",
            "GitHub": "",
            "Mobile": ""
        },
        "Skills": {
            "Languages": [],
            "Tools/Platforms": [],
            "Soft Skills": []
        },
        "Training": [],
        "Projects": [],
        "Certificates": [],
        "Achievements": [],
        "Education": []
    }
    
    lines = resume_text.split('\n')
    section = None
    
    for line in lines:
        line = line.strip()
        
        # Parsing name and contact information
        if line.startswith("Mihir Srivastava"):
            parsed_data["Name"] = "Mihir Srivastava"
        elif line.startswith("Linkedin:"):
            parsed_data["Contact"]["LinkedIn"] = line.split(":")[1].strip()
        elif line.startswith("Email:"):
            parsed_data["Contact"]["Email"] = line.split(":")[1].strip()
        elif line.startswith("Github:"):
            parsed_data["Contact"]["GitHub"] = line.split(":")[1].strip()
        elif line.startswith("Mobile:"):
            parsed_data["Contact"]["Mobile"] = line.split(":")[1].strip()
        
        # Identifying sections
        elif line == "SKILLS":
            section = "Skills"
        elif line == "TRAINING":
            section = "Training"
        elif line == "PROJECTS":
            section = "Projects"
        elif line == "CERTIFICATES":
            section = "Certificates"
        elif line == "ACHIEVEMENTS":
            section = "Achievements"
        elif line == "EDUCATION":
            section = "Education"
        
        # Parsing Skills section
        elif section == "Skills":
            if "Languages:" in line:
                parsed_data["Skills"]["Languages"] = [x.strip() for x in line.split(":")[1].split(',')]
            elif "Tools/Platforms:" in line:
                parsed_data["Skills"]["Tools/Platforms"] = [x.strip() for x in line.split(":")[1].split(',')]
            elif "Soft Skills:" in line:
                parsed_data["Skills"]["Soft Skills"] = [x.strip() for x in line.split(":")[1].split(',')]
        
        # Parsing Training section
        elif section == "Training":
            if line:
                training = {"Title": line, "Date": "", "Overview": "", "Outcome": "", "Tech Stacks": []}
                parsed_data["Training"].append(training)
            elif line.startswith("•"):
                if "Tech stacks used:" in line:
                    parsed_data["Training"][-1]["Tech Stacks"] = [x.strip() for x in line.split(":")[1].split(',')]
                elif "Outcome:" in line:
                    parsed_data["Training"][-1]["Outcome"] = line.split(":")[1].strip()
                elif "Overview:" in line:
                    parsed_data["Training"][-1]["Overview"] = line.split(":")[1].strip()
                else:
                    parsed_data["Training"][-1]["Date"] = line.split(":")[1].strip()
        
        # Parsing Projects section
        elif section == "Projects":
            if line:
                project = {"Title": line, "Date": "", "Details": "", "Tech Stacks": []}
                parsed_data["Projects"].append(project)
            elif line.startswith("◦"):
                if "Tech stacks used:" in line:
                    parsed_data["Projects"][-1]["Tech Stacks"] = [x.strip() for x in line.split(":")[1].split(',')]
                else:
                    parsed_data["Projects"][-1]["Details"] = line.strip()
        
        # Parsing Certificates section
        elif section == "Certificates":
            if line.startswith("•"):
                certificate = {"Title": line.split("•")[1].strip(), "Date": ""}
                parsed_data["Certificates"].append(certificate)
            else:
                parsed_data["Certificates"][-1]["Date"] = line.strip()
        
        # Parsing Achievements section
        elif section == "Achievements":
            if line.startswith("•"):
                achievement = {"Title": line.split("•")[1].strip(), "Details": ""}
                parsed_data["Achievements"].append(achievement)
            else:
                parsed_data["Achievements"][-1]["Details"] = line.strip()
        
        # Parsing Education section
        elif section == "Education":
            if line:
                education = {"Institution": line, "Degree": "", "CGPA": "", "Duration": ""}
                parsed_data["Education"].append(education)
            elif line.startswith("Bachelor of Technology"):
                parsed_data["Education"][-1]["Degree"] = line
            elif "CGPA:" in line:
                parsed_data["Education"][-1]["CGPA"] = line.split(":")[1].strip()
            elif "-" in line:
                parsed_data["Education"][-1]["Duration"] = line
    
    return json.dumps(parsed_data, indent=4)

resume_text = """
Mihir Srivastava
Linkedin: mihirshrivastav Email: mihir.srivastava001@gmail.com
Github: MihirShrivaastav Mobile: +91-7318191290
SKILLS
• Languages: Python, R, C++
• Tools/Platforms: Tableau, Excel, Unity, Blender
• Soft Skills: Problem-Solving, Team Player, Adaptability
TRAINING
• Data Science using Python June 2023 - Aug 2023
Online Training
Overview: I was introduced to basic data types and essential Python libraries. I learned to use pandas for data
manipulation, Matplotlib and Plotly for visualization, and NumPy for numerical operations.
Outcome: I gained skills in importing data into Python and working effectively in Jupyter Notebook.
◦ Tech stacks used: Python and Jupyter Notebook.
PROJECTS
• Customer Churn Prediction Model May 2024
◦ I developed models to predict customer churn for a telecommunications company, using Logistic Regression and Random
Forest.
◦ The project included feature engineering, exploratory data analysis, and handling missing values. The models achieved
decent predictive performance.
◦ Tech stacks used: Python, VScode
• Customer Segmentation and Training December 2023
◦ Analyzed customer purchase history, demographics, and online behavior. Applied segmentation techniques Using Kmeans clustering, decision trees to identify distinct groups with unique needs.
◦ Tech stacks used: Python, VScode
• Flutter Birdie Game October 2023
◦ The project involved designing gameplay mechanics, creating assets, and implementing game logic to mimic the original
Flappy Bird experience.
◦ Key features included obstacle generation, scoring system, and collision detection to ensure a smooth and engaging
gameplay experience.
◦ Tech stacks used: Unity, C#
CERTIFICATES
• R Programming (Coursera) April 2024
• Python for Data Science, AI and Development (IBM) March 2024
• Data Visualization with Tableau (Coursera) Feb 2024
• Blockchain Basics (Coursera) Feb 2024
• Data Science using Python (Cipher Schools) Jun 2023
ACHIEVEMENTS
• Flamingo’s Graphics Designing Head Since April 2023
◦ Developed compelling graphics and layouts for use on websites, social media and in print materials.
◦ Managed and supervised a team of 8 members in a University Event (One World).
EDUCATION
Lovely Professional University Punjab, India
Bachelor of Technology - Computer Science and Engineering; CGPA: 7.54 Since August 2021
Sant Atulanand Convent School Varanasi, U.P.
Intermidiate – Percentage: 89.4% June 2018-March 2020
Sant Atulanand Convent School Punjab, India
Matriculation – Percentage: 90.6% June 2017-March 2018
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
