package router

import (
	"database/sql"

	"github.com/gin-gonic/gin"
	"github.com/monitor-cmr/web-w-go/handler"
	"github.com/monitor-cmr/web-w-go/service"
	"github.com/monitor-cmr/web-w-go/storage/mysql"
)

func Router(db *sql.DB) *gin.Engine {
	router := gin.Default()
	store := mysql.NewAlbumMySQL(db)

	svcAlbum := service.NewAlbumService(store)
	al := handler.NewAlbumHandler(svcAlbum) // create a new album handler

	router.GET("/albums", al.GetAlbums)
	router.POST("/albums", al.PostAlbums)
	router.GET("/albums/:id", al.GetAlbumByID)
	router.PUT("/albums/:id", al.PutAlbums)
	router.DELETE("/albums/:id", al.DeleteAlbums)

	return router
}
