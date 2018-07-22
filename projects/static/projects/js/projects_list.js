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
    $('.card-img-top').lazy();

    var categories = ['autonomo', 'sumo', 'hockey', 'combate'];
    var category = GetURLParameter('cat');

    if ($.inArray(category, categories) === -1)
        category = undefined;

    if (category) {
        $('a[data-cat="'+category+'"]').addClass('active');
        $('#project-row > div').each(function() {
            ($(this).data('cat') == category) ? $(this).show() : $(this).hide();
        });
    } else {
        $('a[data-cat="all"').addClass('active');
    }

    window.history.replaceState("projects_hist", "ThundeRatz | Projects", "/projects/robots/");

    $('#categories-menu').on('click', 'a', function() {
        var cat = $(this).data('cat');
        $('a[data-cat]').removeClass('active');
        $(this).addClass('active');

        $('#project-row > div').each(function() {
            if (cat != 'all') {
                ($(this).data('cat') == cat) ? $(this).show() : $(this).hide();
            } else {
                $(this).show();
            }
        });
    });
})
