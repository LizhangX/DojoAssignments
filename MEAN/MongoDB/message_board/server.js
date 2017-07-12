var express = require('express');
var mongoose = require('mongoose');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/static'));

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/basic_mongoose', { useMongoClient: true });

var MessageSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'name cannot be blank'],
        minlength: [4, 'Name must be at least four characters']
    },
    message: {
        type: String,
        required: [true, 'message cannot be blank']  
    },
    _comments: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Comment'
    }]
}, { timestamps: true });
var CommentSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'name cannot be blank'],
        minlength: [4, 'Name must be at least four characters']
    },
    comment: {
        type: String,
        required: [true, 'comment cannot be blank']  
    },
    _message: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Message'
    }
},{ timestamps: true });

var Message = mongoose.model('Message', MessageSchema);
var Comment = mongoose.model('Comment', CommentSchema);


//routes
app.get('/', function(req, res) {
    Message.find({}).populate('_comments').exec(function(err, messages){
        if (err) {
            console.log(err);
        } else {
            console.log(messages);
            res.render('index.ejs', {messages: messages});
        }
    });
    
});

app.post('/messages', function(req, res) {
    Message.create(req.body, function(err, message){
        if (err) {
            // console.log(err);
        } else {
            console.log(message);
        }
    });
    res.redirect('/');
});

app.post('/comments', function(req, res) {
    console.log(req.body);
    Comment.create(req.body, function(err, comment){
        if (err) {
            console.log(err);
        } else {
            console.log(comment);
            Message.findByIdAndUpdate(req.body.message, {$push: { _comments: comment._id}}, {new: true}, function(err, message){
                if (err) {
                    console.log(err);
                } else {
                    console.log(message);
                    res.redirect('/');
                }
            });
        }
    });
});


app.listen(8000, function() {
    console.log('App listening on port 8000!');
});