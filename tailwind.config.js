/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/*.html", "./src/**/templates/**/*.html"],
  theme: {
    extend: {
      screens: {
        '3xl': '1920px',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
};
