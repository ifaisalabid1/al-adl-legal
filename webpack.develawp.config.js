const path = require("path");

module.exports = {
  entry: "./develawp/static/develawp/js/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "./develawp/static/develawp/js/"),
  },
};
