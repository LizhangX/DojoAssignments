$(document).ready(function () {
    $('.header h1').click(function () {
        $('.firstBox img').hide();
    });
    $('.header ul li:first-child').click(function () {
        $('.firstBox img').show();
    });
    $('.header ul li:nth-child(2)').click(function () {
        $('.firstBox img').toggle();
    });
    $('.header ul li:nth-child(3)').click(function () {
        $('.firstBox img').slideUp();
    });
    $('.header ul li:nth-child(4)').click(function () {
        $('.firstBox img').slideDown();
    });
    $('.subBox:nth-child(2)').click(function () {
        $('.firstBox img').fadeIn();
    });
    $('.subBox:nth-child(1)').click(function () {
        $('.firstBox img').fadeOut();
    });
    $('.wrapper').addClass('wot');
    $('.subBox h2').before('<h2>hello</h2>');
    $('.subBox h2').after('<h2>yeah</h2>');
    $('.subBox p').append('lol');
    $('.subBox button').html('<button>clickme</button>');
    $('.subBox').attr('room','moment');
    $('.header ul li:nth-child(5)').click(function() {
        var a = $('.box input').val();
        alert(a);
    });
    $('.subBox2:first-child').click(function() {
        var a = $('.subBox2:nth-child(3) p').text();
        alert(a);
    });






    $('.subBox2:nth-child(2)').click(function() {
        $('div').data("name","value");
        var a = $('div').data('name');
        alert(a);
    });
});