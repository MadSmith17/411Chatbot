from sklearn.tree import DecisionTreeClassifier
import numpy as np

# List of questions (features)
questions = [
    "Do you enjoy problem-solving?",                      # Feature 1
    "Do you prefer working with hardware over software?", # Feature 2
    "Do you enjoy creating user interfaces?",             # Feature 3
    "Are you interested in data analysis?",               # Feature 4
    "Do you prefer working independently?",               # Feature 5
    "Are you interested in cybersecurity and protecting data?", # Feature 6
    "Do you have an interest in artificial intelligence?",       # Feature 7
    "Do you enjoy optimizing processes and systems?",            # Feature 8
    "Are you interested in networking and computer systems?",     # Feature 9
    "Do you enjoy working directly with clients or stakeholders?" # Feature 10
]


# Binary feature matrix (1 = Yes, 0 = No)
X = np.array([
    # Feature values for each question, followed by Job Title
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 0], 
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0], 
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1], 
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0], 
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 0], 
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0], 
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0], 
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]
])

y = [
    # Feature values for each question, followed by Job Title
    "Front-End Developer",
     "Data Scientist",
    "Network Engineer",
     "Machine Learning Engineer",
    "Cybersecurity Specialist",
    "Full Stack Developer",
     "Computer Hardware Engineer",
    "Backend Developer",
    "UX/UI Designer",
    "Systems Administrator",
    "Database Administrator",
     "Software Developer",
     "Security Analyst",
    "Research Scientist",
     "Product Manager",
    "AI Engineer",
    "Ethical Hacker",
    "IT Consultant",
    "Solutions Architect"
]

# Step 2: Train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)


def ask_question(question):
    answer = input(question + " (Yes/No): ").strip().lower()
    if answer == 'yes':
        return 1
    elif answer == 'no':
        return 0
    else:
        print("Invalid response. Please answer Yes or No.")
        return ask_question(question)  # Ask again if the response is invalid

def predict_career(clf, questions):
    user_answers = []
    for question in questions:
        answer = ask_question(question)
        user_answers.append(answer)
    
    # Convert to numpy array and reshape to match input format
    user_answers = np.array(user_answers).reshape(1, -1)
    
    # Predict the career based on user answers
    prediction = clf.predict(user_answers)
    print(f"Based on your answers, a suitable career path for you could be: {prediction[0]}")

# Run the interactive career predictor
predict_career(clf, questions)