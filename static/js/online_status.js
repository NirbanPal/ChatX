const loggedin_username = JSON.parse(document.getElementById('json-username-sender').textContent)
const online_status = new WebSocket(
    'ws://'
    +window.location.host
    +'/ws/'
    +'online/'
)

online_status.onopen = function(e){
    online_status.send(JSON.stringify({
        'username':loggedin_username,
        'type':'open',
    }))

}

// event for showing that user had left the website or chat
window.addEventListener("beforeunload", function(e){
    online_status.send(JSON.stringify({
        'username':loggedin_username,
        'type':'offline',
    }))
})

online_status.onclose = function(e){
    console.log("DISCONNECTED FROM ONLINE")
    // online_status.send(JSON.stringify({
    //     'username':loggedin_username,
    //     'type':'offline'
    // }))
}


// online_status.onerror = function(e){

// }
// online_status.onmessage = function(e){
//     data = JSON.parse(e.data)
//     var username = data['username']
//     var onlineStatus = data['online_status']
//     if (username!=loggedin_username){
//         var user_to_change = document.getElementById("${data.username}_status")
//         var small_status_to_change = document.getElementById("${data.username}_status")
//         if (onlineStatus===true){
//             user_to_change.style='green'
//             small_status_to_change.textContent="Online"

//         }
//         else{
//             user_to_change.style='grey'
//             small_status_to_change.textContent="Offline"

//         }


//     }

// }

online_status.onmessage = function(e){
    var data = JSON.parse(e.data)
    if(data.username != loggedin_username){
        var user_to_change = document.getElementById(`${data.username}_status`)
        var small_status_to_change = document.getElementById(`${data.username}_small`)
        var dotStatus = document.getElementById(`${data.username}_dotStatus`)
        if(data.online_status == true){
            user_to_change.style.color = 'green'
            small_status_to_change.textContent = 'Online'
            dotStatus.classList.remove("d-none")
        }else{
            user_to_change.style.color = 'grey'
            small_status_to_change.textContent = 'Offline'
            dotStatus.classList.add("d-none")
        }
    }
}
