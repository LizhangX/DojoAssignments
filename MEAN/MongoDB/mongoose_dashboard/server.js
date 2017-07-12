var express = require('express');
var mongoose = require('mongoose');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/static"));

app.set('view engine', 'ejs');
app.set('views', __dirname + "/views");

//mongoose
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/basic_mongoose', { useMongoClient: true });
var CatSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Name cannot be blank"]
    },
    weight: {
        type: Number,
        required: [true, "Weight cannot be blank"]
    },
    color: {
        type: String,
        required: [true, "Color cannot be blank"]
    }
}, { timestamps: true });
var Cat = mongoose.model('Cat', CatSchema);

//routes
app.get('/', function(req, res) {
    Cat.find({}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            res.render('index.ejs', {messages: messages});
        }
    });
});

app.get('/cats/showNew', function(req, res) {
    console.log('inside show new method');
    
    res.render('new.ejs');
});

app.get('/cats/:id', function(req, res) {
    Cat.find({_id: req.params.id}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            console.log(messages);
            
            res.render('display.ejs', {messages: messages});
        }
    });
});

app.post('/cats/addNew', function(req, res) {
    Cat.create(req.body, function(err, cat){
        if (err) {
            let errors_arr = [];
            for (var key in err.errors) {
                var error = err.errors[key];
                errors_arr.push(error.message);  
            }
                console.log(errors_arr); 
        } else {
            console.log(cat);
            
        }
    });
    res.redirect('/');
});

app.get('/cats/showEdit/:id', function(req, res) {
    Cat.find({_id: req.params.id}, function(err, messages){
        if (err) {
            console.log(err);
        } else {
            res.render('edit.ejs', {messages: messages});
        }
    });
});

app.post('/cats/edit/:id', function(req, res) {
    console.log(req.params.id);
    
    Cat.findByIdAndUpdate(req.params.id, {$set: req.body}, function(err, message){
        if (err) {
            console.log(err);
        } else {
            res.redirect('/');
        }
    });
    
});

app.post('/cats/destroy/:id', function(req, res) {
    Cat.findByIdAndRemove(req.params.id, function(err,message){
        if (err) {
            console.log(err);
        } else {
            res.redirect('/');
        }
    });
});

app.listen(8000, function() {
    console.log('App listening on port 8000!');
});