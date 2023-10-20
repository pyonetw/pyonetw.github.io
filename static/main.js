$(function() {
    var pycode = $('code.python').length;
    var cccode = $('code.cpp').length;
    var jscode = $('code.javascript').length;
    var bodyHTML = $('body').html();
    var excount = (bodyHTML.match(/ex\(\+\)/g) || []).length;
    var sumCode = pycode + cccode + jscode;
    var sumCode = sumCode == 0 ? '' : sumCode;
    $('#ex-count > a.nav-link').text(sumCode);
});

// hide menu after click menu item
$(document).on('click','.navbar-collapse',function(e) {
    if( $(e.target).is('a') && ( $(e.target).attr('class').indexOf('dropdown-toggle') == -1) ) {
        $(this).collapse('hide');
    }
});

// copy code to clipboard
// <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.7.1/clipboard.min.js"></script>
var pre = document.getElementsByTagName('pre');
for (var i = 0; i < pre.length; i++) {
    var button = document.createElement('button');
    button.className = 'btn btn-copy btn-secondary';
    button.textContent = 'Copy #' + String(i+1).padStart(3, '0');
    pre[i].insertBefore(button, pre[i].firstChild);
}
var copyCode = new Clipboard('.btn-copy', {
   	text: function (trigger) {
        var origText = $(trigger).next().text().replace(/\n\            /g, '\n');
        origText = origText.replace('\n', '');
        return origText;
    }
});