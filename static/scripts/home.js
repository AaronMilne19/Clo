var titles = document.getElementsByClassName('mag-title');
var infoBox = document.getElementById('mainbox');

if (screen.width <= 575) {
    infoBox.scrollIntoView(alignToTop = true);
}

for (const title of titles) {
    if ("/" + title.id + "/" === window.location.pathname) {
        title.classList.add("yellow");
    }
}
