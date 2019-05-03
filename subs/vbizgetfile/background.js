chrome.browserAction.onClicked.addListener(function() {
  var autovbiz = false;
  chrome.storage.sync.get(['autovbiz'], function(items) {
    if (!items.autovbiz) {
      autovbiz = false
      chrome.storage.sync.set({
        'autovbiz': '0',
      }, function() {});
    } else {
      autovbiz = items.autovbiz == '0' ? false : true;
    }

    if (!autovbiz) {
      chrome.storage.sync.set({
        'autovbiz': '1',
      }, function() {
        autovbiz = true;
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
    } else {
      chrome.storage.sync.set({
        'autovbiz': '0',
      }, function() {
        autovbiz = false;
      });
    }

  });
});

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

  if (changeInfo.status == 'complete' && tab.url.includes('https://bocaodientu.dkkd.gov.vn')) {
    var autovbiz = false;
    chrome.storage.sync.get(['autovbiz'], function(items) {
      autovbiz = items.autovbiz == '0' ? false : true;
      console.log('updated' + autovbiz);
      if (autovbiz) {
        chrome.tabs.sendMessage(tabId, {
          command: "auto"
        }, function(response) {
          console.log("Hey hey auto!")
        });
      }
    });

  }
});
