import * as decision_tree from './decision_tree_model.js';

document.addEventListener("DOMContentLoaded", (event) => {
// Array of questions to ask the user
const questions = [
    "Do you enjoy problem-solving?",               
    "Do you prefer working with hardware over software?", 
    "Do you enjoy creating user interfaces?",        
    "Are you interested in data analysis?",               
    "Do you prefer working independently?",              
    "Are you interested in cybersecurity and protecting data?", 
    "Do you have an interest in artificial intelligence?",      
    "Do you enjoy optimizing processes and systems?",           
    "Are you interested in networking and computer systems?",     
    "Do you enjoy working directly with clients or stakeholders?" 
]


// Initialize variables to keep track of the user's progress
let currentQuestion = 0;
let userAnswers = [];


// Display the first question
function displayQuestion() {
    if (currentQuestion < questions.length) {
        document.querySelector(".question h2").textContent = questions[currentQuestion];
    } else {
        // If no more questions, calculate and display the result
        predictCareer(userAnswers);
    }
}

// Make a prediction using the decision tree in JavaScript
function predictCareer(answers) {
    console.log(answers)
    const result = decision_tree.predict(answers);  // Use the JavaScript model to predict
    document.getElementById("nextPageButton").style.display = "none";
    document.getElementById("nextPageButton2").style.display = "none";
    document.querySelector(".question h2").textContent = "Your suitable career path is: " + result;
}

// Handle Yes/No button clicks
function answerQuestion(answer) {
    userAnswers.push(answer);  // Store the answer (1 or 0)
    currentQuestion++;  // Move to the next question
    displayQuestion();  // Display the next question
}

// Select the button using its ID
const nextPageButton = document.getElementById('nextPageButton');
const nextPageButton2 = document.getElementById('nextPageButton2');
// Add a click event listener to the button
nextPageButton.addEventListener('click', function() {
    console.log('button 1 pressed');
    answerQuestion(1.0);
});

nextPageButton2.addEventListener('click', function() {
    console.log('button 0 pressed');
    answerQuestion(0.0);
});
// Start the process by showing the first question
displayQuestion();

});