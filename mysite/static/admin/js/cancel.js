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
>>>>>>> 63dfa81123beb2cff90ef876d41f9c177fbc8155
        });
    });
})(django.jQuery);
