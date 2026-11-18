// IMPORTING ALPINE JS
import Alpine from "alpinejs";

window.Alpine = Alpine;
Alpine.start();

// IMPORT HTMX
import "htmx.org";
window.htmx = require("htmx.org");

const testimonial = new Swiper(".testimonial", {
  // Optional parameters

  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  spaceBetween: "30",

  breakpoints: {
    768: {
      slidesPerView: 3,
    },
  },
});

const testimonial_homepage_slider = new Swiper(".testimonial_homepage_slider", {
  // Optional parameters

  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  spaceBetween: "100",

  breakpoints: {
    768: {
      slidesPerView: 2,
    },
  },
});


const coursesSlider = new Swiper(".courses_homepage_slider", {
  // Optional parameters

  loop: true,

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  spaceBetween: "100",

  breakpoints: {
    768: {
      slidesPerView: 2,
    },
  },
});