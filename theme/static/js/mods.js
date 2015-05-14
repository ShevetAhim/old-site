$( document ).ready(function() {
    // Set items in rows to the same height
    items = $('.row-item');
    maxHeight = Math.max.apply(
    Math, items.map(function() {
        return $(this).height();
    }).get());
    items.height(maxHeight);
});
