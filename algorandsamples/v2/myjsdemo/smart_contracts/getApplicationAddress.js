const algosdk = require('algosdk');

appID = 95223182
const actual = algosdk.getApplicationAddress(appID);
console.log("Application Address: " + actual);