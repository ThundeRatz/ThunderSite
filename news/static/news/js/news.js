$('document').ready(function() {
    var p = $('.body-image').parent()
    p.wrap('<div class="images-w1 mx-auto"></div>')
    p.addClass('images-w2')
    $('.body-image').each(function() {
        var url = $(this).attr('src')
        $(this).wrap('<div><a href="' + url + '" data-lightbox="news-gallery" data-title="."><div class="image z-depth-1" style="background-image: url(' + url + ');"></div></a></div>')
        $(this).remove();
    })

    $('.images-w2').slick({
        infinite: false,
        speed: 500,
        cssEase: 'linear',
        slidesToShow: 3,
        slidesToScroll: 1,

        respondTo: 'min',
        responsive: [{
            breakpoint: 800,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 600,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            },
        }],
    });
})
