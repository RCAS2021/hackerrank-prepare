let res = document.getElementById('res');
let btn0 = document.getElementById('btn0');
let btn1 = document.getElementById('btn1');
let btnClr = document.getElementById('btnClr');
let btnSum = document.getElementById('btnSum');
let btnSub = document.getElementById('btnSub');
let btnMul = document.getElementById('btnMul');
let btnDiv = document.getElementById('btnDiv');
let btnEql = document.getElementById('btnEql');

btn0.addEventListener('click', () =>{
    res.innerHTML += 0;
});

btn1.addEventListener('click', () =>{
    res.innerHTML += 1;
});

btnClr.addEventListener('click', () =>{
   res.innerHTML = ''; 
});

btnSum.addEventListener('click', () =>{
   res.innerHTML += '+'; 
});

btnSub.addEventListener('click', () =>{
   res.innerHTML += '-'; 
});

btnMul.addEventListener('click', () =>{
   res.innerHTML += '*'; 
});

btnDiv.addEventListener('click', () =>{
   res.innerHTML += '/'; 
});

btnEql.addEventListener('click', () =>{
    let c = res.innerHTML.split(/([\+\-\*\/])/); // Splits into op1, operator, op2
    let r = Math.floor(eval(parseInt(c[0], 2)+c[1]+parseInt(c[2], 2))); //eval(parseInt(op1, base2)+operator+(parseInt(op2, base2)))
    res.innerHTML = r.toString(2); //transforms the number back to base 2
});

//eval function, parseInt(num, base) https://www.hackerrank.com/challenges/js10-binary-calculator/topics
//parseInt https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/parseInt