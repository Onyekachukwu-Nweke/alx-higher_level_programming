#!/usr/bin/node
exports.callMeMoby = (x, theFunc) => {
  for (let i = 0; i < x; i++) theFunc();
};
