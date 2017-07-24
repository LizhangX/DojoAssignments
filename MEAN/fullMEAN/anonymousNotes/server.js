let express = require('express');
let bp = require('body-parser');
let morgan = require('morgan');
let session = require('express-session');
let port = 8000;

let app = express();

app.use(express.static(__dirname + '/public/dist'));
app.use(morgan('tiny'));
app.use(bp.urlencoded( { extended: true } ));
app.use(bp.json());
app.use(session({
    secret:'mysecret',
    resave: false,
    saveUninitialized: true,
    cookie: {}
}));

require('./server/config/mongoose');
require('./server/config/routes')(app);

app.listen(port, ()=> { console.log(`Listening to port ${port}...`); });

