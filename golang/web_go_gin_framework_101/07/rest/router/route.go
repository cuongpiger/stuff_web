package router

import (
	"net/http"
	"strconv"

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

func Router() *gin.Engine {
	router := gin.Default()

	router.GET("/albums", getAlbums)
	router.POST("/albums", postAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.PUT("/albums/:id", putAlbums)
	router.DELETE("/albums/:id", deleteAlbums)

	return router
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
	var newAlbum album

	if err := c.BindJSON(&newAlbum); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	lenAlbum := len(albums)
	newAlbum.ID = albums[lenAlbum-1].ID + 1
	albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusOK, gin.H{"data": newAlbum.ID})
}

/**
 * Description: Get an album by ID
 * Method: GET
 * URL: localhost:8080/albums/<int:id>
 */
func getAlbumByID(c *gin.Context) {
	tempID := c.Param("id")

	id, err := strconv.Atoi(tempID)
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	for _, album := range albums {
		if album.ID == id {
			c.IndentedJSON(http.StatusOK, album)
			return
		}
	}

	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Not Found"})
}

/**
 * Description: Update an album
 * Method: PUT
 * URL: localhost:8080/albums/<int:id>
 */
func putAlbums(c *gin.Context) {
	tempID := c.Param("id") // Get the id from the URL

	id, err := strconv.Atoi(tempID) // Convert the id to an integer
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	var updateAlbum album

	// call BindJSON to get the data from the request
	if err := c.BindJSON(&updateAlbum); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	updateAlbum.ID = id
	for i, a := range albums {
		if a.ID == id {
			albums[i] = updateAlbum
			c.IndentedJSON(http.StatusOK, gin.H{"data": updateAlbum.ID})
			return
		}
	}

	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Not Found"})
}

/**
 * Description: Delete an album
 * Method: DELETE
 * URL: localhost:8080/albums/<int:id>
 */
func deleteAlbums(c *gin.Context) {
	tempID := c.Param("id") // Get the id from the URL

	id, err := strconv.Atoi(tempID) // Convert the id to an integer
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	for i, a := range albums {
		if a.ID == id {
			albums = append(albums[:i], albums[i+1:]...)
			c.IndentedJSON(http.StatusOK, gin.H{"message": "Delete Success"})
			return
		}
	}

	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Not Found"})
}
