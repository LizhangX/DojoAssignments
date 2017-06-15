$(function () {
    var string = '';
    for (var i = 1; i <= 151; i++) {
        string = string + '<img id="' + i + '" src="http://pokeapi.co/media/img/' + i + '.png">';
    };
    $('#left').append(string);

    $(document).on ('click','img', function(event) {
        // event.stopPropagation();
        var ID = $(this).attr('id');
        var pic = "http://pokeapi.co/api/v1/pokemon/" + ID + '/';
        $.get(pic, function (res) {
            console.log(res);
                var name = res.name;
                var type = res.types;
                var height = res.height;
                var weight = res.weight;
                $('#right').empty();
                $('#right').append('<h1>' + name + '</h1>');
                $('#right').append('<img src=\"http://pokeapi.co/media/img/' + ID + '.png\">')
                $('#right').append('<p>types</p><ul><li>' + type[0].name + '</li></ul>');
                $('#right').append('<p>height</p><p>' + height + "</p>");
                $('#right').append('<p>weight</p><p>' + weight + "</p>");
            },
            "json"
        );
    })
});