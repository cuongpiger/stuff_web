package router

import (
	"github.com/gin-gonic/gin"
	"github.com/monitor-cmr/web-w-go/handler"
)

func Router() *gin.Engine {
	router := gin.Default()

	al := handler.NewAlbumHandler() // create a new album handler

	router.GET("/albums", al.GetAlbums)
	router.POST("/albums", al.PostAlbums)
	router.GET("/albums/:id", al.GetAlbumByID)
	router.PUT("/albums/:id", al.PutAlbums)
	router.DELETE("/albums/:id", al.DeleteAlbums)

	return router
}
