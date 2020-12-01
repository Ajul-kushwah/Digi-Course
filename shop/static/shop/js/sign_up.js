var token = null;
var loading =null;
var wrongotp =null;

window.onload = function(){
    loading = document.getElementById('loading');

}
function validate(event){

    var form = event.target;
    var values = form.elements;
    var name = values.name.value;
    var email = values.email.value;
    token = values.csrfmiddlewaretoken.value;

    var error = document.getElementById('message');
    var message =null;

    message = validateForm(form);

    if(message){
        error.innerHTML = message;
        error.hidden = false;
    }
    else{

        error.innerHTML = "";
        error.hidden = true;
        //email..
        console.log('sending otp ..');
        try{
            sendEmail(email , name , token)
         }catch(er){
            console.log(er)
         }
    }
    return false;
}
function validateForm(form){

    var values = form.elements;
    var name = values.name.value;
    var phone = values.phone.value;
    var email = values.email.value;
    var password = values.password.value;
    var repassword = values.repassword.value;
//    token = values.csrfmiddlewaretoken.value;

    var message = null;

    if(!name.trim()){
            message = "Name Is Required."
    }else if(!email.trim()){
            message = "Email Is Required."
    }
    else if(!password.trim()){
            message = "Password Is Required."
    }
    else if(!repassword.trim()){
            message = "Enter Password Again."
    }
    else if(password.trim() != repassword.trim()){
            message = "Password Not Matched"
    }else if ( check_email(email)){
        message = "Email already register."
     
    }

    return message;
}

function check_email(email){
    var msg=null;
    $.ajax({
        method:"POST",
        url:"/check_email/",
        data:{'email': email}
    })
    .done(function(mseg){
        msg=mseg;
    })
    .fail(function(error){
        msg=error;
    })
    
    return msg;
}

function sendEmail(email,name,token){
//    console.log(token);
//    console.log(email,name);
    loading.hidden = false;
    $.ajax({
        method:"POST",
        url:"/send-otp/",
        headers:{'X-CSRFToken':token },
        data:{'name':name, 'email':email}
    })
    .done(function(msg){
//        alert('data '+ msg);
        loading.hidden = true;
        showOtpInput();
    })
    .fail(function(error){
        loading.hidden = true;
        function sweetalertclick3(){
            // Swal.fire('Hello world!');
            Swal.fire('Oops...', 'Internet connection unstable ! Try Again', 'error');
        }
        sweetalertclick3();
//        alert('Unable to send otp '+ error);
    })
 }


function showOtpInput(){
    var otpInput = document.getElementById('verificationInput');
    var submitButton = document.getElementById('submitButton');
    var verifyButton = document.getElementById('verifyButton');

    otpInput.hidden = false;
    verifyButton.hidden = false;
    submitButton.hidden = true;

}

function verifyCode(){
    var codeInput = document.getElementById('code');
    wrongotp = document.getElementById('wrong-otp');
    var code = codeInput.value;
    console.log('ttttt ',token)

    loading.hidden = false;

    $.ajax({
        method:"POST",
        url:"/verify/",
        headers:{'X-CSRFToken':token },
        data:{'code': code}
    })
    .done(function(msg){
        loading.hidden = true;
//        alert('code verified '+ msg);
        submitFrom();
    })
    .fail(function(error){
        loading.hidden = true;
        wrongotp.innerHTML = 'Wrong Otp';
        wrongotp.hidden = false;
        console.log(wrongotp);
//        alert('code is Invalid '+ error );
    })
}

function submitFrom(){
    var form = document.getElementById('form');
    var message = validateForm(form);
    if (message){

    }else{
        form.submit();
    }
}