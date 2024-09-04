/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.{jsx, js, ts, tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

