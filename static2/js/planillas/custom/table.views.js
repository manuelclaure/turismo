$('.k-selectable').on('click', function() {
    $('.k-selectable').each(function() {
        $(this).css('background-color', '');
    });
    $(this).css('background-color', '#CADFF0');
}