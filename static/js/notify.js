const user_id= JSON.parse(document.getElementById("json-username").textContent)

const notifySocket = new WebSocket(
    'ws://'
    +window.location.host
    +'/ws/'
    +'notification/'
)

notifySocket.onopen = function(e){
    console.log("Notifications Connected")
}

notifySocket.onclose = function(e){
    console.log("Notifications disconnected")

}
notifySocket.onerror = function(e){

}


var badge = document.getElementById('count_badge')

notifySocket.onmessage=function(e){
    data = JSON.parse(e.data)
    badge.innerHTML=data['countOfNotifi']
    console.log(data['countOfNotifi'])
    
}