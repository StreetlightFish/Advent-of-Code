const fs = require('fs');
// First I want to read the file
fs.readFile('input.txt', function read(err, data) {
    if (err) {
        throw err;
    }
    const content = data;

    // Invoke the next step here however you like
    console.log(content);   // Put all of the code here (not the best solution)
    processFile(content);   // Or put the next step in a function and invoke it
});

function processFile(content) {
    console.log(content);
}
