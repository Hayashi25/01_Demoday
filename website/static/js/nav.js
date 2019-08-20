//------------------------------MENU----------------------------------------------------------

//TROCAR A COR DO MENU QUANDO A PAGINA ROLAR E SEU EIXO Y FOR MAIOR QUE 100PX
window.onscroll = function () {
    let menu = document.querySelector("#menu");
    if (window.pageYOffset > 100) {
        menu.style.backgroundColor = "rgba(50, 112, 53, 0.900)";
    }
    else {
        menu.style.backgroundColor = "rgba(0, 0, 0, 0)";
    }
}