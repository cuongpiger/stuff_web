package main

import "github.com/monitor-cmr/web-w-go/router"

func main() {
	router := router.Router()  // get gin.Engine from the router/route.go
	router.Run(":8080")  // run app
}
