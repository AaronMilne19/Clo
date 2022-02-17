var acc = document.getElementsByClassName("menuelement");
var about = document.getElementById("aboutclo")
var openedElement = null;
about.style.maxHeight = about.scrollHeight + 'px';
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var thisPanel = this.nextElementSibling;
    if (openedElement == this) {
      thisPanel.style.maxHeight = null;
      about.style.maxHeight = about.scrollHeight + 'px';
      openedElement = null;
    }

    else if (openedElement) {
      var openedPanel = openedElement.nextElementSibling;
      openedPanel.style.maxHeight = null;
      thisPanel.style.maxHeight = thisPanel.scrollHeight + "px";
      openedElement = this;
    }

    else {
      thisPanel.style.maxHeight = thisPanel.scrollHeight + "px";
      about.style.maxHeight = 0;
      openedElement = this;


    }
  });
}