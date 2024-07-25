#!/usr/bin/node
let nbrArg = 0;
exports.logMe = function (item) {
  console.log(`${nbrArg}: ${item}`);
  nbrArg++;
};
