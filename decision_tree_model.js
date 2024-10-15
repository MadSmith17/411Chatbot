export function predict(input) {
    var var0;
    if (input[6] <= 0.5) {
        if (input[16] <= 0.5) {
            if (input[14] <= 0.5) {
                if (input[10] <= 0.5) {
                    if (input[3] <= 0.5) {
                        if (input[0] <= 0.5) {
                            var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0];
                        } else {
                            var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                        }
                    } else {
                        if (input[4] <= 0.5) {
                            var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0];
                        } else {
                            if (input[11] <= 0.5) {
                                var0 = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                            } else {
                                var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                            }
                        }
                    }
                } else {
                    if (input[5] <= 0.5) {
                        var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0];
                    } else {
                        var0 = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                    }
                }
            } else {
                if (input[5] <= 0.5) {
                    var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0];
                } else {
                    var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                }
            }
        } else {
            if (input[0] <= 0.5) {
                var0 = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
            } else {
                if (input[9] <= 0.5) {
                    var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0];
                } else {
                    var0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
                }
            }
        }
    } else {
        if (input[2] <= 0.5) {
            var0 = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        } else {
            var0 = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        }
    }


    // Define profession names corresponding to the one-hot encoded output
    const professions = [
        "Software Engineer",         // index 0
        "Data Scientist",            // index 1
        "Project Manager",           // index 2
        "Teacher",                   // index 3
        "Graphic Designer",          // index 4
        "Finance Manager",           // index 5
        "Construction Worker",       // index 6
        "Nurse",                     // index 7
        "Police Officer",            // index 8
        "Journalist",                // index 9
        "Research Scientist",        // index 10
        "Environmental Scientist",   // index 11
        "Lab Technician",            // index 12
        "Lawyer"                     // index 13
    ];

    // Find the index of the max value in var0 (which is the predicted class)
    const predictedIndex = var0.indexOf(1.0);
    
    // Return the corresponding profession
    console.log(var0)
    return professions[predictedIndex];

}
