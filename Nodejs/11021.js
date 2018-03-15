// // 11021번
// var fs = require('fs');
// // var text = fs.readFileSync('/dev/stdin').toString().split('\n');
//
// var text = fs.readFileSync('input.text', 'utf8').split('\n');
// // console.log(text.length)
// // console.log(text);
//
// for (var i = 0; i < text.length-2; i++) {
//   var text2 = text[i+1].split(' ');
//   console.log("Case #"+String(i+1)+': '+(Number(text2[0])+Number(text2[1])));
// }
//

// 11022번
var fs = require('fs');
// var text = fs.readFileSync('/dev/stdin').toString().split('\n');

var text = fs.readFileSync('input.text', 'utf8').split('\n');
// console.log(text.length)
// console.log(text);

for (var i = 0; i < text.length-2; i++) {
  var text2 = text[i+1].split(' ');
  console.log("Case #"+String(i+1)+': '+
  text2[0]+' + '+text2[1]+ ' = '+
  (Number(text2[0])+Number(text2[1]))
  );
}
