const locationDiv =document.querySelector('#location')
const generateLocation =document.querySelector('#generatenews')
console.log('hello', generateLocation)


generateLocation.addEventListener("click", async function(){
    let newsData= await getnews()
    console.log(newsData)
    let newsHtml = ''
    newsData?.forEach((newsArticle) => {
    newsHtml += `<div class="card" style="width: 18rem;">
    <img src="${newsArticle.image_url}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">${newsArticle.title}</h5>
      <p class=""card-text">"${newsArticle.snippet}"</p>
      <a href="${newsArticle.url}" class="btn btn-primary">Read Me Two</a>
    </div>
    </div>`
    
   
  })
// const reducer = (accumulator, currentValue) => accumulator + personCardHtml(currentValue);
// const personsHtml = people.reduce(reducer, '')
const container = document.querySelector('#news-container')
container.insertAdjacentHTML('beforeend', newsHtml)
    // renderdiv(weather)
})
 
function getnews(){
    let newsURL=`https://api.marketaux.com/v1/news/all?countries=US&filter_entities=true&language=en&api_token=${keys}`
   const newsResults = fetch(newsURL)
    .then((response) => {
        return response.json()
    })
    .then((newsData) =>  {
        return newsData.data
    })
    .catch(function(err){
        console.error(err)
    }) 
    return newsResults
}


function renderdiv(weather){
     // Adding to DOM
    let unix_timestamp = weather.dt
    let dateTime = new Date(unix_timestamp*1000)
    let date= document.createElement('p')
    date.textContent=`Date: ${dateTime}`
    locationDiv.appendChild(date)

    let city =document.createElement('p')
    city.textContent=`City: ${weather.name}`
    locationDiv.appendChild(city)

    let sky =document.createElement('p')
    sky.textContent=`Weather: ${weather.weather[0].main}: ${weather.weather[0].description}`
 
    
    locationDiv.appendChild(sky)

    let temp =document.createElement('p')
    temp.textContent=`Tempature: ${weather.main.temp}`
    locationDiv.appendChild(temp)

    let icon=document.createElement('img')
    icon.setAttribute('src', `http://openweathermap.org/img/wn/${weather.weather[0].icon}.png`)
    locationDiv.appendChild(icon)
}

