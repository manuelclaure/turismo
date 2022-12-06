function format_big_number(n = 0) {
    if(n.trim() == "None") {
        return "0.0";
    }
    n = n.replace(',', '.');
    n = n.trim();
    var punto = n.indexOf('.') - 1;
    if(punto < 0) {
        punto = n.length() - 1;
    }
    var m = n.substring(punto + 1);
    for(var i = punto, j = 1; i >= 0; i--, j++) {
        m = n.charAt(i) + m;
        if(j % 6 == 0 && i != 0) {
            m = '\'' + m;
        }
        else if(j % 3 == 0 && i != 0) {
            m = ',' + m;
        }
    }
    return m;
}
function init_format() {
    // alert("jo");
    $('.big_number-input').each(function() {
        $(this).val(format_big_number($(this).val()));
    });
}