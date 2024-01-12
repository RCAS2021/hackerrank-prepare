'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', 
     * followed by one or more letters.
     */
    var re = /^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$/; // ^ -> at the beginning, (Mr|...) -> One or(|) another, \. -> contains ., [a-zA-z] -> contains a lowercase or uppercase character between a-z , +$ -> needs to have at least one time at the end
    //var re = /^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)\w+$/; (Mr\.) -> if the other prefixes didn't also have the '.' at the end, it would be necessary to use this, ex: (Mr. or Ms(without the dot)), \w -> alphanumeric character including _ (underscore), this would fail if the test had for example: Mr.8, as it also matches with (0-9).
    
    /*
     * Do not remove the return statement
     */
    return re;
}


function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(!!s.match(re));
}

//regular expressions https://www.hackerrank.com/challenges/js10-regexp-1/topics