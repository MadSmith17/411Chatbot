import * as decision_tree from './decision_tree_model.js';

document.addEventListener("DOMContentLoaded", (event) => {
// Array of questions to ask the user
const questions = [
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
];

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