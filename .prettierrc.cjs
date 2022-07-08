/** @type {import('prettier').Config} */
module.exports = {
  printWidth: 120,
  semi: false,
  singleQuote: true,
  trailingComma: 'all',

  plugins: [require('prettier-plugin-packagejson')],
}
