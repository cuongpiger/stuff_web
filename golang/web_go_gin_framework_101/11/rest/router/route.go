package router

import (
	"github.com/gin-gonic/gin"
	"github.com/monitor-cmr/web-w-go/handler"
	"github.com/monitor-cmr/web-w-go/storage/memory"
)

func Router() *gin.Engine {
	router := gin.Default()
	store := memory.NewAlbumMemory()
	al := handler.NewAlbumHandler(store) // create a new album handler

	router.GET("/albums", al.GetAlbums)
	router.POST("/albums", al.PostAlbums)
	router.GET("/albums/:id", al.GetAlbumByID)
	router.PUT("/albums/:id", al.PutAlbums)
	router.DELETE("/albums/:id", al.DeleteAlbums)

	return router
}
