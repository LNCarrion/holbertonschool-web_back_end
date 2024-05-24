module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  }, // Move the closing curly brace to this position

  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],

  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  }, // Add a comma after the closing curly brace

  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },

  plugins: ['jest'],

  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  }, // Add a comma after the closing curly brace

  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    },
  ], // Add a comma after the closing curly brace
};
