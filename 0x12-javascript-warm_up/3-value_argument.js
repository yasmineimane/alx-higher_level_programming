#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
if (firstArg === undefined) { console.log('No argument'); } else { console.log(firstArg); }
