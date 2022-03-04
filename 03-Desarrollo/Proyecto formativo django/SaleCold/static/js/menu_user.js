const IconoMenuUsuarioNormal=document.getElementById('icon-menu-user-normal');
const MenuUsuarioNormal=document.getElementById('menu-user-normal');
IconoMenuUsuarioNormal.addEventListener('click',()=>MenuUsuarioNormal.classList.toggle('menu-user-normal--show'));
IconoMenuUsuarioNormal.addEventListener('click',()=> console.log('Funciona'));