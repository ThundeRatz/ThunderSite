$(document).ready(function() {
    $('#contact-button').on('click', function() {
        $("html, body").animate({ scrollTop: $(document).height()-$(window).height() }, 1000);
    })

    $('#project-images-w2').slick({
        infinite: false,
        speed: 500,
        cssEase: 'linear',
        // variableWidth: true,
        slidesToShow: 3,
        slidesToScroll: 1,
    });

    // Start with typography on top
    var $container = $('html, body'),
        $scrollTo = $('.title');

    $container.scrollTop(
        $scrollTo.offset().top - $container.offset().top + $container.scrollTop() - 10
    );
})
