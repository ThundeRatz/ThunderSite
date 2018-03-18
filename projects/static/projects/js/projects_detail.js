$(document).ready(function() {
    $('#contact-button').on('click', function() {
        $("html, body").animate({ scrollTop: $(document).height()-$(window).height() }, 1000);
    })

    $('#project-images-w2').slick({
        infinite: false,
        speed: 500,
        cssEase: 'linear',
        slidesToShow: 3,
        slidesToScroll: 1,

        respondTo: 'min',
        responsive: [{
            breakpoint: 1000,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 670,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            },
        }],
    });

    // Start with typography on top
    var $container = $('html, body'),
        $scrollTo = $('.typography');

    $container.scrollTop(
        $scrollTo.offset().top - $container.offset().top + $container.scrollTop() - 10
    );
})
