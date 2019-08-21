
let imgs = [];
let slideCaixa = document.getElementById("carrossel");
let imgAtual;
let numMaiorImg;
let tempoImg;

//------------------------------CARROSSEL----------------------------------------------------------

//CRIAR UMA FUNÇÃO QUE FAZ O CARREGAMENTO DO CAMINHO PARA ACESSAR A IMAGEM E ADICIONAR AO VETOR
function puxarImg() {
    let n = 1;
    for (let i = 0; i < 3; i++) {
        imgs[i] = new Image();
        imgs[i].src = "static/img/index/img" + n + ".jpg";
        n++;
    }
}

//APLICAR A IMAGEM NO BACKGROUND DA DIV, INFORMANDO QUAL IMAGEM VAI CARREGAR ATRAVÉS DO APARAMETRO
function mostrarImagens(img) {
    slideCaixa.style.backgroundImage = "url('" + imgs[img].src + "')";
}

//CHAMAR AS FUNCOES 
function iniciar() {
    puxarImg();
    imgAtual = 0;
    numMaiorImg = imgs.length - 1;
    mostrarImagens(imgAtual);
    tempoImg = setInterval(troca, 4000);
}

//TROCAR IMAGENS
function troca() {
    imgAtual++;
    if (imgAtual > numMaiorImg) {
        imgAtual = 0;
    }
    mostrarImagens(imgAtual);
}

window.addEventListener("load", iniciar);
