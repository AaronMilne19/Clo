/*Commented out - underline active element functionally (without reset when Membership menu is closed!)*/


var acc = document.getElementsByClassName("membership_element");
var i;
var openedMembershipElement = null;
var membership_outer_hidden_panel = document.getElementById("membership_outer_hidden_panel")


for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var thisMembershipPanel = this.nextElementSibling;

        if (openedMembershipElement == this){
            thisMembershipPanel.style.maxHeight = null;
            // this.style.textDecoration = "none"
            openedMembershipElement = null;
        }

        else if (openedMembershipElement){
            var openedMembershipPanel = openedMembershipElement.nextElementSibling;
            openedMembershipPanel.style.maxHeight = null;
            // openedMembershipElement.style.textDecoration = "none";

            // this.style.textDecoration = "underline";
            thisMembershipPanel.style.maxHeight = thisMembershipPanel.scrollHeight + "px"
            openedMembershipElement = this;
            membership_outer_hidden_panel.style.maxHeight = "max-content"

        }

        else{
            // this.style.textDecoration = "underline";
            thisMembershipPanel.style.maxHeight = thisMembershipPanel.scrollHeight + "px"
            openedMembershipElement = this;
            membership_outer_hidden_panel.style.maxHeight = "max-content"


        }

    })
}