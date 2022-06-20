package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type album struct {
	ID     int
	Title  string
	Artist string
	Price  float64
}

var albums = []album{
	{ID: 1, Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{2, "Jeru", "Gerry Mulligan", 17.99},
	{3, "Sarah Vaughan and Clifford Brown", "Sarah Vaughan", 39.99},
}

func main() {
	router := gin.Default()

	router.GET("/albums", getAlbums)
	router.POST("/albums", postAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.PUT("/albums/:id", putAlbums)
	router.DELETE("/albums/:id", deleteAlbums)

	router.Run(":8080")
}

/**
 * Description: Get all albums
 * Method: GET
 * URL: localhost:8080/albums
 */
func getAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"data": albums})
}

/**
 * Description: Create an album
 * Method: POST
 * URL: localhost:8080/albums 
 **/
func postAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"data": "Creare albums"})
}

/**
 * Method: GET
 * URL: localhost:8080/albums/<int:id>
 */
func getAlbumByID(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"data": "Get an albums"})
}

/**
 * Method: PUT
 * URL: localhost:8080/albums/<int:id>
 */
func putAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"data": "Update an albums"})
}

/**
 * Method: DELETE
 * URL: localhost:8080/albums/<int:id>
 */
func deleteAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{"data": "Delete an albums"})
}
