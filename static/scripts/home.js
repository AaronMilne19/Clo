var titles = document.getElementsByClassName('mag-title');
var infoBox = document.getElementById('mainbox');
var issuesList = document.getElementsByClassName('issue-link');


if (screen.width <= 575) {
    infoBox.scrollIntoView(alignToTop = true);
}

for (const title of titles) {
    var magId = window.location.pathname.split("/");

    if (title.id  === magId[1]) {
        title.classList.add("yellow");
    }
}

function showIssueBox(issue) {
    var issueBox = document.getElementById('IssueBox' + issue);
    issueBox.classList.add('show-issue', issue);
}

function hideIssueBox(issue) {
    var issueBox = document.getElementById('IssueBox' + issue);
    issueBox.classList.remove('show-issue');
}
