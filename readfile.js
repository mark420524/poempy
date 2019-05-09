const fs=require('fs');
const readline=require('readline');
var readFile=function (filename,callback){
	let fileRead=fs.createReadStream(filename);
	let contentReadLine=readline.createInterface({input:fileRead});
	let arr = new Array();
	contentReadLine.on('line',function(line){
		arr.push(line);
	});
	contentReadLine.on('close',function(){
		callback(arr);
	});
}

var readcb=function(arr){
	console.log(arr.length);
	console.log(arr[0])
}
let filename="poemall.txt";
readFile(filename,readcb)
