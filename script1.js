function GetAnswer(){
    
    song = document.getElementsByClassName("song")[0].value;
    keymatrix = document.getElementsByClassName("keymatrix")[0].value;
    const request = new XMLHttpRequest();
    const url = "http://127.0.0.1:8000/answer"
    const params = "song=" + song+ "&keymatrix=" + keymatrix;
    request.open('POST',url,true)
    request.setRequestHeader('Content-Type', 'application/x-www-form-url');
    request.addEventListener("readystatechange", () => {
        if (request.readyState === 4 && request.status === 200) {
            console.log( request.responseText );
        }
    });
    response = request.send(params);
    alert(request.responseText)
}