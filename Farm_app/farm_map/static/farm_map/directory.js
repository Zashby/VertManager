const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value

function farmChoice(farm_id){
    const data = {
        farm_id : farm_id,
    }
    {
        // console.log(farm_id)
    // console.log(csrfToken)
    // console.log(csrfToken)
    fetch('/',{
        method: 'POST',
        body: JSON.stringify(data),

        headers:{
            'X-CSRFToken':csrfToken
        }
    }).then(res => res.json()).then(data => {console.log(data)
})}
}