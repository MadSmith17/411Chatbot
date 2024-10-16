from flask import Flask, render_template, request

app = Flask(__name__)

# Resume chatbot logic
class ResumeHelpBot:
    def __init__(self):
        self.questions = [
            "Do you have work experience? (yes/no)",
            "Do you have any volunteer experience? (yes/no)",
            "Do you have any certifications or courses related to the job? (yes/no)",
            "Would you like tips on improving your education section? (yes/no)"
        ]
        self.responses = {
            "work_experience_yes": "Great! Be sure to highlight your achievements and responsibilities at your previous jobs.",
            "work_experience_no": "No problem! Focus on your skills, education, and volunteer work if any.",
            "volunteer_experience_yes": "Excellent! Volunteer work can show commitment and community involvement, include it in your resume.",
            "volunteer_experience_no": "That's okay! Consider looking for volunteer opportunities to bolster your resume.",
            "certifications_yes": "Be sure to list any certifications that are relevant to the job you're applying for.",
            "certifications_no": "Consider pursuing certifications that are related to your field to make your resume stand out.",
            "education_tips_yes": "Make sure your education section lists your degree(s), relevant coursework, and any honors or awards.",
            "education_tips_no": "Alright! Let me know if you need help with other sections.",
        }
        self.current_question = 0
        self.responses_given = {}

    def get_next_question(self):
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]
        else:
            return "All questions completed."

    def process_answer(self, answer):
        if self.current_question == 0:
            key = "work_experience_" + answer
        elif self.current_question == 1:
            key = "volunteer_experience_" + answer
        elif self.current_question == 2:
            key = "certifications_" + answer
        elif self.current_question == 3:
            key = "education_tips_" + answer
        else:
            return "No more questions."
        
        self.responses_given[self.current_question] = self.responses.get(key, "Invalid response.")
        self.current_question += 1
        return self.responses_given[self.current_question - 1]

# Initialize the bot
bot = ResumeHelpBot()

# Flask routes
@app.route('/')
def index():
    question = bot.get_next_question()
    return render_template('index.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer'].strip().lower()
    response = bot.process_answer(answer)
    next_question = bot.get_next_question()
    return render_template('index.html', question=next_question, response=response)

if __name__ == '__main__':
    app.run(debug=True)
