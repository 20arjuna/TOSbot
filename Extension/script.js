var site = "";
chrome.tabs.getSelected(null,function(tab) {
    var tablink = new URL(tab.url);
    site = tablink.hostname;
    document.getElementById("sitename").innerHTML = site + " may be trying to pull a fast one on you!";
})


function loading()
{
  $.ajax({
       type: "POST",
       url: "/getTOS.py",
       data: { param: site }
   });
  console.log("Loading baby");
}

document.getElementById("analyze").addEventListener('click', loading);
