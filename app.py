from flask import Flask, render_template

app = Flask(__name__)

# Dummy Data for Speakers
speakers = {
    "1": {"first_name": "Alice", "last_name": "Smith", "linkedin": "https://linkedin.com/in/alicesmith"},
    "2": {"first_name": "Bob", "last_name": "Jones", "linkedin": "https://linkedin.com/in/bobjones"},
    "3": {"first_name": "Charlie", "last_name": "Brown", "linkedin": "https://linkedin.com/in/charliebrown"},
    "4": {"first_name": "Diana", "last_name": "Prince", "linkedin": "https://linkedin.com/in/dianaprince"},
    "5": {"first_name": "Evan", "last_name": "Wright", "linkedin": "https://linkedin.com/in/evanwright"},
    "6": {"first_name": "Fiona", "last_name": "Gallagher", "linkedin": "https://linkedin.com/in/fionagallagher"},
    "7": {"first_name": "George", "last_name": "Miller", "linkedin": "https://linkedin.com/in/georgemiller"},
    "8": {"first_name": "Hannah", "last_name": "Abbott", "linkedin": "https://linkedin.com/in/hannahabbott"}
}

# Dummy Data for Schedule (8 talks + 1 lunch break)
# Categories: 1 = Cloud Infrastructure, 2 = AI & Data
schedule = [
    {
        "id": "T1",
        "type": "talk",
        "time": "09:00",
        "title": "Introduction to Google Cloud",
        "category": "1",
        "description": "An overview of Google Cloud Platform fundamentals and core services.",
        "speakers": [speakers["1"]]
    },
    {
        "id": "T2",
        "type": "talk",
        "time": "10:00",
        "title": "Scaling Applications with Kubernetes",
        "category": "1",
        "description": "Deep dive into GKE (Google Kubernetes Engine) and container orchestration.",
        "speakers": [speakers["2"], speakers["3"]]
    },
    {
        "id": "T3",
        "type": "talk",
        "time": "11:00",
        "title": "Machine Learning APIs in GCP",
        "category": "2",
        "description": "How to leverage Google's pre-trained machine learning APIs for vision, natural language, and translation.",
        "speakers": [speakers["4"]]
    },
    {
        "id": "L1",
        "type": "break",
        "time": "12:00",
        "title": "Lunch Break",
        "description": "Enjoy a 60-minute break with networking and catered lunch.",
        "duration": "60 mins"
    },
    {
        "id": "T4",
        "type": "talk",
        "time": "13:00",
        "title": "Data Warehousing with BigQuery",
        "category": "2",
        "description": "Exploring serverless, highly scalable, and cost-effective multi-cloud data warehouse solutions.",
        "speakers": [speakers["5"]]
    },
    {
        "id": "T5",
        "type": "talk",
        "time": "14:00",
        "title": "Serverless Computing: Cloud Run & Functions",
        "category": "1",
        "description": "Building and deploying highly scalable containerized applications on a fully managed serverless platform.",
        "speakers": [speakers["6"]]
    },
    {
        "id": "T6",
        "type": "talk",
        "time": "15:00",
        "title": "Generative AI on Google Cloud",
        "category": "2",
        "description": "Building next-generation applications with Vertex AI and foundational models.",
        "speakers": [speakers["7"], speakers["8"]]
    },
    {
        "id": "T7",
        "type": "talk",
        "time": "16:00",
        "title": "Security Best Practices in GCP",
        "category": "1",
        "description": "Ensuring your cloud environment is secure and compliant using Identity and Access Management (IAM).",
        "speakers": [speakers["1"]]
    },
    {
        "id": "T8",
        "type": "talk",
        "time": "17:00",
        "title": "Building Real-Time Data Pipelines",
        "category": "2",
        "description": "Processing streaming data with Pub/Sub and Dataflow.",
        "speakers": [speakers["4"]]
    }
]

@app.route('/')
def index():
    conference_info = {
        "date": "November 15, 2026",
        "location": "Google Tech Center, São Paulo, Brazil"
    }
    return render_template('index.html', info=conference_info, schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')