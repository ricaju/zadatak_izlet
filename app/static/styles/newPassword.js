function resetingPassword(){
	var newPassword = document.getElementById("inputPassword").value;
	var confirmPassword = document.getElementById("repeatPassword").value;
	var email = document.getElementById("inputEmail").value;

	if(newPassword=="" || confirmPassword=="" || email==""){
		alert("Some boxes are empty");
	}
	else if(newPassword != confirmPassword){
		alert("New password and confirmed password are not the same!");
	}
	else{
		alert("Your password has been changed!"); 
		window.location = "login.html";
	}

}