from sklearn.tree import DecisionTreeClassifier
import numpy as np
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory

#Run this code before opening/Usign frontend.html to start server

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

# route server to frontend.html main file
@app.route('/')
def serve_frontend():
    return send_from_directory('../', 'frontend.html')

# route server to any html file
@app.route('/<page_name>.html')
def serve_page(page_name):
    try:
        return send_from_directory('../', f'{page_name}.html')
    except FileNotFoundError:
        return "Page not found", 404

# Serve CSS files from the CSS folder
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('../css', filename)

    # Serve JavaScript files from the scripts folder
@app.route('/scripts/<path:filename>')
def serve_js(filename):
    return send_from_directory('.', filename)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    answers = data['answers']
    prediction = clf.predict([answers])
    return  prediction[0]

if __name__ == '__main__':
    app.run(debug=True)

