var catController = require('./../controllers/cats.js');

module.exports = function(app){
    //routes
    app.get('/', catController.index);
    app.get('/cats/showNew', catController.showNew);
    app.get('/cats/:id', catController.showOne);
    app.post('/cats/addNew', catController.addnew);
    app.get('/cats/showEdit/:id', catController.showEdit);
    app.post('/cats/edit/:id', catController.edit);
    app.post('/cats/destroy/:id', catController.destroy);
};