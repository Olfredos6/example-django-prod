function addToCart(id) {
    formData = new FormData()
    formData.append("id", id)
    return fetch("/cart/", {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            'X-CSRFToken': CSRFToken,
        },
        mode: "same-origin",
        body: JSON.stringify({ id })
    })
}

function populateItemsToCart(items = []) {
    if(items.length == 0){
        document.querySelector("#cart-items-list").innerHTML = `<p class="text-muted">No items.</p>`
        return
    }

    let cart_body_html = ""
    items.forEach(book => {
        cart_body_html += `
        <div class="cart-item">
            <div class="d-flex flex-row">
                <div class="mt-1">
                    <img src="${book.image}" alt="Book Thumbnail">
                </div>
                <div class="d-flex flex-row">
                    <small>${book.title}</small>
                </div>
            </div>
            <div class="d-flex flex-row justify-content-around">
                <span>$${book.price}</span>
                <i class="fas fa-trash float-left btn-remove-cart-item" data-book-id="${book.id}"></i>
            </div>
        </div>`
    })
    document.querySelector("#cart-items-list").innerHTML = cart_body_html
}

document.querySelector("#btn-add-to-cart").addEventListener("click", (e) => {
    // const cart_item = {
    //     "id": parseInt(e.currentTarget.dataset.bookId),
    //     "image_url": e.currentTarget.dataset.bookImageUrl,
    //     "title": e.currentTarget.dataset.bookTitle
    // }
    // const formData = FormData()


    addToCart(e.currentTarget.dataset.bookId)
        .then(response => {
            // Check if the request was successful (status code 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Parse the response body as JSON
            return response.json();
        })
        .then(data => {
            // Work with the JSON data
            console.log(data)
            populateItemsToCart(data)
        })
        .catch(error => {
            // Handle errors during the fetch operation
            console.error('Fetch error:', error);
        });
})

// document.querySelector("#btn-remove-cart-item").addEventListener("click", e=>{
//     fetch(`/cart/remove/${e.currentTarget.dataset.bookId}`)
//     .then(response => {
//         // Check if the request was successful (status code 200-299)
//         if (!response.ok) {
//           throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         // Parse the response body as JSON
//         return response.json();
//       })
//       .then(data => {
//         // Work with the JSON data
//         populateItemsToCart(data)
//       })
//       .catch(error => {
//         // Handle errors during the fetch operation
//         console.error('Fetch error:', error);
//       });
// })

$("body").on("click", ".btn-remove-cart-item", e => {
    fetch(`/cart/remove/${e.currentTarget.dataset.bookId}`)
        .then(response => {
            // Check if the request was successful (status code 200-299)
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Parse the response body as JSON
            return response.json();
        })
        .then(data => {
            // Work with the JSON data
            populateItemsToCart(data)
        })
        .catch(error => {
            // Handle errors during the fetch operation
            console.error('Fetch error:', error);
        });
})


populateItemsToCart(JSON.parse(document.getElementById('cart-data').textContent))
