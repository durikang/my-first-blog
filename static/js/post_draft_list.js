$(document).ready(function () {
    $('table .boarder').click(function () {
        window.location = $(this).data('href');
        return false;
    });
});
