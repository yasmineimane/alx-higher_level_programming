#!/usr/bin/node
exports.esrever = function (list) {
  const list2 = [];
const length = list.length;
  for (let i = length -1; i >= 0; i--) {
    for (let j = 0; j < length; j++) {
	list2[j] = list[i];
  }
  return list2;
};
