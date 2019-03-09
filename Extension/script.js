chrome.tabs.getSelected(null,function(tab) {
    var tablink = new URL(tab.url);
    var site = tablink.hostname;
    document.getElementById("sitename").innerHTML = site + " may be trying to pull a fast one on you!";
})

function loading()
{
  console.log("Loading baby");
}

document.getElementById('analyze').addEventListener('click', loading)
