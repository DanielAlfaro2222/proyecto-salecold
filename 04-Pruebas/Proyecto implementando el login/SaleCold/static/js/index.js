const MenuPrincipal = document.getElementById('main-menu');
const IconMenuPrincipal = document.getElementById('main-menu-icon');
const IconoMenuUsuarioNormal = document.getElementById('icon-menu-user-normal');
const MenuUsuarioNormal = document.getElementById('menu-user-normal');

IconMenuPrincipal.addEventListener('click', () =>
	MenuPrincipal.classList.toggle('main-header__menu-categories--show')
);

IconoMenuUsuarioNormal.addEventListener('click', () =>
	MenuUsuarioNormal.classList.toggle('menu-user-normal--show')
);