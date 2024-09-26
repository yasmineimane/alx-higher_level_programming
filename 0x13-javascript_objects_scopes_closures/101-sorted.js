#!/usr/bin/node
const { dict } = require('./101-data');
const occurrencesDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }
  occurrencesDict[occurrences].push(userId);
}
console.log(occurrencesDict);
