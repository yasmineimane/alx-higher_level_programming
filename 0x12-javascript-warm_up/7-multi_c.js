#!/usr/bin/node
const args = process.argv.slice(2);
const x = Number(args[0]);
if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
