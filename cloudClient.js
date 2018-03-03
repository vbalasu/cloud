/* USAGE
var c = require('./cloudClient.js')
c.cloudDelete('test.csv', 'public')
c.cloudAppend('test.csv', 'public', 'someMoreData')
c.cloudPut('test.csv', 'public', 'somedata')
c.cloudGet('test.csv', 'public')
*/

var rp = require('request-promise')

module.exports.cloudGet = function (filename, domain) {
    baseurl = 'https://cloudmaticafunctions.azurewebsites.net/api/cloudGet?code=m8Qpr9D0D/FyOatpL9jnCL34ZBtMBz1U04kp4n4dia9kAfhFjNWgVQ=='
    url = baseurl + '&filename='+encodeURIComponent(filename)
    url = url + '&domain='+encodeURIComponent(domain)
    return rp.get(url)
    .then((data)=>{return data})
    .catch((err)=>{throw err.message})
}

module.exports.cloudPut = function (filename, domain, contents) {
    var options = {
        method: 'POST',
        uri: 'https://cloudmaticafunctions.azurewebsites.net/api/cloudPut?code=SDSGxtRh2S5RrSW/aNiFfgTE1bJhMqof3aiFdp8p7iYMjns/mFes0A==',
        body: {
            filename: filename,
            domain: domain,
            contents: contents
        },
        json: true // Automatically stringifies the body to JSON
    }
    return rp(options)
    .then((data)=>{return data})
    .catch((err)=>{throw err.message})
}

module.exports.cloudAppend = function (filename, domain, contents) {
    var options = {
        method: 'POST',
        uri: 'https://cloudmaticafunctions.azurewebsites.net/api/cloudAppend?code=WoQI74R74MsaMzqo3cxEV3AbU6IjzxyCdWMA/3VCBp8Iy9C14JUiHw==',
        body: {
            filename: filename,
            domain: domain,
            contents: contents
        },
        json: true // Automatically stringifies the body to JSON
    }
    return rp(options)
    .then((data)=>{return data})
    .catch((err)=>{throw err.message})
}

module.exports.cloudDelete = function (filename, domain) {
    var options = {
        method: 'POST',
        uri: 'https://cloudmaticafunctions.azurewebsites.net/api/cloudDelete?code=0iDGJqrFf3zzCFkSRtkogamQUR848INQviaa/sNGKlLSSR9uics2CA==',
        body: {
            filename: filename,
            domain: domain
        },
        json: true // Automatically stringifies the body to JSON
    }
    return rp(options)
    .then((data)=>{return data})
    .catch((err)=>{throw err.message})
}