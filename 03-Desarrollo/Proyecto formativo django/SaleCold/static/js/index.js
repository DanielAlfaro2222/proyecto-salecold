'use strict';

const MenuPrincipal = document.getElementById('main-menu');
const IconMenuPrincipal = document.getElementById('main-menu-icon');

window.addEventListener("scroll", () => {
    const nav = document.querySelector(".main-menu");
    nav.classList.toggle("main-menu-scroll", window.scrollY > 600);
});

IconMenuPrincipal.addEventListener("click", () => {
    MenuPrincipal.classList.toggle("main-header__menu-categories--show");
});