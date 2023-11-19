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
    const data = JSON.parse(e.data)
    if(data.message && data.username===message_username){
        document.querySelector("#chat-body").innerHTML += `
        <tr>
            <td>
                <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">
                    ${data.message}
                </p>
            </td>
        </tr>`
    }
    else{
        document.querySelector("#chat-body").innerHTML += `
        <tr>
            <td>
                <p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">
                    ${data.message}
                </p>
            </td>
        </tr>`

    }

    

}


document.getElementById('chat-message-submit').onclick = function(e){
    e.preventDefault()

    const messageInputDom = document.querySelector('#message_input')
    const message = messageInputDom.value
    if (message.trim()===""){

        alert('You can not send only whitespaces as message')

        messageInputDom.value='';
        return false
    }
    else{
        
        socket.send(JSON.stringify({
            'type':'chat-message',
            'message':message,
            'username':message_username
        }));
    
        messageInputDom.value='';
    
        return false
    }
}


