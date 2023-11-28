const canvas = document.querySelector("canvas"),
toolBtns = document.querySelectorAll(".tool"),
ctx = canvas.getContext("2d");

let isDrawing = false,
brushWidth = 5;

window.addEventListener("load", () => {
// setting canvas width/height..offsetwidth/heighz returns viawable width and height of an element
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
});

const startDraw = () => {
    isDrawing = true;
    ctx.beginPath(); // creating new path to draw
    ctx.lineWidth = brushWidth;
};

const drawing = (e) => {
    if(!isDrawing) return; //isDrawing is false return from here
    ctx.lineTo(e.offsetX, e.offsetY); // creating line according to the mouse pointer
    ctx.stroke();   //  drawind/filling line with color
};

toolBtns.forEach(btn => {
    btn.addEventListener("click", () =>{ // adding click event to all tool option
        console.log(btn.id);
    });
});

canvas.addEventListener("mousedown", startDraw);
canvas.addEventListener("mousemove", drawing);
canvas.addEventListener("mouseup", () => isDrawing = false);