$(document).ready(function() {
    $('#fullpage').fullpage({
        navigation: true,
        controlArrows: false,
        responsiveWidth: 768,
        keyboardScrolling: false,

        onLeave: function(index, nextIndex, direction) {
            $('#menu'+index).removeClass('active');
            $('#menu'+nextIndex).addClass('active');

            if (index === 1) {
                $('#header').fadeIn();
                $('#section-buttons').addClass('hidden');
                $('#fp-nav ul li a span, .fp-slidesNav ul li a span').css('background', '#1C1C42');
            } else if (nextIndex === 1) {
                $('#header').fadeOut();
                $('#section-buttons').removeClass('hidden');
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
        slidesToScroll: 3,
        speed: 300,
        pauseOnHover: false,
        pauseOnFocus: false,

        respondTo: 'min',
        responsive: [{
            breakpoint: 1000,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
            },
        }, {
            breakpoint: 670,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1,
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
        slidesToShow: 5,
        slidesToScroll: 5,
        speed: 300,
        pauseOnHover: false,
        pauseOnFocus: false,

        respondTo: 'min',
        responsive: [{
            breakpoint: 1260,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
            },
        }, {
            breakpoint: 1010,
            settings: {
                slidesToScroll: 3,
                slidesToShow: 3,
            },
        }, {
            breakpoint: 760,
            settings: {
                slidesToScroll: 2,
                slidesToShow: 2,
            },
        }, {
            breakpoint: 510,
            settings: {
                slidesToScroll: 1,
                slidesToShow: 1,
            },
        }],
    })

    // this is for the first fadeout
    setTimeout(function(){
        $('.slick-slide').addClass('opacidown');
    }, 2700);
    // all the rest of the transitions after the initial
    $('#sponsors-gold-w2').on('afterChange', function(event, slick, currentSlide, nextSlide){
        $('#sponsors-gold-w2 .slick-slide').removeClass('opacidown');
        setTimeout(function(){
            $('#sponsors-gold-w2 .slick-slide').addClass('opacidown');
        }, 2700);
    });

    $('#sponsors-silver-w2').on('afterChange', function(event, slick, currentSlide, nextSlide){
        $('#sponsors-silver-w2 .slick-slide').removeClass('opacidown');
        setTimeout(function(){
            $('#sponsors-silver-w2 .slick-slide').addClass('opacidown');
        }, 2700);
    });

    $('#header').hide();

    $('.navbar-brand, #menu1').click(function() {
        $.fn.fullpage.moveTo(1);
    });

    $('#menu2, #menu2-start').click(function() {
        $.fn.fullpage.moveTo(2);
    });

    $('#menu3, #menu3-start').click(function() {
        $.fn.fullpage.moveTo(3, 0);
    });

    $('#menu4, #menu4-start').click(function() {
        $.fn.fullpage.moveTo(4);
    });

    $('#menu5, #menu5-start').click(function() {
        $.fn.fullpage.moveTo(5);
    });

    $('#menu6, #menu6-start').click(function() {
        $.fn.fullpage.moveTo(6);
    });
});

$(document).on('keydown', function(event) {
    if (event.keyCode == 9) {   //tab pressed
        event.preventDefault(); // stops its action
    }
});
