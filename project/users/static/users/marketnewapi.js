const container = document.querySelector('#news-container')


async function showArticles(){
    let newsData= await getnews()
    let newsHtml = ''
    newsData?.forEach((newsArticle) => {
    newsHtml += `<div class="col-4">
        <div class="card" style="height:100%"> 
        <img src="${newsArticle.image_url}" class="card-img-top" alt="...">
            <div class="card-body">
            <h5 class="card-title">${newsArticle.title}</h5>
            <p class=""card-text">"${newsArticle.snippet}"</p>
            <a href="${newsArticle.url}" class="btn btn-primary">Learn More</a>
            </div>
        </div>
    </div>`

    })
    container.insertAdjacentHTML('beforeend', newsHtml)
}

if(container) {
    showArticles()
}


 
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



