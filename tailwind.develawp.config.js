module.exports = {
  content: ["./develawp/templates/**/*.html"],

  theme: {
    extend: {
      colors: {
        lightGreen: "#00e7bc",
        textBlue: "#525FE1",
        primary: "#2E9FD1",
        secondary: "#143B5D",
        third: "#211D1E",
        gold: "#FFBF00",
      },
    },

    container: {
      center: true,
      padding: {
        DEFAULT: "1rem",
        sm: "3rem",
      },
    },

    fontFamily: {
      poppins: ["Poppins", "sans-serif"],
      openSans: ["Open Sans", "sans-serif"],
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
