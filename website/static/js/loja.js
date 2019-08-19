
//----------------------------LOJINHA-----------------------------------------------------
let body = document.querySelector("body");
window.location;
function arrumarLayoutLoja(){
    // ?????//
    if (location.href == "file:///C:/Users/Principal/Desktop/certo/loja.html"){
        body.style.gridTemplateRows = "35vh 35vh 35vh 35vh";
        body.style.gridTemplateColumns = "30vh 50vh 50vh 50vh"

    }
    else{
        body.style.gridTemplateRows = "100vh 85vh 70vh 30vh";
    }

}
window.addEventListener("load", arrumarLayoutLoja);

// ----------------ITENS DE TROCA DA LOJINHA-------------------------------
let papel = document.querySelector(".papel");
let plastico = document.querySelector(".plastico");
let metal = document.querySelector(".metal");
let vidro = document.querySelector(".vidro");
let mostraP = document.querySelector("#materialPlastico");

function mostrarItensDeTroca(){
    mostraP.style.display="block";
};
papel.onclick = mostrarItensDeTroca;
