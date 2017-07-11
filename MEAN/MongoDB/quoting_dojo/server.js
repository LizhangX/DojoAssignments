var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/static"));

app.set('view engine', 'ejs');
app.set('views', __dirname + "/views");

//mongoose
var mongoose = require('mongoose');
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/basic_mongoose', { useMongoClient: true});
var QuoteSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Name is blank!"]
    },
    quote: {
        type: String,
        required: [true, "quote is blank!"]
    }
},{ timestamps: true });
var Quote = mongoose.model('Quote', QuoteSchema);




app.get('/', function(req, res) {
    res.render('index.ejs');
});

app.post('/quotes', function(req, res) {
    Quote.create(req.body, function(err, message){
        if (err) {
            let errors_arr = [];
            for (var key in err.errors) {
                let error = err.errors[key];
                error_arr.push(error.message);   
            }
        } else {
            console.log(message);
            
        }
    });
    res.redirect('/showQuotes');
});

app.get('/showQuotes', function(req, res) {
    Quote.find({}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            return res.render('quotes.ejs', {messages: messages});
        }
    });
});



app.listen(8000, function() {
    console.log('App listening on port 8000!');
});