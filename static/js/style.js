$(document).ready(function() {
    $('#menu-toggle, #menu > ul > li > a').click(function(e) {
        var $toggle = $(this);
        var $menu = $('#' + $(this).attr('aria-controls'));

        if ($menu.attr('aria-hidden') == 'true') {
            $('body').addClass('open');
            $menu.attr('aria-hidden', 'false');
            $toggle.attr('aria-expanded', 'true');
        }
        else if ($menu.attr('aria-hidden') == 'false') {
            $('body').removeClass('open');
            $menu.attr('aria-hidden', 'true');
            $toggle.attr('aria-expanded', 'faremove');
        }
    });
});