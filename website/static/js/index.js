let imgs = [];
let slideCaixa = document.getElementById("carrossel");
let imgAtual;
let numMaiorImg;
let tempoImg;

function puxarImg(){
    let n = 1;
    for(let i = 0; i<3; i++){
        imgs[i] = new Image();
        imgs[i].src = "static/img/index/imagem"+n+".jpg";
        n++;
    }
}

function mostrarImagens(img){
    slideCaixa.style.backgroundImage = "url('"+imgs[img].src+"')";
}

function iniciar(){
    puxarImg();
    imgAtual = 0;
    numMaiorImg = imgs.length-1;
    mostrarImagens(imgAtual);
    tempoImg=setInterval(troca, 4000);
}

function troca(){
    imgAtual++;
    if(imgAtual > numMaiorImg){
        imgAtual = 0;
    }
    mostrarImagens(imgAtual);
}

window.addEventListener("load", iniciar);