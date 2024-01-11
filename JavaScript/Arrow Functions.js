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

/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    //Without Arrow Functions
    //for(let i = 0; i < nums.length; i++){
    //    if(nums[i] % 2 == 0){
    //        nums[i] = nums[i]*2
    //    }
    //    else
    //       nums[i] = nums[i] * 3
    //}
    //return nums

    //Using arrow functions
    return nums.map(s => s%2==0 ? s*2: s*3)
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}

//conditional ternary operator https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#conditional_ternary_operator
//map https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map