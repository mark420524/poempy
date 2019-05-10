const fs=require('fs');
const readline=require('readline');

/**node schedule */
const schedule = require('node-schedule');


 

schedule.scheduleJob('1111job','*/2 * * * * *', function(){
  console.log('1111');
});
 
setTimeout(function(){
	console.log('cancel 1111job')
	schedule.cancelJob('1111job')
},5000)



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
	let length=arr.length;
	for (let i=0;i<3;i++) {
		let random=randomNum(1,length)
		console.log(arr[random])
	}
	 
}
var randomNum=function (minNum,maxNum){ 
    switch(arguments.length){ 
        case 1: 
            return parseInt(Math.random()*minNum+1,10); 
        break; 
        case 2: 
            return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
        break; 
            default: 
                return 0; 
            break; 
    } 
}
let filename="poemall.txt";
readFile(filename,readcb)
