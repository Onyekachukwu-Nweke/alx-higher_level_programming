#!/usr/bin/node
exports.addMeMaybe = (num, theFunc) => {
  theFunc(++num);
};
