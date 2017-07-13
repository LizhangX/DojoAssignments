var express = require('express');
var mongoose = require('mongoose');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/static"));

app.set('view engine', 'ejs');
app.set('views', __dirname + "/client/views");

//mongoose

require('./server/config/mongoose.js');
require('./server/config/routes.js')(app);




app.listen(8000, function() {
    console.log('App listening on port 8000!');
});