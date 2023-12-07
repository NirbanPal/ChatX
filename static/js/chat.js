//id of that user with whom current user will talk
const id = JSON.parse(document.getElementById('json-username').textContent);

const sender_username = JSON.parse(document.getElementById('json-username-sender').textContent);

const receiver_username = JSON.parse(document.getElementById('json-username-receiver').textContent);

const messageInput = document.getElementById('message_input');

var sendButton = document.getElementById('chat-message-submit');

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

//If there is any incoming message in the socket
socket.onmessage = function(e){
    const data = JSON.parse(e.data)
    if(data.message && data.username===sender_username){
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
                <p class="bg-primary p-2 mt-2 ml-3 shadow-sm text-white float-left rounded">
                    ${data.message}
                </p>
            </td>
        </tr>`

    }

    

}


sendButton.onclick = function(e){
    e.preventDefault()

    const message = messageInput.value
    if (message.trim()===""){

        alert('You can not send only whitespaces as message')

        messageInput.value='';
        return false
    }
    else{
        
        socket.send(JSON.stringify({
            'type':'chat-message',
            'message':message,
            'username':sender_username,
            'receiver':receiver_username,
        }));
        
        messageInput.value='';
        sendButton.disabled = true;
        sendButton.classList.add('not-allowed','disabled')
        // scrollToBottom()
        return false
    }
}



// Add an event listener to the input field
messageInput.addEventListener('input', function() {
    // Check if the input value contains only spaces
    if (messageInput.value.trim() === '' || messageInput.value===null) {
        // If only spaces, disable the send button
        sendButton.disabled = true;
        sendButton.classList.add('not-allowed','disabled')
    } else {
        // If some letters are typed, enable the send button
        sendButton.disabled = false;
        sendButton.classList.remove('not-allowed','disabled')

    }
});

//scroll to bottom
// function scrollToBottom() {
//     let objDiv = document.getElementById("chat-body");
//     console.log(objDiv.scrollHeight)

//     objDiv.scrollTop = objDiv.scrollHeight;
// }

// scrollToBottom()

