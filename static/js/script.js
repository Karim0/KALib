$(document).ready(function () {
    $('.header__burger').click(function (ever) {
        $('.header__burger, .header__menu').toggleClass('active');
        $('body').toggleClass('lock')
    });

    // $('.header__link.dropbtn, .dropdown-content').hover(function (ever) {
    //     $('.dropdown-content').toggleClass('visible')
    // })
    $('.dropdown__menu').hover(function (ever) {
        $('.dropdown-content').toggleClass('visible')
    })
});