package memory

import (
	"github.com/monitor-cmr/web-w-go/domain"
	"github.com/monitor-cmr/web-w-go/errs"
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

func (a *AlbumMemory) SelectAll() ([]domain.Album, *errs.AppErrs) {
	return a.albums, nil
}

func (a *AlbumMemory) Select(id int) (*domain.Album, *errs.AppErrs) {
	for _, v := range a.albums {
		if v.ID == id {
			return &v, nil
		}
	}

	return nil,	errs.NewNotFoundError()
}

func (a *AlbumMemory) Save(album domain.Album) (*int, *errs.AppErrs) {
	lenAlbum := len(a.albums)
	album.ID = a.albums[lenAlbum-1].ID + 1
	a.albums = append(a.albums, album)
	return &album.ID, nil
}

func (a *AlbumMemory) Update(album domain.Album) *errs.AppErrs {
	for i, v := range a.albums {
		if v.ID == album.ID {
			a.albums[i] = album
			return nil
		}
	}

	return errs.NewNotFoundError()
}

func (a *AlbumMemory) Delete(id int) *errs.AppErrs {
	for i, v := range a.albums {
		if v.ID == id {
			a.albums = append(a.albums[:i], a.albums[i+1:]...)
			return nil
		}
	}

	return errs.NewNotFoundError()
}