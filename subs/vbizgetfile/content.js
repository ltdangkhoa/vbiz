chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  var list = []
  $("input").each(function() {
    if ($(this).attr('src') == '../../Img/pdf.png') {
      list.push($(this).attr('id'))
    }
  });
  test(list);
  sendResponse({
    result: "success"
  });
});

function test(list) {
  // alert(list)
  // alert('hi')
  setTimeout(function() {
    if (list.length > 0) {
      var el = list.pop()
      $('#' + el).click();
      test(list);
    }

  }, 1000);
}
