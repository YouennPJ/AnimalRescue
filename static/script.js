let bouton = document.getElementById("sauvegarderFormulaire")
bouton.addEventListener("click",valide, false)

function valide(event){
    console.log("Debut")
    if (validerForm()){
        console.log("Valide")
        document.getElementById("form").submit()
        event.preventDefault()
    }
    else {
        console.log("Invalide")
        document.getElementById("submitinvalide").innerHTML = "Tous les champs doivent être remplis et correct!"
        event.preventDefault()
    }
}

function validerForm() {

    var valide = true;
    var nom = document.getElementById("nom").value;
    var rue = document.getElementById("rue").value;
    var espece = document.getElementById("espece").value;
    var race = document.getElementById("race").value;
    var age = document.getElementById("age").value;
    var description = document.getElementById("description").value;
    var email = document.getElementById("email").value;
    var ville = document.getElementById("ville").value;
    var codePostal = document.getElementById("code_postal").value;

    
    if (nom.length < 3 || nom.length > 20) {
        document.getElementById("nominvalide").innerHTML = 
        "Le nom doit contenir entre 3 et 20 caracteres"
        valide = false;
    }
    if (nom.includes(',')) {
      document.getElementById("nominvalide").innerHTML = 
      "Le champ ne peut pas contenir de virgule"
      valide = false;
    } 
    if (!nom) {
        document.getElementById("nominvalide").innerHTML = "Champ requis"
        valide = false;
    }
    if (!(!nom) && !nom.includes(',') && !(nom.length < 3 || nom.length > 20)) {
        document.getElementById("nominvalide").innerHTML = ""
    }


    
    if (espece.includes(',')) {
        document.getElementById("especeinvalide").innerHTML =
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    } 
    if (!espece) {
        document.getElementById("especeinvalide").innerHTML =
        "Champ requis"
        valide = false;
    } 
    if (!espece.includes(',') && !(!espece)) {
        document.getElementById("especeinvalide").innerHTML = ""
    }


    if (!race) {
        document.getElementById("raceinvalide").innerHTML =
        "Champ requis"
        valide = false;
    } 
    if (race.includes(',')) {
        document.getElementById("raceinvalide").innerHTML =
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    } 
    if (!race.includes(',') && !(!race) ){
        document.getElementById("raceinvalide").innerHTML = ""
    }


    if (!age) {
        document.getElementById("ageinvalide").innerHTML =
        "Le champ doit contenir des chiffres"
        valide = false;
    } 
    if (age < 0 || age > 30) {
        document.getElementById("ageinvalide").innerHTML =
        "L'age doit etre en 0 et 30'"
        valide = false;
    }
    if (!(age < 0 || age > 30) && !(!age) ){
        document.getElementById("ageinvalide").innerHTML = ""
    }


    if (!description) {
        document.getElementById("descriptioninvalide").innerHTML =
        "Champ requis"
        valide = false;
    } else {
        document.getElementById("descriptioninvalide").innerHTML = ""
    }
    if (description.includes(',')) {
        document.getElementById("descriptioninvalide").innerHTML =
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    } 
    if (!description.includes(',') && !(!description) ){
        document.getElementById("descriptioninvalide").innerHTML = ""
    }



    if (!email) {
        document.getElementById("emailinvalide").innerHTML =
        "Champ requis"
        valide = false;
    } 
    if (!/.*@..*\...*/.test(email)) {
        document.getElementById("emailinvalide").innerHTML =
        "Le format du mail est incorrect"
        valide = false;
    } 
    if (email.includes(',')) {
        document.getElementById("emailinvalide").innerHTML= 
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    }  
    if (!email.includes(',') && !(!email) && /.*@..*\...*/.test(email)){
        document.getElementById("emailinvalide").innerHTML = ""
    }


    if (!rue) {
        document.getElementById("rueinvalide").innerHTML=
        "Champ requis"
        valide = false;
    }
    if (rue.includes(',')) {
        document.getElementById("rueinvalide").innerHTML=
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    }  
    if (!rue.includes(',') && !(!rue) ){
        document.getElementById("rueinvalide").innerHTML = ""
    }


    if (!ville) {
        document.getElementById("villeinvalide").innerHTML=
        "Champ requis"
        valide = false;
    }
    if (ville.includes(',')) {
        document.getElementById("villeinvalide").innerHTML=
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    }  
    if (!ville.includes(',') && !(!ville) ){
        document.getElementById("villeinvalide").innerHTML = ""
    }


    if (!/[A-Za-z][0-9][A-Za-z]\s?[0-9][A-Za-z][0-9]/.test(codePostal)) {
        document.getElementById("code_postalinvalide").innerHTML=
        "Le format du code postal est incorrect"
        valide = false;
    }   
    if (!codePostal) {
        document.getElementById("code_postalinvalide").innerHTML=
        "Champ requis"
        valide = false;
    }
    if (codePostal.includes(',')) {
        document.getElementById("code_postalinvalide").innerHTML=
        "Le champ ne peut pas contenir de virgule"
        valide = false;
    }  
    if (!codePostal.includes(',') && !(!codePostal) && /[A-Za-z][0-9][A-Za-z]\s?[0-9][A-Za-z][0-9]/.test(codePostal)){
        document.getElementById("code_postalinvalide").innerHTML = ""
    }
    

    return valide;
}