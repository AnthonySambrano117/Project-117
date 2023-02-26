const locationDiv =document.querySelector('#location')
const generateLocation =document.querySelector('#generatenews')
console.log('hello', generateLocation)


generateLocation.addEventListener("click", async function(){
    let newsData= await getnews()
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



