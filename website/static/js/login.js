window.onload = function() {
    document.getElementById('login_aluno').style.visibility = 'hidden';
    document.getElementById('login_escola').style.visibility = 'hidden';
}

logarEscola = function() {
    document.getElementById('login_escola').style.visibility = 'visible';
    document.getElementById('login_aluno').style.visibility = 'hidden';
    document.getElementById('icones').style.visibility = 'hidden';
}

logarAluno = function() {
    document.getElementById('login_aluno').style.visibility = 'visible';
    document.getElementById('login_escola').style.visibility = 'hidden';
    document.getElementById('icones').style.visibility = 'hidden';
}

voltarOpcoes = function() {
    document.getElementById('icones').style.visibility = 'visible';
    document.getElementById('login_escola').style.visibility = 'hidden';
    document.getElementById('login_aluno').style.visibility = 'hidden';
}