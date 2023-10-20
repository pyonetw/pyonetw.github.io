$('body').on('keydown', function(event) {
    var charCode = String.fromCharCode(event.which);
    if (charCode=='0') {
        $('#showcode').val('');
    }
    else {
        $('#showcode').val($('#showcode').val()+String.fromCharCode(event.which));
    }

    if ($('#showcode').val()=='SHOW') {
        $('code.python').parent().removeClass('d-none');
    }
    else {
        $('code.python').parent().addClass('d-none');
    }
});