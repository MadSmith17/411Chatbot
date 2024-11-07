from sklearn.tree import DecisionTreeClassifier
import numpy as np
import joblib
from flask_cors import CORS
from flask import Flask, request, jsonify



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



# Save the JavaScript code to a file
#with open('decision_tree_model.js', 'w') as f:
    #f.write(js_code)

#print("Decision tree model exported to JavaScript successfully.")

#joblib.dump(clf, 'decision_tree_model.joblib')

#start up flask server for decision tree communicatiion with js script
app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    answers = data['answers']
    prediction = clf.predict([answers])
    return  prediction[0]

if __name__ == '__main__':
    app.run(debug=True)

