(function($) {
    'use strict';
    $(function() {
<<<<<<< HEAD
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
=======
        $('.cancel-link').click(function(e) {
            e.preventDefault();
            window.history.back();
>>>>>>> ac31e32ee02d5e8dd84ebc466c678a256a789bf9
        });
    });
})(django.jQuery);
