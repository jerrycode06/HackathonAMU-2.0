function updateMap() {
    fetch("static/js/data.json")
        .then(response => response.json())
        .then(rsp => {

            rsp.data.forEach(element => {
                latitude = element.Lat
                longitude = element.Long


                cases = element.Confirmed;
                if (cases > 255) {
                    color = "rgb(255,0,0)"
                }
                else (
                    color = "rgb(${cases},0,0)"
                )

                // Mark on the map
                var marker = new mapboxgl.Marker({
                    draggable: false,
                    color: color
                })
                    .setLngLat([longitude, latitude])
                    .addTo(map);

                var popup = new mapboxgl.Popup({ closeOnClick: true })
                    .setLngLat([-96, 37.8])
                    .setHTML('<h1>As of 11th April 2020</h1>')
                    .addTo(map);

            });
        })
}

updateMap();