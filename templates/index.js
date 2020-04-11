function updateMap()
{
    fetch("http://shiny.john-coene.com:8080/dxy")
    .then(response => response.json())
    .then(data =>{
        console.log(data)
    })
}

updateMap();