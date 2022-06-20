package service

import "github.com/monitor-cmr/web-w-go/domain"

type AlbumServiceRepository interface {
	FetchAll() ([]domain.Album, error)
	Fetch(int) (*domain.Album, error)
	Save(domain.Album) (*int, error)
	Update(domain.Album) error
	Delete(int) error
}

type AlbumService struct {
	repo domain.AlbumRepository
}

func NewAlbumService(repo domain.AlbumRepository) *AlbumService {
	return &AlbumService{
		repo: repo,
	}
}

func (s AlbumService) FetchAll() ([]domain.Album, error) {
	return s.repo.SelectAll()
}

func (s AlbumService) Fetch(id int) (*domain.Album, error) {
	return s.repo.Select(id)
}

func (s AlbumService) Save(a domain.Album) (*int, error) {
	return s.repo.Save(a)
}

func (s AlbumService) Update(a domain.Album) error {
	return s.repo.Update(a)
}

func (s AlbumService) Delete(id int) error {
	return s.repo.Delete(id)
}
