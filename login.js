var pokusaji = 3;
function login(){
	if(document.getElementById("inputUserame").value == "korisnik" && document.getElementById("inputPassword").value == "1234"){  //iz baze ce se vući username i password
		console.log("kasjdfksdjf");
		alert ("Successfull login");
		window.location = "izleti.html";
	}
	else{
		pokusaji--;
		alert ("Wrong password! You have: " + pokusaji + " attempts left");
	}
	if(pokusaji == 0){
			document.getElementById("inputUserame").disabled = true;   //nakon 3 pokusaja polja se vise ne mogu ispuniti
			document.getElementById("inputPassword").disabled = true;
			document.getElementById("logButton").disabled = true;
		}
	}