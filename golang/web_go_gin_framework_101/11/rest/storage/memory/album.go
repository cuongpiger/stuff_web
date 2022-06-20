package memory

import (
	"errors"

	"github.com/monitor-cmr/web-w-go/domain"
)

type AlbumMemory struct {
	albums []domain.Album
}

func NewAlbumMemory() *AlbumMemory {
	var albums = []domain.Album{
		{ID: 1, Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
		{2, "Jeru", "Gerry Mulligan", 17.99},
		{3, "Sarah Vaughan and Clifford Brown", "Sarah Vaughan", 39.99},
	}

	return &AlbumMemory{
		albums: albums,
	}
}

func (a *AlbumMemory) SelectAll() ([]domain.Album, error) {
	return a.albums, nil
}

func (a *AlbumMemory) Select(id int) (*domain.Album, error) {
	for _, v := range a.albums {
		if v.ID == id {
			return &v, nil
		}
	}

	return nil, errors.New("Not Found")
}

func (a *AlbumMemory) Save(album domain.Album) (*int, error) {
	lenAlbum := len(a.albums)
	album.ID = a.albums[lenAlbum-1].ID + 1
	a.albums = append(a.albums, album)
	return &album.ID, nil
}

func (a *AlbumMemory) Update(album domain.Album) error {
	for i, v := range a.albums {
		if v.ID == album.ID {
			a.albums[i] = album
			return nil
		}
	}

	return errors.New("Not Found")
}

func (a *AlbumMemory) Delete(id int) error {
	for i, v := range a.albums {
		if v.ID == id {
			a.albums = append(a.albums[:i], a.albums[i+1:]...)
			return nil
		}
	}

	return errors.New("Not Found")
}