#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const secondMax = Math.max(...args.filter(num => num !== max));
  console.log(secondMax);
}
