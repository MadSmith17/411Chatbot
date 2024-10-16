# Basic Decision Tree Chatbot for Resume Help

class ResumeHelpBot:
    def __init__(self):
        self.questions = {
            "q1": "Do you have work experience? (yes/no)",
            "q2": "Do you have any volunteer experience? (yes/no)",
            "q3": "Do you have any certifications or courses related to the job? (yes/no)",
            "q4": "Would you like tips on improving your education section? (yes/no)",
        }
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

    def ask_question(self, question_key):
        # Ask user a question and return the response
        print(self.questions[question_key])
        return input().strip().lower()

    def run(self):
        print("Welcome to the Resume Help Bot!")
        
        # Work experience question
        response = self.ask_question("q1")
        if response == "yes":
            print(self.responses["work_experience_yes"])
        else:
            print(self.responses["work_experience_no"])
        
        # Volunteer experience question
        response = self.ask_question("q2")
        if response == "yes":
            print(self.responses["volunteer_experience_yes"])
        else:
            print(self.responses["volunteer_experience_no"])
        
        # Certifications question
        response = self.ask_question("q3")
        if response == "yes":
            print(self.responses["certifications_yes"])
        else:
            print(self.responses["certifications_no"])
        
        # Education tips question
        response = self.ask_question("q4")
        if response == "yes":
            print(self.responses["education_tips_yes"])
        else:
            print(self.responses["education_tips_no"])
        
        print("Thank you for using the Resume Help Bot!")

# Run the bot
if __name__ == "__main__":
    bot = ResumeHelpBot()
    bot.run()
