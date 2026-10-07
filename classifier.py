import re


def contains_keyword(text, keyword):
    """
    Check whether a keyword exists in the text.
    Uses word boundaries for short keywords.
    """

    keyword = keyword.lower()

    if keyword in ["ai", "sql", "php", "git", "aws", "azure"]:
        return re.search(r"\b" + re.escape(keyword) + r"\b", text) is not None

    return keyword in text


def classify_resource(title, description=""):
    """
    Automatically classify an educational resource
    into a suitable technology/education category.
    """

    title_text = str(title).lower().strip()
    description_text = str(description).lower().strip()

    # --------------------------------------------------
    # 1. DATA SCIENCE
    # --------------------------------------------------

    data_science_keywords = [
        "data science",
        "data analysis",
        "pandas",
        "numpy",
        "statistics",
        "data visualization",
        "data analytics",
        "exploratory data analysis"
    ]

    for keyword in data_science_keywords:
        if contains_keyword(title_text, keyword):
            return "Data Science"

    # --------------------------------------------------
    # 2. ARTIFICIAL INTELLIGENCE
    # --------------------------------------------------

    ai_keywords = [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "neural network",
        "natural language processing",
        "nlp",
        "computer vision",
        "reinforcement learning"
    ]

    for keyword in ai_keywords:
        if contains_keyword(title_text, keyword):
            return "Artificial Intelligence"

    # --------------------------------------------------
    # 3. DATABASE
    # --------------------------------------------------

    database_keywords = [
        "database",
        "sql",
        "mysql",
        "mongodb",
        "dbms",
        "postgresql",
        "oracle database"
    ]

    for keyword in database_keywords:
        if contains_keyword(title_text, keyword):
            return "Database"

    # --------------------------------------------------
    # 4. WEB DEVELOPMENT
    # --------------------------------------------------

    web_keywords = [
        "html",
        "css",
        "web development",
        "website",
        "frontend",
        "backend",
        "javascript",
        "php",
        "react",
        "node.js"
    ]

    for keyword in web_keywords:
        if contains_keyword(title_text, keyword):
            return "Web Development"

    # --------------------------------------------------
    # 5. CLOUD COMPUTING
    # --------------------------------------------------

    cloud_keywords = [
        "cloud computing",
        "cloud",
        "aws",
        "azure",
        "google cloud",
        "cloud services"
    ]

    for keyword in cloud_keywords:
        if contains_keyword(title_text, keyword):
            return "Cloud Computing"

    # --------------------------------------------------
    # 6. CYBER SECURITY
    # --------------------------------------------------

    cyber_keywords = [
        "cyber security",
        "cybersecurity",
        "phishing",
        "network security",
        "information security",
        "ethical hacking",
        "cyber attack",
        "penetration testing"
    ]

    for keyword in cyber_keywords:
        if contains_keyword(title_text, keyword):
            return "Cyber Security"

    # --------------------------------------------------
    # 7. TOOLS
    # --------------------------------------------------

    tools_keywords = [
        "git",
        "github",
        "docker",
        "linux",
        "version control"
    ]

    for keyword in tools_keywords:
        if contains_keyword(title_text, keyword):
            return "Tools"

    # --------------------------------------------------
    # 8. PROGRAMMING
    # --------------------------------------------------

    programming_keywords = [
        "python",
        "java",
        "programming",
        "c++",
        "c language",
        "coding",
        "javascript",
        "programming fundamentals"
    ]

    for keyword in programming_keywords:
        if contains_keyword(title_text, keyword):
            return "Programming"

    # --------------------------------------------------
    # 9. CHECK DESCRIPTION
    # --------------------------------------------------

    combined_text = f"{title_text} {description_text}"

    # Data Science
    for keyword in data_science_keywords:
        if contains_keyword(combined_text, keyword):
            return "Data Science"

    # Artificial Intelligence
    for keyword in ai_keywords:
        if contains_keyword(combined_text, keyword):
            return "Artificial Intelligence"

    # Database
    for keyword in database_keywords:
        if contains_keyword(combined_text, keyword):
            return "Database"

    # Web Development
    for keyword in web_keywords:
        if contains_keyword(combined_text, keyword):
            return "Web Development"

    # Cloud Computing
    for keyword in cloud_keywords:
        if contains_keyword(combined_text, keyword):
            return "Cloud Computing"

    # Cyber Security
    for keyword in cyber_keywords:
        if contains_keyword(combined_text, keyword):
            return "Cyber Security"

    # Tools
    for keyword in tools_keywords:
        if contains_keyword(combined_text, keyword):
            return "Tools"

    # Programming
    for keyword in programming_keywords:
        if contains_keyword(combined_text, keyword):
            return "Programming"

    # --------------------------------------------------
    # DEFAULT CATEGORY
    # --------------------------------------------------

    return "Other"