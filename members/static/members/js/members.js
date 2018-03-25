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
    // fixSizes();
    $('.flip, .front, .back').addClass('h-100');

    var areas = ['EL', 'MC', 'CP', 'DM', 'AF'];
    var area = GetURLParameter('area');

    if ($.inArray(area, areas) === -1)
        area = undefined;

    if (area) {
        $('a[data-area="'+area+'"]').addClass('active');
        $('#member-row > div').each(function() {
            ($(this).data('area') == area) ? $(this).show() : $(this).hide();
        });
    } else {
        $('a[data-area="all"').addClass('active');
    }

    window.history.replaceState("members_hist", "ThundeRatz | Membros", "/members/");

    $('#areas-menu').on('click', 'a', function() {
        var area = $(this).data('area');
        $('a[data-area]').removeClass('active');
        $(this).addClass('active');

        $('#member-row > div').each(function() {
            if (area != 'all') {
                ($(this).data('area') == area) ? $(this).show() : $(this).hide();
            } else {
                $(this).show();
            }
        });
    });

});
