from sklearn.tree import DecisionTreeClassifier
import numpy as np

# List of questions (features)
questions = [
    "Do you like technology?",
    "Do you enjoy working with numbers and data?",
    "Do you prefer working with people?",
    "Do you enjoy solving complex problems?",
    "Do you consider yourself a creative person?",
    "Do you enjoy managing others or leading teams?",
    "Do you prefer working outdoors?",
    "Do you like helping people directly (e.g., teaching, counseling, healthcare)?",
    "Do you prefer working with your hands (e.g., building, crafting, repairing)?",
    "Do you enjoy analyzing and interpreting data?",
    "Do you prefer structured, routine work?",
    "Do you enjoy writing or working with words?",
    "Do you like learning new languages or working in a global environment?",
    "Do you enjoy performing or public speaking?",
    "Are you interested in law and justice?",
    "Do you enjoy working in the medical field or helping patients?",
    "Do you prefer designing and creating things (e.g., architecture, products, clothes)?",
    "Do you enjoy programming or writing code?",
    "Do you like working in a laboratory or with scientific experiments?",
    "Do you enjoy working in finance or handling money?"
]


# Binary feature matrix (1 = Yes, 0 = No)
X = np.array([
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Software Engineer
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Data Scientist
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Project Manager
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Teacher
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # Graphic Designer
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Finance Manager
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Construction Worker
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # Nurse
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Police Officer
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],  # Journalist
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # Research Scientist
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Environmental Scientist
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # Lab Technician
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]   # Lawyer
])

y = [
    "Software Engineer",
    "Data Scientist",
    "Project Manager",
    "Teacher",
    "Graphic Designer",
    "Finance Manager",
    "Construction Worker",
    "Nurse",
    "Police Officer",
    "Journalist",
    "Research Scientist",
    "Environmental Scientist",
    "Lab Technician",
    "Lawyer"
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