

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
async function predictCareer(answers) {
    console.log(answers)

    //se nd response to flask app and get career choice
    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers: answers })
    });
    const result = await response.text();
    document.querySelector(".question h2").textContent = 'Predicted Career: ' + result;

    //hide the buttons for now
    nextPageButton.style.display = "none";
    nextPageButton2.style.display = "none"; 
    
            //const result = decision_tree.predict(answers);  // Use the JavaScript model to predict
    //document.getElementById("nextPageButton").style.display = "none";
    //document.getElementById("nextPageButton2").style.display = "none";
    //document.querySelector(".question h2").textContent = "Your suitable career path is: " + result;
}

// Handle Yes/No button clicks
function answerQuestion(answer) {
    userAnswers.push(answer);  // Store the answer (1 or 0)
    currentQuestion++;  // Move to the next question
    displayQuestion();  // Display the next question
}

const homeButton = document.querySelector(".HomeButton");
homeButton.addEventListener('click', function() {
    location.reload();
});
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