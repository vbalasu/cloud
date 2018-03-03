//https://github.com/vbalasu/cloud/cloudAppend.js
module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    var filename = req.body.filename
    var domain = req.body.domain
    var contents = req.body.contents
    if (filename) {
        var azure = require('azure-storage')
        var blobSvc = azure.createBlobService()
        blobSvc.appendFromText('blobcontainer', domain+'/'+filename, contents, function(error, result, response){
            if(error) { context.res = {status:404,headers: {"Content-Type": "text/html"},body:error.message}; context.done() }
            else {
                context.res = { headers: {"Content-Type": "text/html"},
                    body : 'https://cloudmaticafunctions.azurewebsites.net/api/cloudGet?code=m8Qpr9D0D/FyOatpL9jnCL34ZBtMBz1U04kp4n4dia9kAfhFjNWgVQ==&filename='+encodeURIComponent(filename)+'&domain='+encodeURIComponent(domain) }
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