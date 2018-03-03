//https://github.com/vbalasu/cloud/cloudDelete.js
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    var filename = req.body.filename
    var domain = req.body.domain
    if (filename) {
        var azure = require('azure-storage')
        var blobSvc = azure.createBlobService()
        blobSvc.deleteBlob('blobcontainer', domain+'/'+filename, function(error, result, response){
            if(error) {context.res = { status: 404, headers: {"Content-Type": "text/html"}, body : error.message }; context.done()}
            else {
                context.res = { headers: {"Content-Type": "text/html"},
                body : 'deleted' }
                context.done()
            }
        })
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass a filename and domain on the query string or in the request body"
        };
        context.done()
    }
};