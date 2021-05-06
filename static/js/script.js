$(document).ready(function () {
    // Side Nav Right
    $('.sidenav').sidenav({ edge: "right" });
    // DropDown button
    $('.dropdown-trigger').dropdown();
    // Tool Tip
    $('.tooltipped').tooltip();
    // Delete recipe modal // Recipe Page
    $('.modal').modal();
    // Paralax Home page
    $('.parallax').parallax();
    // Carousel Home page
    $('.carousel').carousel();
    // Slider Home Page
    $('.slider').slider();

    // Scroll down on Recipes Page
    $(".down").click(function () {
        $('html, body').animate({
            scrollTop: $(".up").offset().top
        }, 2000);
    });
 
    // Collapsible Accordion // 
     $('.collapsible').collapsible();

     // Material Box Recipe Page
     $('.materialboxed').materialbox();
});
