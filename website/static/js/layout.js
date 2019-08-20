
let imgs = [];
let slideCaixa = document.getElementById("carrossel");
let imgAtual;
let numMaiorImg;
let tempoImg;

//------------------------------CARROSSEL----------------------------------------------------------

//CRIAR UMA FUNÇÃO QUE FAZ O CARREGAMENTO DO CAMINHO PARA ACESSAR A IMAGEM E ADICIONAR AO VETOR
function puxarImg(){
    let n = 1;
    for( let i = 0; i<3; i++){
        imgs[i] = new Image();
        imgs[i].src = "static/img/index/img" + n + ".jpg";
        n++;
    }
}

//APLICAR A IMAGEM NO BACKGROUND DA DIV, INFORMANDO QUAL IMAGEM VAI CARREGAR ATRAVÉS DO APARAMETRO
function mostrarImagens(img){
    slideCaixa.style.backgroundImage = "url('"+imgs[img].src+"')";
}

//CHAMAR AS FUNCOES 
function iniciar(){
    puxarImg();
    imgAtual = 0;
    numMaiorImg = imgs.length-1;
    mostrarImagens(imgAtual);
    tempoImg=setInterval(troca, 4000);
}

//TROCAR IMAGENS
function troca(){
    imgAtual++;
    if(imgAtual > numMaiorImg){
        imgAtual = 0;
    }
    mostrarImagens(imgAtual);
}

//QUANADO A PAGINA FOR CARREGADA
window.addEventListener("load", iniciar);

//------------------------------ FIM CARROSSEL----------------------------------------------------------

//------------------------------MENU----------------------------------------------------------

//TROCAR A COR DO MENU QUANDO A PAGINA ROLAR E SEU EIXO Y FOR MAIOR QUE 100PX
window.onscroll = function (){
    let menu = document.querySelector(".menu");
    if (window.pageYOffset > 100){
        menu.style.backgroundColor = "rgba(50, 112, 53, 0.900)";
    }
    else{
        menu.style.backgroundColor = "rgba(0, 0, 0, 0)";
    }
}





// ----------------ITENS DE TROCA DA LOJINHA-------------------------------
let papel = document.querySelector(".papel");
let plastico = document.querySelector(".plastico");
let metal = document.querySelector(".metal");
let vidro = document.querySelector(".vidro");

let materiais = document.querySelector("#materiais");
let materialPlastico = document.querySelector("#material_Plastico");
let materialPapel = document.querySelector("#material_Papel");
let materialMetal = document.querySelector("#material_Metal");
let materialVidro = document.querySelector("#material_Vidro");
let fecha = document.querySelector("#fechar");

// ABRIR POUP UP DE ITENS DO PLASTICO
function abrirPlastico(){
    materiais.style.display="block";
    materialPlastico.style.display="flex";
};
plastico.onclick = abrirPlastico;

// ABRIR POUP UP DE ITENS DO PAPEL
function abrirPapel(){
    materiais.style.display="block";
    materialPapel.style.display="flex";
};
papel.onclick = abrirPapel;

// ABRIR POUP UP DE ITENS DO METAL
function abrirMetal(){
    materiais.style.display="block";
    materialMetal.style.display="flex";
};
metal.onclick = abrirMetal;

// ABRIR POUP UP DE ITENS DO VIDRO
function abrirVidro(){
    materiais.style.display="block";
    materialVidro.style.display="flex";
};
vidro.onclick = abrirVidro;


// FECHAR TODAS AS POUP UP
function fechar(){
    materiais.style.display="none";
    materialPapel.style.display="none";
    materialPlastico.style.display="none";
    materialMetal.style.display="none";
    materialVidro.style.display="none";
};
fecha.onclick = fechar;