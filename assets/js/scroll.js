$(document).ready(function(){
    $(".carousel-testimony").owlCarousel({
      items: 3,              // Show 3 items at a time
      margin: 20,            // Add some margin between items
      loop: true,            // Enable looping of carousel
      autoplay: true,        // Enable auto-scrolling
      autoplayTimeout: 5000, // Scroll every 5 seconds
      autoplayHoverPause: true, // Pause on hover
      nav: true,             // Enable navigation buttons
      dots: true,            // Enable dots
      responsive: {
        0: {
          items: 1          // 1 item for small screens
        },
        600: {
          items: 2          // 2 items for medium screens
        },
        1000: {
          items: 3          // 3 items for large screens
        }
      }
    });
  });
  