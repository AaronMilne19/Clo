var acc = document.getElementsByClassName("menuelement");
var about = document.getElementById("aboutclo")
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      about.style.maxHeight = about.scrollHeight + "px";



    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
      about.style.maxHeight = 0;


    }
  });
}