#!/usr/bin/node
const { list } = require('./100-data');
const newArray = list.map((value, index) => value * index);
console.log(list);
console.log(newArray);
