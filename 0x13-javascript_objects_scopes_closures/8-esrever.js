#!/usr/bin/node
exports.esrever = function (list) {
  let list2 = [];
  for (let i = list.length; i >= 0; i--) {
    list2 = list[i];
  }
  return list2;
};
