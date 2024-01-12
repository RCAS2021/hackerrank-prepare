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

function getMaxLessThanK(n, k){
    let max = 0;
    for(let a = 1; a <= n; a++){
        for(let b = a + 1; b <= n; b++){
            let bitAnd = a&b
            if(max < bitAnd && bitAnd < k ){
                max = bitAnd;
            }
        }
    }
    return max;
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}

//bitwise operators https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND