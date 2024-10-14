// Select the button using its ID
const nextPageButton = document.getElementById('nextPageButton');
const nextPageButton2 = document.getElementById('nextPageButton2');
// Add a click event listener to the button
nextPageButton.addEventListener('click', function() {
    // Add the fade-out class to the body
    document.body.classList.add('fade-out');
    
    // Wait for the transition to complete before redirecting
    setTimeout(function() {
        window.location.href = 'newpage.html'; // Replace with your desired URL
    }, 1000); // Delay matches the CSS transition duration (1 second)
});

nextPageButton2.addEventListener('click', function() {
    // Add the fade-out class to the body
    document.body.classList.add('fade-out');
    
    // Wait for the transition to complete before redirecting
    setTimeout(function() {
        window.location.href = 'option2.html'; // Replace with your desired URL
    }, 1000); // Delay matches the CSS transition duration (1 second)
});