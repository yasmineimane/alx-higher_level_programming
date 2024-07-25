#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const item of list) {
    if (searchElement === item) {
      count++;
    }
  }
  return count;
};
