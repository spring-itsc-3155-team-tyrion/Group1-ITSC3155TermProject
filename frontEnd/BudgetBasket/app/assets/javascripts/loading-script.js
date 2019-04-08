$(window).on('load', function(){
    loading();
    setTimeout(notLoading, 3000);
});


function loading(){
    $('#recipes-table').addClass("hidden");
    $('nav').css("opacity", "0.25");
    $('#recipes-table').css("opacity", "0.25");
    $('.next-step-btn').css("opacity", "0.25");
    $('.loader').css("opacity", "1 !important");
    
}

function notLoading(){
    $('.loader').addClass("hidden");
    $('nav').css("opacity", "1");
    $('#recipes-table').css("opacity", "1");
    $('.next-step-btn').css("opacity", "1");
    setTimeout($('#recipes-table').removeClass("hidden"), 3000);
}
