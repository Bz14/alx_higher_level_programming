#!/usr/bin/node
exports.esrever = function (list) {
  let l = 0;
  let r = list.length - 1;
  while (l <= r) {
    const temp = list[l];
    list[l] = list[r];
    list[r] = temp;
    l += 1;
    r -= 1;
  }
  return list;
};
