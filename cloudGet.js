//https://github.com/vbalasu/cloud/cloudGet.js
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.filename || (req.body && req.body.filename)) {
        var azure = require('azure-storage')
        var blobSvc = azure.createBlobService()
        blobSvc.getBlobToText('blobcontainer', req.body.domain+'/'+req.body.filename, function (err, blobcontent, blob) {
            context.res = { body : blobcontent }
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