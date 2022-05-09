console.log('hello mấy cưng')

const helloWorldBox = document.getElementById('hello-world')
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')

// helloWorldBox.textContent = 'Hello mấy cưng'
// helloWorldBox.innerHTML = 'Hello <b style="color: red;">mấy cưng</b>'

$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function(response) {
        console.log(">> Success: ", response.text)
        helloWorldBox.textContent = response.text
    },
    error: function(error) {
        console.log('>> Error', error)
    }
})

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function(response) {
        console.log(response)
        const data = response.data

        setTimeout(() => {
            spinnerBox.classList.add('not-visible')

            console.log(data)
    
            data.forEach(el => {
                postsBox.innerHTML += `
                    ${el.title} - <b>${el.body}</b><br>
                `
            });
        }, 100)
    },
    error: function(error) {
        console.log(">> Error: ", error)
    }
})