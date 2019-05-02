chrome.browserAction.onClicked.addListener(function() {
  autovbiz = !autovbiz;
  chrome.tabs.query({
    active: true,
    currentWindow: true
  }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {
      command: "click"
    }, function(response) {

    });
  });
});

var autovbiz = false;
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  console.log('autovbiz' + autovbiz);
  if (changeInfo.status == 'complete') {
    if (tab.url.includes('https://bocaodientu.dkkd.gov.vn') && autovbiz) {
      chrome.tabs.sendMessage(tabId, {
        command: "auto"
      }, function(response) {
        console.log("Hey hey auto!")
      });
    }
  }
});
