// $(function () {
//     for (var i = 1; i <= 151; i++) {
//         $('body').append('<img src="http://pokeapi.co/media/img/' + i + '.png">');
//     }
// });

//version2.0
$(function () {
    var string = '';
    for (var i = 1; i <= 151; i++) {
        string = string + '<img src="http://pokeapi.co/media/img/' + i + '.png">';
    };
    $('body').append(string);
});
