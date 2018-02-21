$(document).ready(function() {
    $('#fullpage').fullpage({
        navigation: true,
        controlArrows: false,
        responsiveWidth: 768    ,
        // keyboardScrolling: false,

        onLeave: function(index, nextIndex, direction) {
            $('#menu'+index).removeClass('active');
            $('#menu'+nextIndex).addClass('active');

            if (index === 1) {
                $('#header').fadeIn();
                $('#fp-nav ul li a span, .fp-slidesNav ul li a span').css('background', '#1C1C42');
            } else if (nextIndex === 1) {
                $('#header').fadeOut();
                $('#fp-nav ul li a span, .fp-slidesNav ul li a span').css('background', '#FFFFFF');
            }

            if (index === 3 && nextIndex !== 1) {
                $('#fp-nav ul li a span, .fp-slidesNav ul li a span').css('background', '#1C1C42');
            } else if (nextIndex === 3) {
                $('#fp-nav ul li a span, .fp-slidesNav ul li a span').css('background', '#FFFFFF');
            }
        }
    });

    var v = new Vivus('thunderlogo', {
        duration: 140,
        type: 'sync',
        start: 'manual',
    }, function (obj) {
        obj.el.classList.add('finished');
        $('#section-buttons').removeClass('hidden');
    });

    setTimeout(function() {
        v.play();
    }, 300);

    $('#thunderlogo').on('click', function() {
        $(this).removeClass('finished');
        $('#section-buttons').addClass('hidden');
        v.stop().reset();
        setTimeout(function() {
            v.play();
        }, 1000);
    })

    $('#sponsors-gold-w2').slick({
        accessibility: false,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 3000,
        cssEase: 'linear',
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        speed: 300,
        pauseOnHover: true,
        pauseOnFocus: true,

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
    })

    $('#sponsors-silver-w2').slick({
        accessibility: false,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 3000,
        cssEase: 'linear',
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        speed: 300,
        pauseOnHover: true,
        pauseOnFocus: true,

        respondTo: 'min',
        responsive: [{
            breakpoint: 1010,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 760,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 510,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            },
        }],
    });

    $('#sponsors-bronze-w2').slick({
        accessibility: false,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 3000,
        cssEase: 'linear',
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        speed: 300,
        pauseOnHover: true,
        pauseOnFocus: true,

        respondTo: 'min',
        responsive: [{
            breakpoint: 1260,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 1010,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 760,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            },
        }, {
            breakpoint: 510,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            },
        }],
    });

    $('#header').hide();

    $('.navbar-brand').on('click', function() {
        $.fn.fullpage.moveTo(1);
    });

    $('#menu2, #menu2-start').on('click', function() {
        $.fn.fullpage.moveTo(2);
    });

    $('#menu3, #menu3-start').on('click', function() {
        $.fn.fullpage.moveTo(3, 0);
    });

    $('#menu4, #menu4-start').on('click', function() {
        $.fn.fullpage.moveTo(4);
    });

    $('#menu5, #menu5-start').on('click', function() {
        $.fn.fullpage.moveTo(5);
    });

    $('#menu6, #menu6-start').on('click', function() {
        $.fn.fullpage.moveTo(6);
    });
});

$(document).on('keydown', function(event) {
    if (event.keyCode == 9) {   //tab pressed
        event.preventDefault(); // stops its action
    }
});
