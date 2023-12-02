const canvas = document.querySelector("canvas"),
toolBtns = document.querySelectorAll(".tool"),
fillColor = document.querySelector("#fill-color"),
sizeSlider = document.querySelector("#size-slider"),
colorBtns = document.querySelectorAll(".color .option-canvas"),
colorPicker = document.querySelector("#color-picker"),
clearCanvas= document.querySelector(".clear-canvas"),
ctx = canvas.getContext("2d");

// global variables with default value

let prevMouseX, prevMouseY, snapshot,
isDrawing = false,
selectedTool = "brush",
brushWidth = 5;
selectedColor = "#2a2a2aba";

window.addEventListener("load", () => {
// setting canvas width/height..offsetwidth/heighz returns viawable width and height of an element
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
});

const drawRect = (e) =>  {
// if fillColor is not checked draw a rect with border else draw rect with background
    if(!fillColor.checked){
    // creating acording to mouse pointer
        return ctx.strokeRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX, prevMouseY - e.offsetY);
    };
    ctx.fillRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX, prevMouseY - e.offsetY);
}

const drawTriangle = (e) => {
    ctx.beginPath(); // creating new path
    ctx.moveTo(prevMouseX, prevMouseY); //moving triangle to the mouse pointer
    ctx.lineTo(e.offsetX, e.offsetY);   // creating firsl line acording t o mouse pointer
    ctx.lineTo(prevMouseX * 2 - e.offsetX, e.offsetY);
    ctx.closePath();
    fillColor.checked ? ctx.fill() : ctx.stroke();
};

const drawCircle = (e) => {
    ctx.beginPath(); // creating new path to the circle
    //  getting radius for circle according to the mouse pointer
     let radius = Math.sqrt(Math.pow((prevMouseX - e.offsetX), 2) + Math.pow((prevMouseY - e.offsetY), 2));
     ctx.arc(prevMouseX, prevMouseY, radius, 0, 2 * Math.PI);
     fillColor.checked ? ctx.fill() : ctx.stroke();     // if fillColor is checked fill circle else draw border circle
};

const startDraw = (e) => {
    isDrawing = true;
    prevMouseX = e.offsetX;     // passing current mouseX position as prevMouseX value
    prevMouseY = e.offsetY;     // passing current mouseY position as prevMouseY value
    ctx.beginPath(); // creating new path to draw
    ctx.lineWidth = brushWidth;
    ctx.strokeStyle = selectedColor;    // passing selectedColor as stroke style
    ctx.fillStyle = selectedColor;      // passing selected color as fill style
    snapshot = ctx.getImageData(0, 0, canvas.width, canvas.height);
};

const drawing = (e) => {
    if(!isDrawing) return; //isDrawing is false return from here
    ctx.putImageData(snapshot, 0, 0);    // adding copied canvas data on to this canvas

    if(selectedTool === "brush" || selectedTool === "eraser" ){
        // if selecter tool is eraser then strokeStyle is white
        // to paint white color on canvas content else stroke color to selected color
        ctx.strokeStyle = selectedTool === "eraser" ? "#fff" : selectedColor;
        ctx.lineTo(e.offsetX, e.offsetY); // creating line according to the mouse pointer
        ctx.stroke();   //  drawind/filling line with color
    }
    else if(selectedTool === "rectangle"){
        drawRect(e);
    }
    else if(selectedTool === "circle"){
        drawCircle(e);
    }
    else{
        drawTriangle(e);
    }

};

toolBtns.forEach(btn => {
    btn.addEventListener("click", () =>{ // adding click event to all tool option
    // removing active class from the previous option and adding on current clicked option
    document.querySelector(".options-canvas .active").classList.remove("active");
    btn.classList.add("active");
    selectedTool = btn.id;
    console.log(btn.id);
    });
});

sizeSlider.addEventListener("change",() => brushWidth = sizeSlider.value);  // passing slider valua as brushSize

colorBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        // removing active class from the previous option and adding on current clicked option
        document.querySelector(".options-canvas .selected").classList.remove("selected");
        btn.classList.add("selected");
        // passing selected btn background color as selectedColor value
        selectedColor = window.getComputedStyle(btn).getPropertyValue("background-color");
    });
});

colorPicker.addEventListener("change", () => {
    // passing picked color value from color picker to last color bakground
    colorPicker.parentElement.style.background = colorPicker.value;
    colorPicker.parentElement.click();
});

clearCanvas.addEventListener("click", () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);   // clearing whole canvas
    console.log("Canvas cleared")
});

canvas.addEventListener("mousedown", startDraw);
canvas.addEventListener("mousemove", drawing);
canvas.addEventListener("mouseup", () => isDrawing = false);