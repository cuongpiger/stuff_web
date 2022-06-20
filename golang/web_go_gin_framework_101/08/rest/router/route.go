package router

import (
	"github.com/gin-gonic/gin"
	"github.com/monitor-cmr/web-w-go/handler"
)

func Router() *gin.Engine {
	router := gin.Default()

	router.GET("/albums", handler.GetAlbums)
	router.POST("/albums", handler.PostAlbums)
	router.GET("/albums/:id", handler.GetAlbumByID)
	router.PUT("/albums/:id", handler.PutAlbums)
	router.DELETE("/albums/:id", handler.DeleteAlbums)

	return router
}
