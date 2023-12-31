/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../**/*.html", "../js/*.js"],
  theme: {
    fontFamily: {
      montserrat: ["Montserrat", "sans-serif"],
    },
    extend: {
      colors: {
        primary: "#222327",
        secondary: "#FBFBFB",
        text: "#B9BFD4",
        detail: "#7A7A8C",
        bgcolor:
          "linear-gradient(90deg, rgba(85, 85, 97, 0.60) 0%, #2F2F33 90%)",
      },
      fontSize: {
        "2xl": [
          "1.5rem",
          {
            lineHeight: "2rem",
            letterSpacing: "-0.01em",
            fontWeight: "500",
          },
        ],
        display: ["7rem", { lineHeight: "normal", fontWeight: "500" }], //112px 136px == 8.5
        h1: ["3.25rem", { lineHeight: "normal", fontWeight: "500" }], //52px
        h2: ["2rem", { lineHeight: "normal", fontWeight: "500" }], //32px
        h3: ["1.25rem", { lineHeight: "normal", fontWeight: "500" }], //20px
        h4: ["1.25rem", { lineHeight: "normal" }], //20px
        h5: ["1rem", { lineHeight: "normal" }], //16px
        mini: ["0.625rem", { lineHeight: "normal" }], //10px
      },
    },
  },
  plugins: [],
};
