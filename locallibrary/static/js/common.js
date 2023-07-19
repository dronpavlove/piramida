$(document).ready(function () {
    $("a").click(function () {
        var elementClick = $(this).attr("href");
        var destination = $(elementClick).offset().top;
        if ($.browser.safari) {
            $('body').animate({ scrollTop: destination }, 2100); //1100 - скорость
        } else {
            $('html').animate({ scrollTop: destination }, 1100);
        }
        return false; 
    });
});