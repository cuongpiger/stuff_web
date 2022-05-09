console.log('hello mấy cưng')

const helloWorldBox = document.getElementById('hello-world')

// helloWorldBox.textContent = 'Hello mấy cưng'
helloWorldBox.innerHTML = 'Hello <b style="color: red;">mấy cưng</b>'

$.ajax({
    type: "GET",
    url: "/hello-world/",
    success: function(response) {
        console.log(">> Success: ", response)
    },
    error: function(error) {
        console.log('>> Error', error)
    }
});