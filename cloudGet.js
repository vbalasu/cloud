//https://github.com/vbalasu/cloud/cloudGet.js
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    var filename = req.query.filename
    var domain = req.query.domain

    if (filename) {
        var azure = require('azure-storage')
        var blobSvc = azure.createBlobService()
        blobSvc.getBlobToText('blobcontainer', domain+'/'+filename, function (err, blobcontent, blob) {
            context.res = {     
                headers: {"Content-Type": "text/html"},
                body : blobcontent 
            }
            context.done()
        })
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass a filename and domain on the query string or in the request body"
        };
    }
};