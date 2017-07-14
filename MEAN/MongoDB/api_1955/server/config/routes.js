var peopleController = require('../controllers/peoples.js');

module.exports = function(app){
    app.get('/', peopleController.index);
    app.get('/new/:name', peopleController.new);
    app.get('/remove/:name', peopleController.remove);
    app.get('/:name', peopleController.show);
}