var titles = document.getElementsByClassName('mag-title');
var infoBox = document.getElementById('mainbox');
var issuesList = document.getElementsByClassName('issue-link');
var issueBox = document.getElementById('IssueBox');

if (screen.width <= 575) {
    infoBox.scrollIntoView(alignToTop = true);
}

for (const title of titles) {
    if ("/" + title.id + "/" === window.location.pathname) {
        title.classList.add("yellow");
    }
}

function showIssueBox(issue) {
    issueBox.classList.add('show-issue');
    
}

function hideIssueBox() {
    issueBox.classList.remove('show-issue');
}
