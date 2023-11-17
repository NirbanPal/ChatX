//id of that user with whom current user will talk
const id = JSON.parse(document.getElementById('json-username').textContent);

const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const receiver_username = JSON.parse(document.getElementById('json-username-receiver').textContent);

// Creating the socket connection
const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
)


//Open the socket connection
socket.onopen = function(e){
    console.log("connection build")
}

//close the socket connection
socket.onclose = function(e){
    console.log("Connection lost")
}

//error in socket connection
socket.onerror = function(e){
    console.log("Error")
}

//If there is sny incoming message in the socket
socket.onmessage = function(e){
    // data = json.parse(e.data)
    console.log(e)

}



