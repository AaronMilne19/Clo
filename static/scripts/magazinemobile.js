var all_issues = document.getElementById("magazine_menu_element")
var hidden_panel_issues = document.getElementById("hidden_panel_issues")
var hidden_panel_open = false;
var close_icon_issues = all_issues.lastElementChild;

all_issues.addEventListener("click", function() {
    this.classList.toggle("active");

    if(hidden_panel_open){
        hidden_panel_issues.style.maxHeight = null;
        close_icon_issues.style.opacity = "0%";
        hidden_panel_open = false;
    }
    else {
        hidden_panel_issues.style.maxHeight = hidden_panel_issues.scrollHeight + 'px';
        close_icon_issues.style.opacity = "100%";
        hidden_panel_open = true;
    }

});