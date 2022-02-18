var acc = document.getElementsByClassName("menuelement");
var about = document.getElementById("aboutclo")
var login_element = document.getElementById("login_element")
var membership_not_auth__element = document.getElementById("membership_not_authenticated")
var ask_to_login_txt = document.getElementById("ask_to_login_after_membership_clicked")
var openedElement = null;

if(ask_to_login_txt) { //check if not null i.e. the user is logged in
  ask_to_login_txt.style.display = "none"; //hide the message when the login panel is closed
}
about.style.maxHeight = about.scrollHeight + 'px';
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var thisPanel = this.nextElementSibling;

    if (openedElement == this) {// clicking on the menu element whose hidden panel is open

      if(ask_to_login_txt){ //check if not null i.e. the user is logged in
              ask_to_login_txt.style.display = "none"; //hide the message when the login panel is closed
              // by opening another panel
      }

      thisPanel.style.maxHeight = null;
      about.style.maxHeight = about.scrollHeight + 'px';
      openedElement = null;
    }

    else if (openedElement) {// clicking on some menu element while another element has its hidden panel open

      if (this == membership_not_auth__element){
        var openedPanel = openedElement.nextElementSibling;
        openedPanel.style.maxHeight = null;
        var loginPanel = login_element.nextElementSibling
        ask_to_login_txt.style.display = "block";
        loginPanel.style.maxHeight = loginPanel.scrollHeight + "px";
        openedElement = login_element;
      }
      else {
        if(ask_to_login_txt){ //check if not null i.e. the user is logged in
                ask_to_login_txt.style.display = "none"; //hide the message when the login panel is closed
                // by opening another panel
        }
        var openedPanel = openedElement.nextElementSibling;
        openedPanel.style.maxHeight = null;
        thisPanel.style.maxHeight = thisPanel.scrollHeight + "px";
        openedElement = this;
      }


    }

    else {//none of the hidden panels are open and therefore About Clo is visible

      if(this == membership_not_auth__element){
        about.style.maxHeight = 0;
        var loginPanel = login_element.nextElementSibling
        ask_to_login_txt.style.display = "block";
        loginPanel.style.maxHeight = loginPanel.scrollHeight + "px";
        openedElement = login_element;
      }
      else {
        thisPanel.style.maxHeight = thisPanel.scrollHeight + "px";
        about.style.maxHeight = 0;
        openedElement = this;
      }



    }
  });
}