#!/usr/bin/node
exports.esrever = function (list) {
  let list2 = [];
  for (let i = list.length; i >= 0; i--) {
    for (let j = 0; j < list.length; j++) {
	list2[j] = list[i];
  }
  return list2;
};
