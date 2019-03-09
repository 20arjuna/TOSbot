chrome.tabs.getSelected(null,function(tab) {
    var tablink = tab.url;
    var site = tablink.substring(tablink.indexOf(":") + 3, tablink.indexOf("/"))
    document.getElementById("sitename").innerHTML = tablink;
})
