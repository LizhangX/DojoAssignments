let path = require('path');
let Notes = require('./../controllers/notes');

module.exports = function(app){
    app.post('/notes', Notes.create);
    app.get('/notes', Notes.show);

    app.all('*', (res, req, next) => {
        res.sendFile(path.resolve('./public/dist/index.html'));
    });

};