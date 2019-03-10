var site = "";
chrome.tabs.getSelected(null,function(tab) {
    var tablink = new URL(tab.url);
    site = tablink.hostname;
    document.getElementById("sitename").innerHTML = site + " may be trying to pull a fast one on you!";
});
jQuery.support.cors = true;
const xhr = new XMLHttpRequest();
xhr.open('POST', 'http://localhost:5000/');
xhr.send(site);

// function loading()
// {
//   console.log("Loading baby");
// }
//
// document.getElementById("analyze").addEventListener('click', loading);
