const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value
// const csrfToken = Cookies.get('csrftoken')
let stackData;

let modal = document.querySelector(".modal")
let closeBtn = document.querySelector(".close-btn")
let modalDiv = document.querySelector(".modal-div")

function scoutStack(stack_id){
    const data = {
        stack_id : stack_id,
        logtype : 'Scout'
    }
    if (confirm('Are you sure you want to scout this stack?'))
     { //console.log(stack_id)
    // console.log(csrfToken)
    // console.log(csrfToken)
    fetch('scout/',{
        method: 'POST',
        body: JSON.stringify(data),

        headers:{
            'X-CSRFToken':csrfToken
        }
    }).then(res => res.json()).then(data => {if(data.response !== 'logged'){
        console.error(data.message)
    } else {location.reload()}
})}
}

function calibrate(stack_id){
const data = {
    stack_id : stack_id,
    logtype : 'Calibrate'
}
if(confirm('Are you sure you want to log this calibration?')){
// console.log(stack_id)
// console.log(csrfToken)
// console.log(csrfToken)
fetch('scout/',{
    method: 'POST',
    body: JSON.stringify(data),

    headers:{
        'X-CSRFToken':csrfToken
    }
}).then(res => res.json()).then(data => {if(data.response !== 'logged'){
    console.error(data.message)
} else {location.reload()}
})}
}


function harvestStack(stack_id){
  const data = {
      stack_id : stack_id,
  }
  if(confirm('Are you sure you want to harvest this stack?')){
  // console.log(stack_id)
  // console.log(csrfToken)
  // console.log(csrfToken)
  fetch('harvest/',{
      method: 'POST',
      body: JSON.stringify(data),
  
      headers:{
          'X-CSRFToken':csrfToken
      }
  }).then(res => res.json()).then(data => {if(data.response !== 'harvested'){
      console.error(data.message)
  } else {location.reload()}
  })}
  }

  function plantStack(stack_id){
    const data = {
        stack_id : stack_id,
    }
    if(confirm('Are you sure you want to plant in this stack?')){
    // console.log(stack_id)
    // console.log(csrfToken)
    // console.log(csrfToken)
    fetch('plant/',{
        method: 'POST',
        body: JSON.stringify(data),
    
        headers:{
            'X-CSRFToken':csrfToken
        }
    }).then(res => res.json()).then(data => {if(data.response !== 'planted'){
        console.error(data.message)
    } else {location.reload()}
    })}
    }


function modalBox(stack_id){
  
  fetch(`/api/stack/${stack_id}`).then(res => res.json()).then(data=> {
        modalPop(data[0]);
  })
  
  
}
function modalPop(stack){


  modalDiv.innerHTML = '';
  if(stack.empty){
    modalDiv.innerHTML = `<button onclick="plantStack(${stack.id})">Plant</button>`
    if(stack.to_calibrate){
      modalDiv.innerHTML = `<button onclick="plantStack(${stack.id})">Plant</button> <button onclick="calibrate(${stack.id})">Calibration</button>`
    }
  } else if (stack.to_harvest === true && stack.scout_week >= stack.harvest_week){ 
    modalDiv.innerHTML= `<button onclick="harvestStack(${stack.id})">Harvest</button>`
    if(stack.to_calibrate){
      modalDiv.innerHTML= `<button onclick="harvestStack(${stack.id})">Harvest</button> <button onclick="calibrate(${stack.id})">Calibration</button>`
    }
  } else if (stack.to_calibrate){
    modalDiv.innerHTML= `<button onclick="calibrate(${stack.id})">Calibration</button>`
    if(stack.scout_week < stack.harvest_week){
      modalDiv.innerHTML = `<button onclick="scoutStack(${stack.id})">Scout</button> <button onclick="calibrate(${stack.id})">Calibration</button>`
    }
  } else if (stack.scout_week >= stack.harvest_week && stack.to_harvest === false){
    modalDiv.innerHTML = '<h4> No more scouting required </h4>'
  } else {modalDiv.innerHTML = `<button onclick="scoutStack(${stack.id})">Scout</button>`}
  modal.style.display = "block"; 
}


closeBtn.onclick = function(){
  modal.style.display = "none"
}
window.onclick = function(e){
  if(e.target == modal){
    modal.style.display = "none"
  }
}

