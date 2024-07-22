#!/usr/bin/node
const args = process.argv.slice(2);
const isNumber = Number(args[0]);
if (!isNumber) {
  console.log('Not a number');
} else {
  console.log(`My number: ${isNumber}`);
}
