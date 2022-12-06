function get_number(n) {
    var str = n + '';
    str = str.replace(',', '.');
    var num = eval(str);
    if(typeof(num) == 'undefined') {
        return 0;
    }
    return num;
}

/*
* Input: <Number>
* Output: <Number.#>
*/
function round(n, d) {
    var m = Math.pow(10, d);
    var num = Math.round(n * m) / m;
    return num;
}
function round_2d(n) {
    var m = 100;
    var num = Math.round(n * m) / m;
    return num;
}