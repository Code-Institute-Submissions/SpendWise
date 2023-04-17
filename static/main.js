
const messages = document.getElementById("messages");


function removeText(){
    setTimeout(300);
    messages.classList.add("hide");
}


setTimeout(removeText, 5000);

