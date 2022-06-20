package handler

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/monitor-cmr/web-w-go/domain"
	"github.com/monitor-cmr/web-w-go/service"
)

type AlbumHandler struct{
	repo service.AlbumServiceRepository
}

func NewAlbumHandler(svc service.AlbumServiceRepository) *AlbumHandler {
	return &AlbumHandler{
		repo: svc,
	}
}

/**
 * Description: Get all albums
 * Method: GET
 * URL: localhost:8080/albums
 */
func (al AlbumHandler) GetAlbums(c *gin.Context) {
	albums, err := al.repo.FetchAll()

	if err != nil {
		c.IndentedJSON(err.Code, gin.H{"message": err.Message})
		return
	}
	c.IndentedJSON(http.StatusOK, gin.H{"data": albums})
}

/**
 * Description: Create an album
 * Method: POST
 * URL: localhost:8080/albums
 **/
func (al AlbumHandler) PostAlbums(c *gin.Context) {
	var newAlbum domain.Album

	if err := c.BindJSON(&newAlbum); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	id, err := al.repo.Save(newAlbum)

	if err != nil {
		c.IndentedJSON(err.Code, gin.H{"message": err.Message})
		return
	}

	c.IndentedJSON(http.StatusOK, gin.H{"data": id})
}

/**
 * Description: Get an album by ID
 * Method: GET
 * URL: localhost:8080/albums/<int:id>
 */
func (al AlbumHandler) GetAlbumByID(c *gin.Context) {
	tempID := c.Param("id")

	id, err := strconv.Atoi(tempID)
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	album, err1 := al.repo.Fetch(id)

	if err1 != nil {
		c.IndentedJSON(err1.Code, gin.H{"message": err1.Message})
		return
	}

	c.IndentedJSON(http.StatusOK, album)
}

/**
 * Description: Update an album
 * Method: PUT
 * URL: localhost:8080/albums/<int:id>
 */
func (al AlbumHandler) PutAlbums(c *gin.Context) {
	tempID := c.Param("id") // Get the id from the URL

	id, err := strconv.Atoi(tempID) // Convert the id to an integer
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Bad Request"})
		return
	}

	var updateAlbum domain.Album

	// call BindJSON to get the data from the request
	if err := c.BindJSON(&updateAlbum); err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "Bad Request"})
		return
	}

	updateAlbum.ID = id
	err1 := al.repo.Update(updateAlbum)

	if err1 != nil {
		c.IndentedJSON(err1.Code, gin.H{"message": err1.Message})
		return
	}

	c.IndentedJSON(http.StatusOK, gin.H{"message": "Update Success"})
}

/**
 * Description: Delete an album
 * Method: DELETE
 * URL: localhost:8080/albums/<int:id>
 */
func (al AlbumHandler) DeleteAlbums(c *gin.Context) {
	tempID := c.Param("id") // Get the id from the URL

	id, err := strconv.Atoi(tempID) // Convert the id to an integer
	if err != nil {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"data": "Bad Request"})
		return
	}

	err1 := al.repo.Delete(id)

	if err1 != nil {
		c.IndentedJSON(err1.Code, gin.H{"message": err1.Message})
		return
	}

	c.IndentedJSON(http.StatusOK, gin.H{"message": "Delete Success"})
}
