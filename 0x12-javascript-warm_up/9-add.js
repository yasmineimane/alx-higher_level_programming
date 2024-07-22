#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const args = process.argv.slice(2);
add(Number(args[0]), Number(args[1]));
