#!/usr/bin/node
const dict = require('./101-data').dict;

function computeUsersByOccurrence (dict) {
  const usersByOccurrence = {};
  for (const userId in dict) {
    const occurrences = dict[userId];
    if (!usersByOccurrence[occurrences]) {
      usersByOccurrence[occurrences] = [];
    }
    usersByOccurrence[occurrences].push(userId);
  }
  return usersByOccurrence;
}

const usersByOccurrence = computeUsersByOccurrence(dict);
console.log(usersByOccurrence);
