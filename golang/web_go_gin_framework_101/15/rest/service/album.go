package service

import (
	"github.com/monitor-cmr/web-w-go/domain"
	"github.com/monitor-cmr/web-w-go/errs"
)

type AlbumServiceRepository interface {
	FetchAll() ([]domain.Album, *errs.AppErrs)
	Fetch(int) (*domain.Album, *errs.AppErrs)
	Save(domain.Album) (*int, *errs.AppErrs)
	Update(domain.Album) *errs.AppErrs
	Delete(int) *errs.AppErrs
}

type AlbumService struct {
	repo domain.AlbumRepository
}

func NewAlbumService(repo domain.AlbumRepository) *AlbumService {
	return &AlbumService{
		repo: repo,
	}
}

func (s AlbumService) FetchAll() ([]domain.Album, *errs.AppErrs) {
	return s.repo.SelectAll()
}

func (s AlbumService) Fetch(id int) (*domain.Album, *errs.AppErrs) {
	return s.repo.Select(id)
}

func (s AlbumService) Save(a domain.Album) (*int, *errs.AppErrs) {
	return s.repo.Save(a)
}

func (s AlbumService) Update(a domain.Album) *errs.AppErrs {
	return s.repo.Update(a)
}

func (s AlbumService) Delete(id int) *errs.AppErrs {
	return s.repo.Delete(id)
}
