var button = document.createElement('button');
button.id = 'btn';
let num = 0;
button.innerHTML = num;
button.style.background = '#FFF';
document.body.appendChild(button)
button.addEventListener("click", function() {
    num += 1;
    button.innerHTML = num;
});