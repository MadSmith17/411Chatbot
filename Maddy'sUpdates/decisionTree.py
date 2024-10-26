from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Chatbot logic
class ResumeHelpBot:
    def __init__(self):
        self.current_question = 0
        self.branch = None  # Store the user’s choice

    def process_answer(self, answer):
        if self.current_question == 0:
            self.branch = answer  # Save the 'yes' or 'no' answer
            self.current_question += 1

        # Branching logic based on user input
        if self.current_question == 1:
            if self.branch == "yes":
                return redirect(url_for('coding_page'))
            elif self.branch == "no":
                return redirect(url_for('non_coding_page'))
        else:
            return "Thank you for completing the questionnaire!"

# Initialize bot
bot = ResumeHelpBot()

# Flask routes
@app.route('/')
def index():
    question = "Would you like to primarily program in your job?"
    return render_template('index.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer'].strip().lower()
    return bot.process_answer(answer)

@app.route('/coding_page')
def coding_page():
    return render_template('coding_page.html')

@app.route('/non_coding_page')
def non_coding_page():
    return render_template('non_coding_page.html')

if __name__ == '__main__':
    app.run(debug=True)
