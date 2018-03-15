// 10950번
// var fs = require('fs');
// // var text = fs.readFileSync('/dev/stdin').toString().split('\n');
//
// var text = fs.readFileSync('input.text', 'utf8');
// text = text.split('\n');
// // console.log(text);
//
// for (var i = 0; i < Number(text[0]); i++) {
//   var text2 = text[i+1].split(' ');
//   console.log(Number(text2[0])+Number(text2[1]));
// }

// // 10951번
// var fs = require('fs');
// // var text = fs.readFileSync('/dev/stdin').toString().split('\n');
//
// var text = fs.readFileSync('input.text', 'utf8');
// text = text.split('\n');
// console.log(text.length)
// // console.log(text);
//
// for (var i = 0; i < text.length-1; i++) {
//   var text2 = text[i].split(' ');
//   console.log(Number(text2[0])+Number(text2[1]));
// }

// // 10952번
// var fs = require('fs');
// // var text = fs.readFileSync('/dev/stdin').toString().split('\n');
//
// var text = fs.readFileSync('input.text', 'utf8');
// text = text.split('\n');
// // console.log(text);
//
// for (var i = 0; i < text.length-1; i++) {
//   var text2 = text[i].split(' ');
//   if (Number(text2[0]) === 0 && Number(text2[1]) === 0) {
//     return;
//   }
//   else{
//   console.log(Number(text2[0])+Number(text2[1]));
//   }
// }

// 10953번
var fs = require('fs');
// var text = fs.readFileSync('/dev/stdin').toString().split('\n');

var text = fs.readFileSync('input.text', 'utf8').split('\n');
// console.log(text.length)
// console.log(text);

for (var i = 0; i < text.length-2; i++) {
  var text2 = text[i+1].split(',');
  console.log(Number(text2[0])+Number(text2[1]));
}
