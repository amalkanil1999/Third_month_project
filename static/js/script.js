;jQuery.noConflict();
(function($) {
    document.addEventListener("DOMContentLoaded", function () {
        var owl = $('#image-slider');
        owl.owlCarousel({
            items: 1,               // Display one item at a time
            loop: true,             // Infinite loop
            margin: 250,              // Set margin to 0
        });
    })
})(jQuery);