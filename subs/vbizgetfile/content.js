chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  var list = []
  $("input").each(function() {
    if ($(this).attr('src') == '../../Img/pdf.png') {
      list.push($(this).attr('id'))
    }
  });
  godownload(list);
  sendResponse({
    result: "success"
  });
});

function godownload(list) {
  setTimeout(function() {
    if (list.length > 0) {
      var el = list.pop()
      $('#' + el).click();
      godownload(list);
    } else {
      goNextPage()
    }

  }, 1000);
}

function goNextPage() {
  var pager = $("body").find('.Pager');
  var pager_table = pager.find('table');
  var pager_table_td = pager_table.find('td');

  var is_current = false;
  pager_table_td.each(function() {
    if (is_current) {
      var next_page = $(this).find('a').attr('href');
      window.location = next_page;
      return false;
    }
    var span = $(this).find('span');
    if (span.length > 0) {
      is_current = true;
    }
  });
}
