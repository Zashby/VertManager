const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value
const lightButton = document.getElementById('light-button')


function stateSwitch(data){
 let   stack = document.getElementById(`${data.stack_id}`);

if(data.empty){
    return
}
 if (data.light_state === true){
    const lightImage = document.getElementById(`light-image-${stack.id}`);
    lightImage.src= "/static/farm_map/lit.png";
 } else{
    const lightImage = document.getElementById(`light-image-${stack.id}`);
    lightImage.src = "/static/farm_map/dim.png";
 }
}

function fixed(stack_id){
    let lightBorder = document.getElementById(`stack-${stack_id}`)
    lightBorder.classList.remove("to_fix")
    let lightDrop = document.getElementById(`light-drop-${stack_id}`)
    lightDrop.remove()
}

function lightSwitch(stack_id){
    const data = {
        type: 'switch',
        stack_id : stack_id,
    }
    
    fetch('',{
        method: 'POST',
        body: JSON.stringify(data),
    
        headers:{
            'X-CSRFToken':csrfToken
        }
    }).then(res => res.json()).then(data => {if(data.response !== 'switch'){
        console.error(data.message)
    } else {stateSwitch(data)}
    })
    }

function lightScheduleFix(event, stack_id){
    const data = {
        type: 'change',
        stack_id : stack_id,
    }
    
    fetch('',{
        method: 'POST',
        body: JSON.stringify(data),
    
        headers:{
            'X-CSRFToken':csrfToken
        }
    }).then(res => res.json()).then(data => {if(data.response !== 'changed'){
        console.error(data.message)
    } else {fixed(stack_id)}
    })
    event.stopPropagation()
}
