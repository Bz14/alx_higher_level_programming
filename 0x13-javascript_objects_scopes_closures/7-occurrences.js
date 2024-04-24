#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const val of list) {
    if (val === searchElement) {
	    count += 1;
    }
  }
  return count;
};
