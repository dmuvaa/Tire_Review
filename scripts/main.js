// Define a list of articles
const articles = [
    { title: "Best Tires for Subaru Outback", filename: "article1.html", contentFilename: "article-content/article-1-content.html" },
    { title: "Best Tires for Honda Civic", filename: "article-content/article2-content.html", contentFilename: "article-content/article-2-content.html" }
    // ... add more articles as they are written
];

// Function to render each article's snippet/teaser
function renderArticle(title, content, filename) {
    return `
    <article>
        <h3>${title}</h3>
        ${content}
        <a href="${filename}" class="read-more">Read More</a>
    </article>`;
}

// Load articles dynamically on the blog page
function loadArticles() {
    let articleContainer = document.getElementById('blogList');
    articleContainer.innerHTML = ''; // Clearing the "Loading..." text

    articles.forEach(article => {
        fetch(article.contentFilename)
        .then(response => response.text())
        .then(content => {
            let articleElement = renderArticle(article.title, content, article.filename);
            articleContainer.innerHTML += articleElement;
        })
        .catch(error => {
            console.error("There was an error fetching the article content.", error);
        });
    });
}

// Execute the function to display articles
loadArticles();
