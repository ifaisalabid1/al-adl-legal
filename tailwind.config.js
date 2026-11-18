module.exports = {
  content: [
    "./website/templates/**/*.html",
    "./develawp/templates/**/*.html",
    "./blog/templates/**/*.html",
    "./templates/**/*.html",
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: "1rem",
        sm: "3rem",
      },
    },

    extend: {
      colors: {
        primary: "#628078",
        secondary: "#12343b",
        third: "#201d1e",
        gold: "#c89665",
      },
    },

    fontFamily: {
      josefinSans: ["Josefin Sans Variable", "sans-serif"],
      kulimPark: ["Kulim Park", "sans-serif"],
    },
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
};
