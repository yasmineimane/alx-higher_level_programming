#!/usr/bin/node
exports.esrever = function (list) {
  const list2 = [];
  const length = list.length;
  for (let i = length - 1; i >= 0; i--) {
    list2.push(list[i]);
  }
  return list2;
};
