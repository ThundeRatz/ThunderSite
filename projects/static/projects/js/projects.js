// http://www.jquerybyexample.net/2012/06/get-url-parameters-using-jquery.html
function GetURLParameter(sParam) {
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
}

$(document).ready(function() {
    var category = GetURLParameter('cat');

    if (category) {
        $('#project-row > div').each(function() {
            ($(this).data('cat') == category) ? $(this).show() : $(this).hide();
        });
        window.history.replaceState("projects_hist", "ThundeRatz | Projects", "/projects/");
    }

    $('#project-search').on('keyup', function() {
        var val = $(this).val().toLowerCase();
        $('#project-row > div').each(function() {
            var text = $(this).data('name').toLowerCase();
            (text.indexOf(val) == 0) ? $(this).show() : $(this).hide();
        });
    });

    $('#categories-menu').on('click', 'li', function() {
        var cat = $(this).data('cat');

        $('#project-row > div').each(function() {
            if (cat) {
                ($(this).data('cat') == cat) ? $(this).show() : $(this).hide();
            } else {
                $(this).show();
            }
        });
    });

    $('#project-images-w2').slick({
        infinite: false,
        speed: 500,
        cssEase: 'linear',
        // variableWidth: true,
        slidesToShow: 3,
        slidesToScroll: 1,
    });

    $('#contact-button').on('click', function() {
        $("html, body").animate({ scrollTop: $(document).height()-$(window).height() }, 1000);
    })

    // Start with typography on top
    var $container = $('html, body'),
        $scrollTo = $('.typography');

    $container.scrollTop(
        $scrollTo.offset().top - $container.offset().top + $container.scrollTop() - 10
    );
})
